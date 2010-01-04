from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from emails.forms import EmailForm

def send_email(request):
    if request.method == "POST":
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            data = email_form.cleaned_data
            from_email = data["email_address"]
            subject = " ".join(["[biodiesel_request]", data["subject"]])
            message = data["message"]
            send_mail(subject, message, from_email, ["rgoonin@gmail.com",])      
            return HttpResponseRedirect(reverse("email_sent"))
    else:
        email_form = EmailForm()
    
    return render_to_response("emails/send_email.html", {
        "email_form": email_form,
    })


