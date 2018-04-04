from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from apps.general.forms import PosibleClienteForm

# Create your views here.

def usuario_view(request):
    return render(request, 'views/usuario.html')

def index_view(request):
    if request.method == 'POST':
        form = PosibleClienteForm(request.POST)
        if form.is_valid():
            re_POST = request.POST
            RUC = re_POST['RUC']
            nombre = re_POST['nombre']
            email = re_POST['email']
            telefono = re_POST['telefono']

            fromEmail = 'from@gmail.com'
            toEmail = 'francisco.farfan.lazo@gmail.com'
            send_mail(
                'Contactenme Palerp',
                """Cliente con los siguientes datos quiere contactarnos.
RUC: {0}
Nombre: {1}
Email: {2}
Telefono: {3}""".format(RUC,nombre,email,telefono),
                fromEmail,
                [toEmail],
                fail_silently=False,
            )
            form.save()
            message = ''
            ok = True
            return render(request, 'views/message.html', {
                'url_image': 'ok.png',
                'tittle_message': 'Prefecto!',
                'message': 'Todos sus datos fueron enviados correctamente en unos momentos uno de nuestros trabajadores se contactara con usted para brindarle toda la ayuda posible.',
                'url_btn': 'index',
                'color_tittle': 'green-text',
                'btn_message': 'Volver al inicio',
            })
        else:
            message = ' '
            ok = False
            return render(request, 'views/message.html', {
                'url_image': 'notok.png',
                'tittle_message': 'Algo salio mal',
                'message': 'Lo sentimos no se puedo enviar sus datos correctamente. Le pedimos disculpas del caso y lo invitamos a que intente enviarnos sus datos nuevamente.',
                'url_btn': 'contactanos',
                'color_tittle': 'red-text',
                'btn_message': 'Intentar de nuevo',
            })
    else:
        form = PosibleClienteForm()

    return render(request, 'views/index.html', {'form': form})

def post_contactanos_view(request):

    return render(request, 'views/message.html')

def productos_view(request):
    return render(request, 'views/productos.html')

def nosotros_view(request):
    return render(request, 'views/nosotros.html')

def contactanos_view(request):
    form = PosibleClienteForm()

    return render(request, 'views/contactanos.html', {'form':form})

def clientes_view(request):
    return render(request, 'views/clientes.html')
