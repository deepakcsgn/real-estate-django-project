# Generated by Django 2.0.1 on 2018-10-25 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20181025_0619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='Age',
        ),
        migrations.AlterField(
            model_name='houseaddress',
            name='landmark',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
