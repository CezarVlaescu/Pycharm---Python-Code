from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'last name', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'username', 'class': 'form-control'}),
        }

    def clean(self):
        field_data = self.cleaned_data
        email_value = field_data.get('email')
        if User.objects.filter(email=email_value).exists():
            msg = "Emailul deja exista! Te rugam sa adaugi un alt email"
            self._errors['email'] = self.error_class([msg])
        return field_data
