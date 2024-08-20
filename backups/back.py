from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Backup
from .forms import BackupForm
import os
import shutil
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import BackupForm
from .models import Backup
from django.utils import timezone
import subprocess
from .forms import BackupForm
from .models import Backup  # Mueve esta línea a la función si es posible

from .models import UserProfile

def es_superusuario(user):
    return user.is_superuser

def acceso_denegado(request):
    return render(request, 'acceso_denegado.html')

def registrarme(request):
    error_message = None
    success_message = None

    if request.method == 'POST':
        if 'password1' in request.POST:
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password1 and password2:
                if password1 == password2:
                    try:
                        existing_user = UserProfile.objects.get(numero=request.POST['numero'])
                        error_message = 'El número de documento ya está en uso'
                    except UserProfile.DoesNotExist:
                        try:
                            user = UserProfile.objects.create(
                                tipo=request.POST['type'],
                                numero=request.POST['numero'],
                                username=request.POST['username'],
                                email=request.POST['email'],
                                password=password1
                            )
                            user.set_password(password1)
                            user.save()
                            success_message = 'Cuenta Creada Correctamente, Por favor inicie sesión'
                        except IntegrityError as e:
                            if 'unique constraint' in str(e):
                                error_message = 'El usuario ya fue creado'
                            else:
                                error_message = f'Error al crear el usuario: {e}'
                else:
                    error_message = 'Las contraseñas no coinciden'
        else:
            numero = request.POST.get('numer')
            password = request.POST.get('contra')
            user = authenticate(request, username=numero, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                error_message = 'Credenciales inválidas'

    context = {
        'error': error_message,
        'done': success_message
    }
    return render(request, 'loginregister.html', context)

def base(request):
    return render(request, 'index.html')

def cuidados(request):
    return render(request, 'cuidados.html')

def about(request):
    return render(request, 'about.html')

def loginregister(request):
    return render(request, 'loginregister.html')

def inicio(request):
    return render(request, 'inicio.html')

def backup_list(request):
    backups = Backup.objects.all()
    return render(request, 'backup_crud.html', {'backups': backups})

import os
import subprocess
from datetime import datetime
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.core.paginator import Paginator
from django.views import View

# Vista basada en clase para crear un respaldo de la base de datos
class BackupDatabaseView(View):
    def post(self, request, *args, **kwargs):
        try:
            # Obtener la configuración de la base de datos
            db_settings = settings.DATABASES['default']
            db_name = db_settings['NAME']
            db_user = db_settings['USER']
            db_password = db_settings['PASSWORD']
            db_host = db_settings['HOST']
            db_port = db_settings['PORT']

            # Crear el nombre del archivo de respaldo
            filename = request.POST.get('filename', f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql")
            backup_dir = os.path.join(settings.BASE_DIR, 'backups')
            backup_path = os.path.join(backup_dir, filename)

            # Asegurarse de que el directorio de respaldos existe
            os.makedirs(backup_dir, exist_ok=True)

            # Usa la ruta completa a mysqldump.exe
            mysqldump_path = r"C:\Program Files\MySQL\MySQL Server 9.0\bin\mysqldump.exe"

            # Comando para crear el respaldo
            command = (
                f"\"{mysqldump_path}\" -h {db_host} -P {db_port} -u {db_user} -p{db_password} "
                f"{db_name} > \"{backup_path}\""
            )

            # Ejecutar el comando y capturar la salida
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                messages.error(request, f"Error al crear el respaldo: {result.stderr}")
            else:
                messages.success(request, f"Respaldo creado exitosamente: {filename}")
        except Exception as e:
            messages.error(request, f"Error al crear el respaldo: {str(e)}")

        return redirect('backup_list')
# Vista para listar los respaldos
def backup_list(request):
    backup_dir = os.path.join(settings.BASE_DIR, 'backups')
    backups = []
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
    
    # Paginación
    paginator = Paginator(backups, 10)  # 10 respaldos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'backup_list.html', {'page_obj': page_obj})

# Vista para restaurar la base de datos
class RestoreDatabaseView(View):
    def post(self, request, *args, **kwargs):
        # Obtener el nombre del archivo desde el campo oculto
        backup_filename = request.POST.get('backup_file')

        if backup_filename:
            try:
                # Obtener la configuración de la base de datos
                db_settings = settings.DATABASES['default']
                db_name = db_settings['NAME']
                db_user = db_settings['USER']
                db_password = db_settings['PASSWORD']
                db_host = db_settings['HOST']
                db_port = db_settings['PORT']

                # Construir la ruta del archivo de respaldo
                backup_dir = os.path.join(settings.BASE_DIR, 'backups')
                backup_path = os.path.join(backup_dir, backup_filename)

                # Verificar que el archivo de respaldo existe
                if not os.path.exists(backup_path):
                    messages.error(request, "El archivo de respaldo especificado no existe.")
                    return redirect('backup_list')

                # Comando para restaurar la base de datos
                command = (
                    f"mysql -h {db_host} -P {db_port} -u {db_user} -p{db_password} "
                    f"{db_name} < {backup_path}"
                )

                # Ejecutar el comando
                result = subprocess.run(command, shell=True, capture_output=True, text=True)

                # Para depuración, imprime la salida del comando
                print("Salida del comando:", result.stdout)
                print("Error del comando:", result.stderr)

                if result.returncode != 0:
                    messages.error(request, f"Error al restaurar la base de datos: {result.stderr}")
                else:
                    messages.success(request, f"Base de datos restaurada desde {backup_filename}")

            except Exception as e:
                messages.error(request, f"Error al restaurar la base de datos: {str(e)}")
        else:
            messages.error(request, "No se especificó un archivo para restaurar")

        return redirect('backup_list')
# Vista para descargar un respaldo
def download_backup(request, filename):
    file_path = os.path.join(settings.BASE_DIR, 'backups', filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404

# Vista para eliminar un respaldo
class DeleteBackupView(View):
    def post(self, request, *args, **kwargs):
        filename = request.POST.get('filename')
        if filename:
            file_path = os.path.join(settings.BASE_DIR, 'backups', filename)
            if os.path.exists(file_path):
                os.remove(file_path)
                messages.success(request, f"Respaldo {filename} eliminado exitosamente")
            else:
                messages.error(request, f"El archivo {filename} no existe")
        else:
            messages.error(request, "No se especificó un archivo para eliminar")

        return redirect('backup_list')