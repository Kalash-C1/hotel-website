# Generated by Django 4.2.2 on 2023-06-22 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_info_mobile_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='fr',
        ),
        migrations.RemoveField(
            model_name='info',
            name='to',
        ),
    ]
