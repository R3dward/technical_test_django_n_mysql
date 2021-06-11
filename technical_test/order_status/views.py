from django.shortcuts import render
from order_status.models import OrderStatus
from shipping_label.models import Shipping_data
from shipping_label.forms import Shipping_Status
import random


# Create your views here.

def shipping_status(request):
    ordered_by = Shipping_data.objects.all()
    context = {
        "form": Shipping_Status(),
        "ordered_by": ordered_by,
    }

    form = Shipping_Status(request.POST or None, request.FILES or None)
    if request.method == "POST":
        order_number = str(random.randint(a=0, b=99999))
        order_status = request.POST["order_status"]
        item = request.POST["item"]
        price = request.POST["price"]
        bought_by = Shipping_data.objects.filter(phone_number=request.POST["bought_by"])
        new_entry = OrderStatus(bought_by_id=bought_by[0].id, order_number=order_number, order_status=order_status,
                                item=item, price=price)
        new_entry.save()
    return render(request, "item_info.html", context)
