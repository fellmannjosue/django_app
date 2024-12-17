from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Ticket
from .forms import TicketForm
import os
import json
from threading import Thread

# Ruta de URL pública para imágenes
PUBLIC_IMAGE_URL = "http://127.0.0.1:8000/static/helpdesk/img/favicon.png"

def send_email_async(subject, message, recipient_list):
    """Función para enviar correos de forma asíncrona."""
    Thread(
        target=send_mail,
        args=(subject, '', 'techcare.app2024@gmail.com', recipient_list),
        kwargs={'html_message': message, 'fail_silently': False}
    ).start()

@csrf_exempt
def submit_ticket(request):
    if request.method == 'POST':
        # Manejar solicitudes JSON desde PyQt5
        if request.headers.get('Content-Type') == 'application/json':
            try:
                data = json.loads(request.body)
                name = data.get('name')
                grade = data.get('grade')
                email = data.get('email')
                description = data.get('description')

                # Validar que todos los campos estén completos
                if not all([name, grade, email, description]):
                    return JsonResponse({'error': 'Todos los campos son obligatorios'}, status=400)

                # Crear el ticket
                ticket = Ticket.objects.create(
                    name=name,
                    grade=grade,
                    email=email,
                    description=description
                )

                # Enviar correo al técnico
                subject_technician = f'Nuevo Ticket #{ticket.id} - {ticket.name}'
                message_technician = render_to_string(
                    'helpdesk/email/email_notification.html',
                    {'ticket': ticket, 'img_url': PUBLIC_IMAGE_URL}
                )
                send_email_async(subject_technician, message_technician, ['techcare.app2024@gmail.com'])

                # Enviar correo al usuario
                subject_user = f'Ticket #{ticket.id} - Confirmación de Recepción'
                message_user = render_to_string(
                    'helpdesk/email/email_notification.html',
                    {'ticket': ticket, 'img_url': PUBLIC_IMAGE_URL}
                )
                send_email_async(subject_user, message_user, [ticket.email])

                return JsonResponse({'message': f'Ticket #{ticket.id} creado exitosamente'}, status=201)

            except json.JSONDecodeError:
                return JsonResponse({'error': 'Error al procesar los datos JSON'}, status=400)

        # Manejar solicitudes estándar desde formularios web
        else:
            form = TicketForm(request.POST)
            if form.is_valid():
                ticket = form.save()

                # Correo al técnico
                subject_technician = f'Nuevo Ticket #{ticket.id} - {ticket.name}'
                message_technician = render_to_string(
                    'helpdesk/email/email_notification.html',
                    {'ticket': ticket, 'img_url': PUBLIC_IMAGE_URL}
                )
                send_email_async(subject_technician, message_technician, ['techcare.app2024@gmail.com'])

                # Copia al usuario
                subject_user = f'Ticket #{ticket.id} - Confirmación de Recepción'
                message_user = render_to_string(
                    'helpdesk/email/email_notification.html',
                    {'ticket': ticket, 'img_url': PUBLIC_IMAGE_URL}
                )
                send_email_async(subject_user, message_user, [ticket.email])

                messages.success(request, f'Ticket #{ticket.id} creado exitosamente.')
                return JsonResponse({'message': f'Ticket #{ticket.id} creado exitosamente'}, status=201)

            else:
                errors = form.errors.as_json()
                return JsonResponse({'error': 'Error en el formulario', 'details': errors}, status=400)

    else:
        form = TicketForm()

    return render(request, 'helpdesk/submit_ticket.html', {'form': form})


def success(request):
    return render(request, 'helpdesk/success.html')


@login_required
def technician_dashboard(request):
    tickets = Ticket.objects.all()
    messages.info(request, 'Bienvenido al Dashboard de Técnico.')
    return render(request, 'helpdesk/technician_dashboard.html', {'tickets': tickets})


@login_required
def update_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        ticket.status = new_status
        ticket.save()

        # Notificación al usuario
        subject_update = f'Ticket #{ticket.id} - Estado Actualizado'
        message_update = render_to_string(
            'helpdesk/email/ticket_update.html',
            {'ticket': ticket, 'technician_name': 'Equipo Técnico', 'img_url': PUBLIC_IMAGE_URL}
        )
        send_email_async(subject_update, message_update, [ticket.email])

        messages.success(request, f'El estado del ticket #{ticket.id} se actualizó correctamente.')
        return redirect('technician_dashboard')

    return render(request, 'helpdesk/update_ticket.html', {'ticket': ticket})
