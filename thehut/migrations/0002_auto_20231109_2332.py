# Generated by Django 3.2.23 on 2023-11-09 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thehut', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='num_guests',
            field=models.IntegerField(choices=[(2, 2), (4, 4)]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
