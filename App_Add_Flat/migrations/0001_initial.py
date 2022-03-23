# Generated by Django 4.0.2 on 2022-03-16 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=400, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Update_Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('House_rent', models.FloatField(blank=True, null=True)),
                ('Utility_bill', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Add_Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Flat_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('House_name', models.CharField(blank=True, max_length=250, null=True)),
                ('Floor', models.IntegerField(blank=True, null=True)),
                ('Flat_number', models.CharField(blank=True, max_length=50, null=True)),
                ('Square_feet', models.FloatField(blank=True, null=True)),
                ('Bedroom', models.IntegerField(blank=True, null=True)),
                ('Guest_room', models.IntegerField(blank=True, null=True)),
                ('Number_of_bath', models.IntegerField(blank=True, null=True)),
                ('Number_of_balcony', models.IntegerField(blank=True, null=True)),
                ('House_rent', models.FloatField(blank=True, null=True)),
                ('Utility_bill', models.FloatField(blank=True, null=True)),
                ('Address', models.TextField(blank=True, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='App_Add_Flat.category')),
            ],
            options={
                'ordering': ['-Created_at'],
            },
        ),
    ]
