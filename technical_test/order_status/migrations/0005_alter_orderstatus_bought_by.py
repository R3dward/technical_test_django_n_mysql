# Generated by Django 3.2.4 on 2021-06-10 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_label', '0001_initial'),
        ('order_status', '0004_alter_orderstatus_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='bought_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shipping_label.shipping_data'),
        ),
    ]
