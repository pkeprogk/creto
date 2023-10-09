# Generated by Django 4.2.5 on 2023-10-09 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbicycle',
            name='bicycle_brand',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='productbicycle',
            name='bicycle_wheel_size',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='productbicycle',
            name='bicycle_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
