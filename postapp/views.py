from django.shortcuts import render
from django.core.mail import send_mail
from .form import ContactForm


def home(request):
    return render(request,'index.html')

def projects(request):
    return  render(request,'photography.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    return  render(request,'contact.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            msg = f'{name} with email {email} said:'
            msg += f'\n{subject}\n\n'
            msg += f'{message}'

            send_mail(
                subject=subject,
                message=msg,
                from_email=email,
                recipient_list = ['alijonovasilbek058@gmail.com'],  # Recipient email address
                fail_silently=False,
            )
        return render(request, 'contact.html', {'form': form})
            # Redirect on success
    else:
        form = ContactForm()  # Initialize an empty form for GET requests
    return render(request, 'contact.html', {'form': form})
