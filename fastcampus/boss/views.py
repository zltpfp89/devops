from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from order.models import Shop, Menu, Order, OrderFood
from order.serializers import ShopSerializer, MenuSerializer, OrderSerializer, OrderFoodSerializer

# Create your views here.
@csrf_exempt
def order_list(request, shop):
    if request.method == 'GET':
        order = Order.objects.filter(shop=shop)
        return render(request, 'boss/order_list.html', {'order_list':order})

@csrf_exempt
def time_input(request):
    if request.method == 'POST':
        order_item = Order.objects.get(pk = request.POST['order_id'])
        shop = order_item.shop.id
        order_item.estimated_time = int(request.POST['estimated_time'])
        order_item.save()

        return render(request, 'boss/success.html', {'shop':shop})
    
    else:
        return HttpResponse(status=404)