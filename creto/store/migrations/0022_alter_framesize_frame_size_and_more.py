# Generated by Django 4.2.5 on 2023-11-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_framesize_frame_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framesize',
            name='frame_size',
            field=models.CharField(choices=[('S', 'S'), ('L', 'L'), ('M', 'M'), ('XL', 'XL')], max_length=10),
        ),
        migrations.AlterField(
            model_name='wheelsize',
            name='wheel_size',
            field=models.CharField(choices=[('28', '28'), ('26', '26'), ('24', '24')], max_length=10),
        ),
    ]
