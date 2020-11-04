# Generated by Django 3.1.3 on 2020-11-04 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dansbagels', '0006_populate_OrderStatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttype',
            name='accountType_text',
            field=models.CharField(choices=[(4, 'Manager'), (3, 'Chef'), (2, 'Cashier'), (1, 'Customer')], max_length=20),
        ),
    ]