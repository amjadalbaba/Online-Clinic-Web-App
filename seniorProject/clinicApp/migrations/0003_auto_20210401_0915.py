# Generated by Django 3.1.7 on 2021-04-01 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0002_auto_20210401_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='firstName',
            new_name='firstNamee',
        ),
    ]
