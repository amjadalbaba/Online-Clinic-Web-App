# Generated by Django 3.1.7 on 2021-04-08 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0008_auto_20210406_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialityName',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
