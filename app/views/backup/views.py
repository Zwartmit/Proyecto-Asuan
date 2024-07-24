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
            message = f'Copia de seguridad creada exitosamente: {backup_filepath}'
            success = True
        except Exception as e:
            message = f'Error al crear la copia de seguridad: {str(e)}'
            success = False

        return JsonResponse({'message': message, 'success': success})

    def get_context_data(self, **kwargs):
        context = {}
        context['titulo'] = 'Crear Copia de Seguridad'
        context['entidad'] = 'Copias de Seguridad'
        context['crear_backup_url'] = reverse_lazy('crear_backup')
        return context
