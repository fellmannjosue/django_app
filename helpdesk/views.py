from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Ticket
from .forms import TicketForm

def submit_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            print("Ticket guardado correctamente:", ticket)

            # Enviar un correo al técnico con plantilla HTML
            subject_technician = f'Nuevo Ticket #{ticket.id} - {ticket.name}'
            message_technician = render_to_string('helpdesk/email/email_notification.html', {'ticket': ticket})
            send_mail(
                subject=subject_technician,
                message='',
                from_email='techcare.app2024@gmail.com',
                recipient_list=['techcare.app2024@gmail.com'],
                fail_silently=False,
                html_message=message_technician,
            )

            # Enviar una copia al usuario con plantilla HTML
            subject_user = f'Ticket #{ticket.id} - Confirmación de Recepción'
            message_user = render_to_string('helpdesk/email/email_notification.html', {'ticket': ticket})
            send_mail(
                subject=subject_user,
                message='',
                from_email='techcare.app2024@gmail.com',
                recipient_list=[ticket.email],
                fail_silently=False,
                html_message=message_user,
            )

            return redirect('success')
        else:
            print(form.errors)  # Imprime los errores si el formulario no es válido

    else:
        form = TicketForm()

    return render(request, 'helpdesk/submit_ticket.html', {'form': form})

def success(request):
    return render(request, 'helpdesk/success.html')

def technician_dashboard(request):
    tickets = Ticket.objects.all()
    return render(request, 'helpdesk/technician_dashboard.html', {'tickets': tickets})

def update_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        ticket.status = new_status
        ticket.save()

        # Enviar notificación por correo al usuario con plantilla HTML
        subject_update = f'Ticket #{ticket.id} - Estado Actualizado'
        message_update = render_to_string('helpdesk/email/ticket_update.html', {'ticket': ticket, 'technician_name': 'Equipo Técnico'})
        send_mail(
            subject=subject_update,
            message='',
            from_email='techcare.app2024@gmail.com',
            recipient_list=[ticket.email],
            fail_silently=False,
            html_message=message_update,
        )

        return redirect('technician_dashboard')

    return render(request, 'helpdesk/update_ticket.html', {'ticket': ticket})
