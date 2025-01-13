from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Ticket
from .forms import TicketForm
import json
from threading import Thread

# Public URL for static images
PUBLIC_IMAGE_URL = "https://soporte.ana-hn.org:437/static/helpdesk/img/favicon.png"

def send_email_with_attachment(subject, message, recipient_list, attachment=None):
    """
    Sends emails with an optional attachment.
    """
    email = EmailMessage(subject, message, 'techcare.app2024@gmail.com', recipient_list)
    email.content_subtype = 'html'  # Set the content type to HTML
    if attachment:  # Attach the file if provided
        email.attach_file(attachment)
    email.send(fail_silently=False)  # Sends the email

@csrf_exempt
def submit_ticket(request):
    """
    Handles ticket submissions from web users or PyQt5 clients.
    Supports file attachments and sends notification emails.
    """
    if request.method == 'POST':
        # Handle JSON requests from PyQt5
        if request.headers.get('Content-Type') == 'application/json':
            try:
                # Parse JSON data
                data = json.loads(request.body)
                name = data.get('name')
                grade = data.get('grade')
                email = data.get('email')
                description = data.get('description')

                # Validate required fields
                if not all([name, grade, email, description]):
                    return JsonResponse({'error': 'All fields are required'}, status=400)

                # Create the ticket
                ticket = Ticket.objects.create(
                    name=name,
                    grade=grade,
                    email=email,
                    description=description
                )

                # Send notification email to the technician
                subject_technician = f'New Ticket #{ticket.id} - {ticket.name}'
                message_technician = render_to_string(
                    'helpdesk/email/email_notification.html',
                    {'ticket': ticket, 'img_url': PUBLIC_IMAGE_URL}
                )
                send_email_with_attachment(subject_technician, message_technician, ['techcare.app2024@gmail.com'])

                # Send confirmation email to the user
                subject_user = f'Ticket #{ticket.id} - Confirmation Received'
                message_user = render_to_string(
                    'helpdesk/email/email_notification.html',
                    {'ticket': ticket, 'img_url': PUBLIC_IMAGE_URL}
                )
                send_email_with_attachment(subject_user, message_user, [ticket.email])

                return JsonResponse({'message': f'Ticket #{ticket.id} created successfully'}, status=201)

            except json.JSONDecodeError:
                return JsonResponse({'error': 'Error processing JSON data'}, status=400)

        # Handle standard form submissions from the web
        else:
            form = TicketForm(request.POST, request.FILES)  # Include request.FILES for file uploads
            if form.is_valid():
                # Save the ticket to the database
                ticket = form.save()

                # File attachment path
                attachment_path = ticket.attachment.path if ticket.attachment else None

                # Send notification email to the technician
                subject_technician = f'New Ticket #{ticket.id} - {ticket.name}'
                message_technician = render_to_string(
                    'helpdesk/email/email_notification.html',
                    {'ticket': ticket, 'img_url': PUBLIC_IMAGE_URL}
                )
                send_email_with_attachment(subject_technician, message_technician, ['techcare.app2024@gmail.com'], attachment_path)

                # Send confirmation email to the user
                subject_user = f'Ticket #{ticket.id} - Confirmation Received'
                message_user = render_to_string(
                    'helpdesk/email/email_notification.html',
                    {'ticket': ticket, 'img_url': PUBLIC_IMAGE_URL}
                )
                send_email_with_attachment(subject_user, message_user, [ticket.email], attachment_path)

                messages.success(request, f'Ticket #{ticket.id} created successfully.')
                return redirect('success')  # Redirect to the success page

            else:
                messages.error(request, 'Error in the form. Please check the fields.')
                return render(request, 'helpdesk/submit_ticket.html', {'form': form})

    else:
        form = TicketForm()
        return render(request, 'helpdesk/submit_ticket.html', {'form': form})


@login_required
def success(request):
    """
    Renders a success page after ticket submission.
    """
    return render(request, 'helpdesk/success.html')


@login_required
def technician_dashboard(request):
    """
    Displays the technician's dashboard with a list of all tickets.
    """
    tickets = Ticket.objects.all()
    messages.info(request, 'Welcome to the Technician Dashboard.')
    return render(request, 'helpdesk/technician_dashboard.html', {'tickets': tickets})


@login_required
def update_ticket(request, ticket_id):
    """
    Allows technicians to update ticket status and add comments.
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        new_comments = request.POST.get('comments')

        # Update ticket status
        if new_status and new_status != ticket.status:
            ticket.status = new_status

        # Update ticket comments
        if new_comments is not None:
            ticket.comments = new_comments

        # Save changes
        ticket.save()

        # Notify the user about the update
        subject_update = f'Ticket #{ticket.id} - Status Updated'
        message_update = render_to_string(
            'helpdesk/email/ticket_update.html',
            {
                'ticket': ticket,
                'technician_name': 'Technical Team',
                'comments': ticket.comments,
                'img_url': PUBLIC_IMAGE_URL
            }
        )
        send_email_with_attachment(subject_update, message_update, [ticket.email])

        messages.success(request, f'Ticket #{ticket.id} updated successfully.')
        return redirect('technician_dashboard')

    return render(request, 'helpdesk/update_ticket.html', {'ticket': ticket})
