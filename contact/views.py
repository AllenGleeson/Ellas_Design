from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm
from django.core.mail import send_mail


def contact(request):
    """ A view for the contact page """

    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        comment = form.cleaned_data.get("comment")

        if request.user.is_authenticated:
            subject = str(request.user) + "'s Comment"
        else:
            subject = "A Visitor's Comment"

        # Sends a the users message to the site owner
        comment = name + " with the email, " + email + \
            ", sent the following message:\n\n" + comment
        send_mail(subject, comment, settings.DEFAULT_FROM_EMAIL, [email])

        message = 'Thank you! I will get back to you as soon as I can!'

        context = {'form': form, 'message': message}
    else:
        context = {'form': form}

    return render(request, 'contact/contact.html', context)
