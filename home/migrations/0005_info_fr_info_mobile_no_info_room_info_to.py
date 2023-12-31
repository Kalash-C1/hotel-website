# Generated by Django 4.1 on 2023-06-24 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_remove_info_room"),
    ]

    operations = [
        migrations.AddField(
            model_name="info",
            name="fr",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="info",
            name="mobile_no",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="info",
            name="room",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="info",
            name="to",
            field=models.DateField(blank=True, null=True),
        ),
    ]
