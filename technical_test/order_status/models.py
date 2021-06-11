from django.db import models
from shipping_label.models import Shipping_data


# Create your models here.

class OrderStatus(models.Model):
    id = models.AutoField(primary_key=True)
    order_number = models.CharField(max_length=5)
    bought_by = models.ForeignKey(Shipping_data, null=True, on_delete=models.CASCADE)
    order_status = models.TextField(max_length=16)
    item = models.TextField(max_length=40)
    price = models.TextField(max_length=30)

    def __str__(self):
        return self.order_number

    class Meta:
        ordering = ['order_number']
