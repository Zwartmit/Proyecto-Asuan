from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.conf import settings
import datetime
import time
import os

@method_decorator(never_cache, name='dispatch')
class BackupDatabaseView(View):
    template_name = 'backup.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        backup_filename = request.POST.get('filename', f'mysql_backup_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.sql')
        backup_dir = request.POST.get('directory', os.path.join(settings.BASE_DIR, 'backups'))

        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        backup_filepath = os.path.join(backup_dir, backup_filename)

        database_name = 'asuan_db'
        database_user = 'root'
        database_password = 'admin'

        try:
            dump_command = f"mysqldump -u {database_user} -p{database_password} {database_name} > {backup_filepath}"
            os.system(dump_command)
            message = f'Copia de seguridad creada y guardada en {backup_filepath}'
            success = True
        except Exception as e:
            message = f'No se pudo crear la copia de seguridad: {str(e)}'
            success = False

        return JsonResponse({'message': message, 'success': success})

    def get_context_data(self, **kwargs):
        context = {
            'titulo': 'Copia de seguridad',
            'entidad': 'Copia de Seguridad',
            'crear_backup_url': reverse_lazy('app:crear_backup'),
        }
        return context


@method_decorator(never_cache, name='dispatch')
class RestoreDatabaseView(View):

    def post(self, request, *args, **kwargs):
        if 'backup_file' not in request.FILES:
            return JsonResponse({'message': 'No se ha enviado ningún archivo', 'success': False})

        backup_file = request.FILES['backup_file']
        backup_filename = backup_file.name
        backup_dir = os.path.join(settings.BASE_DIR, 'backups')

        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        backup_filepath = os.path.join(backup_dir, backup_filename)

        try:
            with open(backup_filepath, 'wb+') as destination:
                for chunk in backup_file.chunks():
                    destination.write(chunk)

            database_name = 'asuan_db'
            database_user = 'root'
            database_password = 'admin'
            restore_command = f"mysql -u {database_user} -p{database_password} {database_name} < {backup_filepath}"

            time.sleep(2)
            os.system(restore_command)

            message = f'Base de datos restaurada desde {backup_filepath}'
            success = True
        except Exception as e:
            message = f'No se pudo restaurar la base de datos: {str(e)}'
            success = False
        finally:
            try:
                os.remove(backup_filepath)
            except Exception as e:
                message += f' (No se pudo eliminar el archivo de respaldo: {str(e)})'

        return JsonResponse({'message': message, 'success': success})
