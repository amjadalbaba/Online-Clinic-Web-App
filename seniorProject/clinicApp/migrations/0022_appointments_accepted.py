# Generated by Django 3.1.7 on 2021-05-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0021_auto_20210429_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='accepted',
            field=models.IntegerField(null=True),
        ),
    ]
