# Generated by Django 3.2.4 on 2021-06-22 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialhandle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialhandle',
            name='copyright_date',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
