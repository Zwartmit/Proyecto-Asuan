from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache
import os
import subprocess
from datetime import datetime
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class BackupDatabaseView(View):
    @method_decorator(permission_required('app.view_backup', raise_exception=False))
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('app.view_backup'):
            return HttpResponseRedirect(reverse('access_denied'))
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return render(request, 'backup.html')
    
    def post(self, request, *args, **kwargs):
        success = False
        try:
            db_settings = settings.DATABASES['default']
            db_name = db_settings['NAME']
            db_user = db_settings['USER']
            db_password = db_settings['PASSWORD']
            db_host = db_settings['HOST']
            db_port = db_settings['PORT']

            filename = request.POST.get('filename', f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql")
            backup_dir = os.path.join(settings.BASE_DIR, 'backups/files')
            backup_path = os.path.join(backup_dir, filename)

            os.makedirs(backup_dir, exist_ok=True)

            mysqldump_path = r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe"

            command = (
                f"\"{mysqldump_path}\" -h {db_host} -P {db_port} -u {db_user} -p{db_password} "
                f"{db_name} > \"{backup_path}\""
            )

            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                messages.error(request, f"Error al crear el respaldo: {result.stderr}")
            else:
                messages.success(request, f"Respaldo creado exitosamente: {filename}")
                success = True
        except Exception as e:
            messages.error(request, f"Error al crear el respaldo: {str(e)}")

        messages_list = list(messages.get_messages(request))
        messages_str = [str(message) for message in messages_list]

        return JsonResponse({'messages': messages_str, 'success': success})

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class RestoreDatabaseView(View):
    @method_decorator(permission_required('app.add_backup', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        success = False
        try:
            if 'backup_file' not in request.FILES:
                messages.error(request, "No se ha enviado ningún archivo")
            else:
                file = request.FILES['backup_file']
                backup_dir = os.path.join(settings.BASE_DIR, 'backups/files')
                os.makedirs(backup_dir, exist_ok=True)
                backup_path = os.path.join(backup_dir, file.name)

                with open(backup_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)

                db_settings = settings.DATABASES['default']
                db_name = db_settings['NAME']
                db_user = db_settings['USER']
                db_password = db_settings['PASSWORD']
                db_host = db_settings['HOST']
                db_port = db_settings['PORT']

                command = (
                    f"mysql -h {db_host} -P {db_port} -u {db_user} -p{db_password} "
                    f"{db_name} < \"{backup_path}\""
                )

                result = subprocess.run(command, shell=True, capture_output=True, text=True)

                if result.returncode != 0:
                    messages.error(request, f"Error al restaurar la base de datos: {result.stderr}")
                else:
                    messages.success(request, f"Base de datos restaurada desde {file.name}")
                    success = True

        except Exception as e:
            messages.error(request, f"Error al restaurar la base de datos: {str(e)}")

        messages_list = list(messages.get_messages(request))
        messages_str = [str(message) for message in messages_list]

        return JsonResponse({'messages': messages_str, 'success': success})
    
@method_decorator(never_cache, name='dispatch')
class BackupListView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            backup_dir = os.path.join(settings.BASE_DIR, 'backups/files')
            files = [f for f in os.listdir(backup_dir) if f.endswith('.sql')]
            file_data = []
            for file in files:
                file_path = os.path.join(backup_dir, file)
                file_info = {
                    'filename': file,
                    'created_at': os.path.getmtime(file_path),
                    'size': os.path.getsize(file_path)
                }
                file_data.append(file_info)
            return JsonResponse({'files': file_data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class DeleteBackupView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        filename = request.POST.get('filename')
        success = False
        if filename:
            file_path = os.path.join(settings.BASE_DIR, 'backups/files', filename)
            if os.path.exists(file_path):
                os.remove(file_path)
                messages.success(request, f"Copia: {filename} eliminada correctamente.")
                success = True
            else:
                messages.error(request, f"El archivo: {filename} no existe.")
        else:
            messages.error(request, "No se especificó un archivo para eliminar.")

        messages_list = list(messages.get_messages(request))
        messages_str = [str(message) for message in messages_list]

        return JsonResponse({'messages': messages_str, 'success': success})