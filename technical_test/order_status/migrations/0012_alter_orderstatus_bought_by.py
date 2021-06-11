# Generated by Django 3.2.4 on 2021-06-11 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_label', '0002_alter_shipping_data_id'),
        ('order_status', '0011_alter_orderstatus_bought_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='bought_by',
            field=models.ForeignKey(db_column='bought_by', null=True, on_delete=django.db.models.deletion.CASCADE, to='shipping_label.shipping_data'),
        ),
    ]
