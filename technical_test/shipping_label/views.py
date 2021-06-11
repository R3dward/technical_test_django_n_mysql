from django.shortcuts import render
from shipping_label.forms import UserShippingForm, Shipping_Status
from order_status.models import OrderStatus
from django.http import HttpResponseRedirect


# Create your views here.

def home_page(request):
    orders = OrderStatus.objects.all()

    context = {
        "orders": orders,
    }

    if request.method == "POST":
        # deleted method
        print("bye bye")
        OrderStatus.objects.get(order_number=request.POST["order_number"]).delete()
        return HttpResponseRedirect("http://127.0.0.1:8000/")

    return render(request, "home.html", context)


def edit_order_details(request, order_number):
    order_posted_to = OrderStatus.objects.filter(order_number=order_number).values("id")[0]
    update_entry = OrderStatus.objects.get(id=order_posted_to["id"])
    entry = OrderStatus.objects.filter(order_number=order_number).values()

    def set_properties(form, entry):
        for field in form.fields:
            if field == "bought_by":
                field2 = "bought_by_id"
                form.fields[field].initial = entry[0][field2]
            else:
                form.fields[field].initial = entry[0][field]
        return form

    context = {
        "form": set_properties(Shipping_Status(), entry),
        "order_number": order_number
    }

    if request.method == "POST":
        update_entry.order_status = request.POST["order_status"]
        update_entry.item = request.POST["item"]
        update_entry.price = request.POST["price"]
        update_entry.save()
        return HttpResponseRedirect('/edit_order/' + order_number)

    return render(request, "edit.html", context)


def shipping_data(request):
    context = {
        "form": UserShippingForm
    }
    if request.method == "POST":
        form = UserShippingForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
    return render(request, "user_data.html", context)
