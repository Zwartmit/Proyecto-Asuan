import io
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
from app.models import *

@login_required
@never_cache
def export_categorias_pdf(request):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    style_title = styles['Title']
    style_heading = styles['Heading2']
    style_normal = styles['Normal']

    # Título
    title = Paragraph("Reporte de Categorías", style_title)
    elements.append(title)
    
    # Fecha
    fecha = datetime.now().strftime("%d/%m/%Y")
    date_paragraph = Paragraph(f"Fecha: {fecha}", style_normal)
    elements.append(date_paragraph)

    # Cabeceras de la tabla
    headers = ['ID', 'Categoría', 'Estado']
    data = [headers]

    # Datos de categorías
    categorias = Categoria.objects.all()
    for categoria in categorias:
        row = [categoria.id, categoria.categoria, 'Activo' if categoria.estado else 'Inactivo']
        data.append(row)

    # Crear tabla
    table = Table(data, colWidths=[1.5*inch] * 3)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (0, 51, 102)),
        ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
    ]))

    elements.append(table)

    doc.build(elements)
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Reporte_de_Categorias.pdf'
    return response

@login_required
@never_cache
def export_marcas_pdf(request):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    style_title = styles['Title']
    style_heading = styles['Heading2']
    style_normal = styles['Normal']

    # Título
    title = Paragraph("Reporte de Marcas", style_title)
    elements.append(title)

    # Fecha
    fecha = datetime.now().strftime("%d/%m/%Y")
    date_paragraph = Paragraph(f"Fecha: {fecha}", style_normal)
    elements.append(date_paragraph)

    # Cabeceras de la tabla
    headers = ['ID', 'Marca', 'Estado']
    data = [headers]

    # Datos de marcas
    marcas = Marca.objects.all()
    for marca in marcas:
        row = [marca.id, marca.marca, 'Activo' if marca.estado else 'Inactivo']
        data.append(row)

    # Crear tabla
    table = Table(data, colWidths=[1.5*inch] * 3)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (0, 51, 102)),
        ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
    ]))

    elements.append(table)

    doc.build(elements)
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Reporte_de_Marcas.pdf'
    return response

@login_required
@never_cache
def export_presentaciones_pdf(request):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    style_title = styles['Title']
    style_heading = styles['Heading2']
    style_normal = styles['Normal']

    # Título
    title = Paragraph("Reporte de Presentaciones", style_title)
    elements.append(title)

    # Fecha
    fecha = datetime.now().strftime("%d/%m/%Y")
    date_paragraph = Paragraph(f"Fecha: {fecha}", style_normal)
    elements.append(date_paragraph)

    # Cabeceras de la tabla
    headers = ['ID', 'Presentación', 'Estado']
    data = [headers]

    # Datos de presentaciones
    presentaciones = Presentacion.objects.all()
    for presentacion in presentaciones:
        row = [presentacion.id, f"{presentacion.presentacion} {presentacion.unidad_medida}", 'Activo' if presentacion.estado else 'Inactivo']
        data.append(row)

    # Crear tabla
    table = Table(data, colWidths=[1.5*inch] * 3)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (0, 51, 102)),
        ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
    ]))

    elements.append(table)

    doc.build(elements)
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Reporte_de_Presentaciones.pdf'
    return response

@login_required
@never_cache
def export_productos_pdf(request):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    style_title = styles['Title']
    style_heading = styles['Heading2']
    style_normal = styles['Normal']

    # Título
    title = Paragraph("Reporte de Productos", style_title)
    elements.append(title)

    # Fecha
    fecha = datetime.now().strftime("%d/%m/%Y")
    date_paragraph = Paragraph(f"Fecha: {fecha}", style_normal)
    elements.append(date_paragraph)

    # Cabeceras de la tabla
    headers = ['ID', 'Producto', 'Cantidad', 'Valor', 'Estado', 'Categoría', 'Marca', 'Presentación']
    data = [headers]

    # Datos de productos
    productos = Producto.objects.all()
    for producto in productos:
        row = [
            producto.id,
            producto.producto,
            producto.cantidad,
            producto.valor,
            'Activo' if producto.estado else 'Inactivo',
            producto.id_categoria.categoria,
            producto.id_marca.marca,
            f"{producto.id_presentacion.presentacion} {producto.id_presentacion.unidad_medida}"
        ]
        data.append(row)

    # Crear tabla
    table = Table(data, colWidths=[1.5*inch] * 8)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (0, 51, 102)),
        ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
    ]))

    elements.append(table)

    doc.build(elements)
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Reporte_de_Productos.pdf'
    return response

