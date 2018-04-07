from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from apps.productos.models import Producto
from apps.productos.models import Compra
from apps.productos.forms import CompraForm
# Create your views here.

import json

@csrf_exempt
def confirmarpago(request):
	if request.method == 'POST':
		data = json.loads(request.body.decode('utf-8'))
		codigo_transaccion = data['codigo_transaccion']
		forma_pago = data['forma_pago']
		medio_pago = data['medio_pago']
		importe_autorizado = data['importe_autorizado']
		numero_pedido = data['numero_pedido']
		codigo_autorizacion = data['codigo_autorizacion']
		numero_tarjeta = data['numero_tarjeta']
		nombre_tarjeta_habiente = data['nombre_tarjeta_habiente']
		email = data['email']
		fecha = data['fecha']
		#do what you have to do
		print(codigo_transaccion)
		comp = Compra.objects.get(codigo = codigo_transaccion)
		if float(importe_autorizado) == float(comp.importe):


			resJSON = {
				'codigo_transaccion': codigo_transaccion,
				'estado': 'correcto',
				'mensaje': 'unMensaje'
			}
		else:
			resJSON = {
				'codigo_transaccion': 'C000P00021',
				'estado': 'error',
				'mensaje': 'unMensaje'
			}
		return JsonResponse(resJSON)

def formatIntegerWithZeros(n, zeros):
	lenN = len(str(n))
	res = ''
	for a in range(zeros - lenN):
		res += '0'

	return '{0}{1}'.format(res, n)

def tienda_view(request):
	if request.method == 'POST':
		form = CompraForm(request.POST)
		tabladetalle = form.data['tabladetalle']
		importe = form.data['importe']
		cliente = User.objects.get(id = form.data['cliente'])
		nitems = form.data['nitems']

		q = Compra(tabladetalle = tabladetalle, importe = importe, cliente = cliente, nitems = nitems)
		q.save()
		idq = q.id
		print(idq)
		n1 = idq // 100000
		n2 = idq % 100000
		q.codigo = "C{0}P{1}".format(formatIntegerWithZeros(n1,3),formatIntegerWithZeros(n2,5))
		q.save()

		return render(request, 'views/formToPayToPeru.html', {'user': cliente, 'compra': q, 'RUCPalerp': '20491228297' })
	else:
		form = CompraForm()
	productos = Producto.objects.all()
	return render(request, 'views/tienda.html', {'productos':productos, 'form': form})

def prueba(request):
	return render(request, 'views/prueba.html')

'''def payToPeruPost_view(request):
	if request.methos == 'POST':
		re_POST = request.POST
		codigo_transaccion = re_POST['codigo_transaccion']
		forma_pago = re_POST['forma_pago']
		medio_pago = re_POST['medio_pago']
		'''
