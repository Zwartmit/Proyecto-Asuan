import os
import subprocess
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views import View
from django.conf import settings
from datetime import datetime
from django.http import JsonResponse
from django.contrib import messages

@method_decorator(never_cache, name='dispatch')
class BackupDatabaseView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        contexto = {
            'titulo': 'Gestión de bases de datos'
        }
        return render(request, 'backup.html', contexto)

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


@method_decorator(never_cache, name='dispatch')
class BackupListView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        backup_dir = os.path.join(settings.BASE_DIR, 'backups/files')
        backups = []

        if os.path.exists(backup_dir):
            for filename in os.listdir(backup_dir):
                if filename.endswith('.sql'):
                    file_path = os.path.join(backup_dir, filename)
                    created_at = datetime.fromtimestamp(os.path.getctime(file_path))
                    size = os.path.getsize(file_path)
                    backups.append({
                        'filename': filename,
                        'created_at': created_at.strftime('%Y-%m-%d %H:%M:%S'),
                        'size': f"{size / 1024 / 1024:.2f} MB"
                    })
        
        backups.sort(key=lambda x: x['created_at'], reverse=True)
        return render(request, 'backup.html', {'backups': backups})
    
@method_decorator(never_cache, name='dispatch')
class RestoreDatabaseView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        success = False
        try:
            backup_file = request.FILES.get('backup_file')
            if not backup_file:
                raise Http404("No se especificó un archivo de respaldo")

            filename = backup_file.name
            
            if not filename.endswith('.sql'):
                raise ValueError("El archivo debe tener una extensión .sql")

            backup_dir = os.path.join(settings.BASE_DIR, 'backups/files')
            backup_path = os.path.join(backup_dir, filename)

            os.makedirs(backup_dir, exist_ok=True)

            with open(backup_path, 'wb+') as destination:
                for chunk in backup_file.chunks():
                    destination.write(chunk)

            db_settings = settings.DATABASES['default']
            db_name = db_settings['NAME']
            db_user = db_settings['USER']
            db_password = db_settings['PASSWORD']
            db_host = db_settings['HOST']
            db_port = db_settings['PORT']

            command = ['mysql', '-h', db_host, '-P', db_port, '-u', db_user, f"-p{db_password}", db_name]
            with open(backup_path, 'r') as input_file:
                result = subprocess.run(command, stdin=input_file, stderr=subprocess.PIPE, text=True)

            if result.returncode != 0:
                messages.error(request, f"Error al restaurar la base de datos: {result.stderr}")
            else:
                messages.success(request, f"Base de datos restaurada desde {filename}")
                success = True

        except ValueError as ve:
            messages.error(request, str(ve))
        except Exception as e:
            messages.error(request, f"Error al restaurar la base de datos: {str(e)}")

        messages_list = list(messages.get_messages(request))
        messages_str = [str(message) for message in messages_list]

        return JsonResponse({'messages': messages_str, 'success': success})

@method_decorator(never_cache, name='dispatch')
class DeleteBackupView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        filename = request.POST.get('filename')
        if filename:
            file_path = os.path.join(settings.BASE_DIR, 'backups', filename)
            if os.path.exists(file_path):
                os.remove(file_path)
                messages.success(request, f"Respaldo {filename} eliminado exitosamente")
                success = True
            else:
                messages.error(request, f"El archivo {filename} no existe")
                success = False
        else:
            messages.error(request, "No se especificó un archivo para eliminar")
            success = False

        messages_list = list(messages.get_messages(request))
        messages_str = [str(message) for message in messages_list]

        return JsonResponse({'messages': messages_str, 'success': success})
