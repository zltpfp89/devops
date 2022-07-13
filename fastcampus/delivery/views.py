from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from order.models import Shop, Menu, Order, OrderFood
from order.serializers import ShopSerializer, MenuSerializer, OrderSerializer, OrderFoodSerializer

# Create your views here.
@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        return render(request, 'delivery/order_list.html', {'order_list':orders})

    elif request.method == 'POST':
        order_item = Order.objects.get(pk = request.POST['order_id'])
        order_item.deliver_finish = 1
        order_item.save()

        return render(request, 'delivery/success.html')