# Generated by Django 3.1.7 on 2021-04-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0018_appointments_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='from_hour',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='to_hour',
            field=models.DateTimeField(null=True),
        ),
    ]
