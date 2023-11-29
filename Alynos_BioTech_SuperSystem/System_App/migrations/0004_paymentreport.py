# Generated by Django 4.2.6 on 2023-11-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System_App', '0003_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Payment Reports',
            },
        ),
    ]
