from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
import os
import datetime
import shutil
from django.conf import settings

class BackupDatabaseView(View):
    template_name = 'backup.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        backup_filename = request.POST.get('filename', f'asuan_db_backup_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.sqlite3')
        backup_dir = request.POST.get('directory', os.path.join(settings.BASE_DIR, 'backups'))

        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        backup_filepath = os.path.join(backup_dir, backup_filename)
        database_filepath = os.path.join(settings.BASE_DIR, 'asuan_db.sqlite3')

        try:
            shutil.copy2(database_filepath, backup_filepath)
            message = f'Guardada en {backup_filepath}'
            success = True
        except Exception as e:
            message = f'No se pudo crear la copia de seguridad: {str(e)}'
            success = False

        return JsonResponse({'message': message, 'success': success})

    def get_context_data(self, **kwargs):
        context = {
            'titulo': 'Copia de seguridad',
            'entidad': 'Copia de Seguridad',
            'crear_backup_url': reverse_lazy('crear_backup'),
        }
        return context

class RestoreDatabaseView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'backup_file' not in request.FILES:
            return JsonResponse({'message': 'No se ha enviado ningún archivo', 'success': False})

        backup_file = request.FILES['backup_file']
        backup_filename = backup_file.name
        backup_dir = os.path.join(settings.BASE_DIR, 'backups')
        backup_filepath = os.path.join(backup_dir, backup_filename)
        database_filepath = os.path.join(settings.BASE_DIR, 'asuan_db.sqlite3')

        try:
            with open(backup_filepath, 'wb+') as destination:
                for chunk in backup_file.chunks():
                    destination.write(chunk)

            shutil.copy2(backup_filepath, database_filepath)
            message = f'Base de datos restaurada desde {backup_filepath}'
            success = True
        except Exception as e:
            message = f'No se pudo restaurar la base de datos: {str(e)}'
            success = False
        finally:
            if os.path.exists(backup_filepath):
                os.remove(backup_filepath)

        return JsonResponse({'message': message, 'success': success})