def export_platos_pdf(request):
    # Configurar el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Reporte_de_platos.pdf'

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Agregar título
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title = Paragraph("Reporte de Platos", title_style)
    elements.append(title)

    # Agregar fecha
    date_style = ParagraphStyle(name='DateStyle', fontSize=12, alignment=1)
    date = Paragraph(f"Fecha: {datetime.now().strftime('%d/%m/%Y')}", date_style)
    elements.append(date)

    # Preparar datos de la tabla
    headers = ['ID', 'Plato', 'Descripción', 'Precio', 'Estado']
    platos = Plato.objects.all().values_list('id', 'plato', 'descripcion', 'precio', 'estado')

    data = [headers]
    for plato in platos:
        data.append(list(plato))

    # Crear tabla
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#04644B'),
        ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, '#000000'),
        ('BACKGROUND', (0, 1), (-1, -1), '#F5F5F5'),
        ('ALIGN', (1, 1), (-1, -1), 'LEFT'),
    ]))
    elements.append(table)

    # Construir el PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def export_meseros_pdf(request):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']

    # Header
    title = "Reporte de Meseros"
    elements.append(Paragraph(title, title_style))

    # Date
    fecha = datetime.now().strftime("%d/%m/%Y")
    date_text = f"Fecha: {fecha}"
    elements.append(Paragraph(date_text, normal_style))

    # Table
    data = [['ID', 'Nombre', 'Tipo de documento', '# de documento', 'Email', 'Prefijo', 'Teléfono']]
    meseros = Mesero.objects.all()
    for mesero in meseros:
        data.append([mesero.id, mesero.nombre, mesero.tipo_documento, mesero.numero_documento, mesero.email, mesero.pais_telefono, mesero.telefono])

    table = Table(data, colWidths=[0.5*inch] * len(data[0]))
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    doc.build(elements)

    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_de_meseros.pdf"'
    buffer.close()
    return response

def export_clientes_pdf(request):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']

    # Header
    title = "Reporte de Clientes"
    elements.append(Paragraph(title, title_style))

    # Date
    fecha = datetime.now().strftime("%d/%m/%Y")
    date_text = f"Fecha: {fecha}"
    elements.append(Paragraph(date_text, normal_style))

    # Table
    data = [['ID', 'Nombre', 'Tipo de documento', '# de documento', 'Email', 'Prefijo', 'Teléfono']]
    clientes = Cliente.objects.all()
    for cliente in clientes:
        data.append([cliente.id, cliente.nombre, cliente.tipo_documento, cliente.numero_documento, cliente.email, cliente.pais_telefono, cliente.telefono])

    table = Table(data, colWidths=[0.5*inch] * len(data[0]))
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    doc.build(elements)

    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_de_clientes.pdf"'
    buffer.close()
    return response

def export_administradores_pdf(request):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']

    # Header
    title = "Reporte de Administradores"
    elements.append(Paragraph(title, title_style))

    # Date
    fecha = datetime.now().strftime("%d/%m/%Y")
    date_text = f"Fecha: {fecha}"
    elements.append(Paragraph(date_text, normal_style))

    # Table
    data = [['ID', 'Nombre', 'Tipo de documento', '# de documento', 'Email', 'Teléfono']]
    administradores = Administrador.objects.all()
    for administrador in administradores:
        data.append([administrador.id, administrador.nombre, administrador.tipo_documento, administrador.numero_documento, administrador.user.email, administrador.telefono])

    table = Table(data, colWidths=[0.5*inch] * len(data[0]))
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    doc.build(elements)

    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_de_administradores.pdf"'
    buffer.close()
    return response

def export_operadores_pdf(request):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']

    # Header
    title = "Reporte de Operadores"
    elements.append(Paragraph(title, title_style))

    # Date
    fecha = datetime.now().strftime("%d/%m/%Y")
    date_text = f"Fecha: {fecha}"
    elements.append(Paragraph(date_text, normal_style))

    # Table
    data = [['ID', 'Nombre', 'Tipo de documento', '# de documento', 'Email', 'Teléfono']]
    operadores = Operador.objects.all()
    for operador in operadores:
        data.append([operador.id, operador.nombre, operador.tipo_documento, operador.numero_documento, operador.user.email, operador.telefono])

    table = Table(data, colWidths=[0.5*inch] * len(data[0]))
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    doc.build(elements)

    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_de_operadores.pdf"'
    buffer.close()
    return response
