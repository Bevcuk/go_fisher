from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags
from django.forms.models import modelformset_factory, inlineformset_factory


from authentication.models import Customer

class UserCreateForm(forms.ModelForm):
    class Meta:
        fields = ['fathername', 'phone', 'city', 'street', 'house_number', 'hash_code']
        model = Customer
    #def clean_phone(self):
        #phone = self.cleaned_data["phone"]
        #for f in cleaned_data.items():
        #if phone.format()==str:
         #   return phone
        #raise forms.ValidationError('Дане поле має містити тільки цифри')

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'E-Mail'}),
            'password1': forms.PasswordInput(attrs={'placeholder': '......'}),
            'password2': forms.PasswordInput(attrs={'placeholder': '......'}),
        }

#clean email field
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Така адреса електронної пошти вже зареєстрована')

    #modify save() method so that we can set user.is_active to False when we first create our user
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False # not active until he opens activation link
            user.save()
        return user