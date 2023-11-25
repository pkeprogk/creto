# Generated by Django 4.2.5 on 2023-10-16 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_framesize_frame_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framesize',
            name='frame_size',
            field=models.CharField(choices=[('XL', 'XL'), ('L', 'L'), ('M', 'M'), ('S', 'S')], max_length=10),
        ),
        migrations.AlterField(
            model_name='productbicycle',
            name='bicycle_price_new',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='wheelsize',
            name='wheel_size',
            field=models.CharField(choices=[('24', '24'), ('28', '28'), ('26', '26')], max_length=10),
        ),
    ]