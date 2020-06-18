# Generated by Django 3.0.2 on 2020-02-29 12:41

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyapp', '0007_auto_20200229_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
