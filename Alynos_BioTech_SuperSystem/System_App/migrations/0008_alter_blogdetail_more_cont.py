# Generated by Django 4.2.6 on 2023-11-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System_App', '0007_blogdetail_more_cont'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetail',
            name='more_cont',
            field=models.TextField(blank=True),
        ),
    ]