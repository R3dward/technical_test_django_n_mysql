from django import forms
from shipping_label.models import Shipping_data
from order_status.models import OrderStatus


# forms.ModelForm
class UserShippingForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your name", "id": "frist_name",
                   "class": "inputs"}),
        max_length=30, help_text="Enter your first name")

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your last name", "id": "lastname",
                   "class": "inputs"}),
        max_length=30, help_text="Enter your last name")

    email = forms.EmailField(widget=forms.TextInput(
        attrs={"type": "email", "placeholder": "Enter your email"},
    ), max_length=40, help_text="Enter a valid email")

    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Enter your phone number"}
    ), max_length=10, help_text="Enter a valid phone number")

    address = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Enter your mailing address"}
    ), max_length=100, help_text="Enter your shipping address")

    class Meta:
        model = Shipping_data
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "address"
        ]


class Shipping_Status(forms.ModelForm):
    shipping_status = (
        ("in_wharehouse", "In Wharehouse"),
        ("in_shipping_facility", "In Shipping Facility"),
        ("out_for_delivery", "Out For Delivery"),
        ("attempted_delivery", "Delivery Attempted"),
        ("delived", "Delivered"),
    )

    order_status = forms.ChoiceField(required=True, choices=shipping_status,
                                     widget=forms.Select(attrs={"id": "order_status"}))

    order_number = forms.CharField(required=False, widget=forms.TextInput(attrs={"id": "order_number", "hidden": True}))

    item = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter the item's title", "id": "item"}),
        max_length=30, help_text="Enter your last name")

    price = forms.DecimalField(required=True, max_value=None, min_value=1, max_digits=None, decimal_places=2)

    bought_by = forms.CharField(required=False, widget=forms.NumberInput(attrs={"hidden": True}))

    class Meta:
        model = OrderStatus
        fields = [
            "order_number",
            "order_status",
            "item",
            "price",
            "bought_by",
        ]
