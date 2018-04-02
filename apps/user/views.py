from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from apps.user.tokens import account_activation_token
from django.core.mail import EmailMessage

from apps.user.forms import RegistroForm

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activa tu cuenta.'
            message = render_to_string('views/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'views/message.html', {
                'url_image': 'mail.png',
                'tittle_message': 'Confirme su email',
                'message': 'Hemos enviado un link de confirmacion a su correo electronico para que active su cuenta.',
                'url_btn': 'index',
                'color_tittle': 'green-text',
                'btn_message': 'Ir a la pagina principal',
            })
    else:
        form = RegistroForm()
    return render(request, 'views/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        #login(request, user)
        # return redirect('home')
        return render(request, 'views/message.html', {
            'url_image': 'ok.png',
            'tittle_message': 'Activacion correcta',
            'message': 'Su cuenta ah sido activada correctamente ahora puede iniciar su sesion.',
            'url_btn': 'login',
            'color_tittle': 'green-text',
            'btn_message': 'Iniciar Sesion',
        })
    else:
        return render(request, 'views/message.html', {
            'url_image': 'notok.png',
            'tittle_message': 'Error',
            'message': 'El link de confirmacion al que usted desea ingresar ah expirado.',
            'url_btn': 'index',
            'color_tittle': 'red-text',
            'btn_message': 'Ir a la pagina principal',
        })
