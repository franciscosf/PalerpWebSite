from django.shortcuts import render, redirect
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
		comp = Compra.objects.get(codigo = codigo_transaccion)
		print(codigo_transaccion)
		# try:
		# 	comp = Compra.objects.get(codigo = codigo_transaccion)
		#
		# except:

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
		codigo = form.data['codigo']

		q = Compra.objects.filter(codigo = codigo, pagado = False)

		if len(q) == 0:

			return render(request, 'views/message.html', {
				'url_image': 'notok.png',
				'tittle_message': 'Ah ocurrido un error.',
				'message': 'Lo sentimos no encontramos la pagina que esta buscando.',
				'url_btn': 'index',
				'color_tittle': 'green-text',
				'btn_message': 'Ir al inicio',
			})
		q = q[0]
		cliente = q.cliente
		importe = str("{0:.2f}".format(q.importe)).replace(',','.')

		return render(request, 'views/formToPayToPeru.html', {'user': cliente, 'compra': q, 'RUCPalerp': '20491228297', 'importe': importe })
	else:
		form = CompraForm()
	productos = Producto.objects.all()
	return render(request, 'views/tienda.html', {'productos':productos, 'form': form})

def prueba(request):
	return render(request, 'views/prueba.html')

@csrf_exempt
def apivalidarcompra(request):
	if request.method == "POST":
		data = json.loads(request.body.decode('utf-8'))
		total = float(0)
		productosEnCarrito = {}
		r = True
		for key, val in data.items():
			if key != 'case':
				pro = val
				q = Producto.objects.filter(codigo = pro['codigo'])
				if len(q) == 1 and pro['cantidad'] > 0:
					q = q[0]
					proNuevo = {}
					proNuevo['cadenacaracteristicas'] = q.cadenacaracteristicas
					proNuevo['cantidad'] = pro['cantidad']
					proNuevo['categoria'] = q.categoria
					proNuevo['codigo'] = q.codigo
					proNuevo['codigofabricante'] = q.codigofabricante
					proNuevo['descripcion'] = q.descripcion
					proNuevo['imagen'] = q.imagen.url
					proNuevo['nombre'] = q.nombre
					proNuevo['precio'] = q.precio
					productosEnCarrito[q.categoria + q.nombre] = proNuevo
					cantidad = float(pro['cantidad'])
					precio = float(q.precio)
					total += float(cantidad * precio)
				else:
					r = False
					break

		if r == False :
			resJSON = {
				'estado' : 'W',
				'total' : total,
				'pec' : productosEnCarrito,
			}

		else:
			resJSON = {
				'estado' : 'R',
				'total' : total,
				'pec' : productosEnCarrito,
			}
			if(data['case'] == '1'):
				tabladetalle = "<table class=''><thead class='left-align'><tr><th>Item</th><th>Nombre</th><th>Cantidad</th><th>Vr.Unitario</th><th>Vr. Total</th></tr></thead><tbody>"
				nitem = 1
				for key, val in productosEnCarrito.items():
					tabladetalle += "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>S/. {3:.2f}</td><td>S/. {4:.2f}</td></tr>".format(nitem, val['nombre'], val['cantidad'], float(val['precio']), float(float(val['precio']) * float(val['cantidad'])))
					nitem += 1
				tabladetalle += "<tr><td></td><td></td>x<td></td><td>Total</td><td>S/. {0:.2f}</td></tr></tbody></table>".format(total)
				cliente = User.objects.get(id = request.user.id)
				q = Compra(tabladetalle = tabladetalle, importe = total, cliente = cliente, nitems = len(productosEnCarrito))
				q.save()
				idq = q.id
				n1 = idq // 100000
				n2 = idq % 100000
				q.codigo = "C{0}P{1}".format(formatIntegerWithZeros(n1,3),formatIntegerWithZeros(n2,5))
				q.save()
				resJSON['codigo'] = q.codigo


		return JsonResponse(resJSON)
	else:
		return render(request, 'views/message.html', {
			'url_image': 'notok.png',
			'tittle_message': '404 Not Found',
			'message': 'Lo sentimos no encontramos la pagina que esta buscando.',
			'url_btn': 'index',
			'color_tittle': 'green-text',
			'btn_message': 'Ir al inicio',
		})


'''def payToPeruPost_view(request):
	if request.methos == 'POST':
		re_POST = request.POST
		codigo_transaccion = re_POST['codigo_transaccion']
		forma_pago = re_POST['forma_pago']
		medio_pago = re_POST['medio_pago']
		'''
