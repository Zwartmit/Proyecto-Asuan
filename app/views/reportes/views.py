from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app.forms import ReporteForm
from app.views.reportes.viewsExcel import *
from app.views.reportes.viewsPDF import *

def get(self, request, *args, **kwargs):
    contexto = {
        'titulo': 'Gestión de bases de datos'
    }
    return render(request, 'backup.html', contexto)

@login_required
@never_cache
def reporte_selector(request):
    if request.method == 'POST':
        tipo_reporte = request.POST.get('tipo_reporte')
        formato = request.POST.get('formato')
        
        if formato == 'excel':
            if tipo_reporte == 'categoria':
                return export_categorias_excel(request)
            elif tipo_reporte == 'marca':
                return export_marcas_excel(request)
            elif tipo_reporte == 'presentacion':
                return export_presentaciones_excel(request)
            elif tipo_reporte == 'producto':
                return export_productos_excel(request)
            elif tipo_reporte == 'plato':
                return export_platos_excel(request)
            elif tipo_reporte == 'mesero':
                return export_meseros_excel(request)
            elif tipo_reporte == 'cliente':
                return export_clientes_excel(request)
            elif tipo_reporte == 'administrador':
                return export_administradores_excel(request)
            elif tipo_reporte == 'operador':
                return export_operadores_excel(request)
            elif tipo_reporte == 'venta':
                return export_ventas_excel(request)
            elif tipo_reporte == 'detalle_venta':
                return export_detalle_ventas_excel(request)
            elif tipo_reporte == 'cuenta':
                return export_cuentas_excel(request)
        elif formato == 'pdf':
            if tipo_reporte == 'categoria':
                return export_categorias_pdf(request)
            elif tipo_reporte == 'marca':
                return export_marcas_pdf(request)
            elif tipo_reporte == 'presentacion':
                return export_presentaciones_pdf(request)
            elif tipo_reporte == 'producto':
                return export_productos_pdf(request)
            elif tipo_reporte == 'plato':
                return export_platos_pdf(request)
            elif tipo_reporte == 'mesero':
                return export_meseros_pdf(request)
            elif tipo_reporte == 'cliente':
                return export_clientes_pdf(request)
            elif tipo_reporte == 'administrador':
                return export_administradores_pdf(request)
            elif tipo_reporte == 'operador':
                return export_operadores_pdf(request)
            elif tipo_reporte == 'venta':
                return export_ventas_pdf(request)
            elif tipo_reporte == 'detalle_venta':
                return export_detalle_ventas_pdf(request)
            elif tipo_reporte == 'cuenta':
                return export_cuentas_pdf(request)
    else:
        form = ReporteForm() 

    contexto = {
        'titulo': 'Generar reportes',
        'entidad': 'Generar reportes'
    }
    
    return render(request, 'reportes.html', contexto)

