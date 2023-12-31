# Generated by Django 4.2.5 on 2023-10-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_framesize_frame_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framesize',
            name='frame_size',
            field=models.CharField(choices=[('L', 'L'), ('M', 'M'), ('XL', 'XL'), ('S', 'S')], max_length=10),
        ),
        migrations.AlterField(
            model_name='wheelsize',
            name='wheel_size',
            field=models.CharField(choices=[('26', '26'), ('24', '24'), ('28', '28')], max_length=10),
        ),
    ]
