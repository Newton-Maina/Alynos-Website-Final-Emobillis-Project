# Generated by Django 4.2.6 on 2023-11-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System_App', '0002_checkoutform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=255)),
                ('department_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('message', models.TextField()),
            ],
        ),
    ]