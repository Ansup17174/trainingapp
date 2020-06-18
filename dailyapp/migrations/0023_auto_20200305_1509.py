# Generated by Django 3.0.2 on 2020-03-05 14:09

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyapp', '0022_auto_20200304_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='weight',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]