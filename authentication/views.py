import datetime
import hashlib
import random
import string

from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils import timezone

from authentication.forms import UserCreateForm, UserForm
from authentication.models import Customer


# То є вхід
def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Ви ввели неправильний логін чи пароль!!!!!!"
            return render_to_response('authentication/login.html', args)
    else:
        return render_to_response('authentication/login.html', args)


# А це вихід
def logout(request):
    auth.logout(request)
    return redirect("/")


# То реєстрація
def register_user(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = UserForm(request.POST)
        args['form'] = form
        args['form2'] = UserCreateForm()
        newuser_form2 = UserCreateForm(request.POST)
        if form.is_valid() & newuser_form2.is_valid():
            user = form.save()
            profile = newuser_form2.save(commit=False)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            salt_bytes = (string.ascii_letters + string.digits).encode('ascii')
            salt = bytes([random.choice(salt_bytes) for _ in range(5)])
            activation_key = hashlib.sha1(salt + email.encode('utf8')).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            profile.user = user
            profile.activation_key = activation_key
            profile.key_expires = key_expires
            profile.save()
            User.objects.get(username=username)
            email_subject = 'Подтверждение регистрации'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
                                48hours http://127.0.0.1:8000/auth/confirm/%s" % (username, profile.activation_key)
            send_mail(email_subject, email_body, 'myemail@example.com', [email], fail_silently=False)
            return HttpResponseRedirect('/auth/register_success/')
        else:
            args['form'] = form
            args['form2'] = newuser_form2
            return render(request, 'authentication/register.html', args)
            # return render_to_response('authentication/register.html', args, context_instance=RequestContext(request))
    else:
        args['form'] = UserForm()
        args['form2'] = UserCreateForm()
        return render_to_response('authentication/register.html', args, context_instance=RequestContext(request))


def register_confirm(request, activation_key):
    args = {}
    if request.user.is_authenticated():
        HttpResponseRedirect('/auth/register_success/')
    # else:
    user_profile = get_object_or_404(Customer, activation_key=activation_key)
    if timezone.now() > user_profile.key_expires:
        return render_to_response('authentication/confirm_expired.html')
    user = user_profile.user
    user.is_active = True
    user.save()
    args.update(csrf(request))
    return render_to_response('authentication/login.html', args)


def register_success(request):
    return render(request, 'authentication/success.html')
