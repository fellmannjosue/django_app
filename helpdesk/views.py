from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Ticket
from .forms import TicketForm

def submit_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()

            # Enviar un correo al técnico
            send_mail(
                subject=f'Nuevo Ticket #{ticket.id} - {ticket.name}',
                message=f'Se ha recibido un nuevo ticket.\n\n'
                        f'Nombre: {ticket.name}\n'
                        f'Grado: {ticket.grade}\n'
                        f'Email: {ticket.email}\n'
                        f'Descripción: {ticket.description}\n\n'
                        f'Estado: {ticket.status}',
                from_email='techcare.app2024@gmail.com',
                recipient_list=['techcare.app2024@gmail.com'],
                fail_silently=False,
            )

            # Enviar una copia al usuario
            send_mail(
                subject=f'Ticket #{ticket.id} - Confirmación de Recepción',
                message=f'Su ticket ha sido recibido.\n\n'
                        f'Nombre: {ticket.name}\n'
                        f'Grado: {ticket.grade}\n'
                        f'Descripción: {ticket.description}\n\n'
                        f'Gracias por su solicitud.',
                from_email='techcare.app2024@gmail.com',
                recipient_list=[ticket.email],
                fail_silently=False,
            )

            return redirect('success')
    else:
        form = TicketForm()

    return render(request, 'helpdesk/submit_ticket.html', {'form': form})

def success(request):
    return render(request, 'helpdesk/success.html')
