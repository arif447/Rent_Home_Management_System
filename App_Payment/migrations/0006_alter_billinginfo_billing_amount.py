# Generated by Django 4.0.2 on 2022-09-25 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Payment', '0005_remove_billinginfo_billing_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billinginfo',
            name='billing_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
