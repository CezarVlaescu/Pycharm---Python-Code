import random
import string

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import CreateView

from userprofile.forms import NewAccountForm


class CreateNewAccount(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'aplicatie1/locations_form.html'
    form_class = NewAccountForm

    def form_invalid(self, form):
        print(form.errors.as_json())
        return super().form_invalid(form)

    def get_success_url(self):
        psw = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase +
                                                   string.digits + '!$%?#@') for _ in range(8))
        if (user_instance := User.objects.filter(id=self.object.id)) and user_instance.exists():
            user_object = user_instance.first()
            user_object.set_password(psw)
            user_object.save()

            content = f"Datele de autentificare sunt: \n {user_object.username} \n {psw}"
            msg_html = render_to_string('registration/invite_user.html', {'content_email': content})
            email = EmailMultiAlternatives(subject='Date conectare aplicatie',
                                           body=content,
                                           from_email='contact@test.ro',
                                           to=[user_object.email])
            email.attach_alternative(msg_html, 'text/html')
            email.send()
        return reverse('locations:lista_locatii')
