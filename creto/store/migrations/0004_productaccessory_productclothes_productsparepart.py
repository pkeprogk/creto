# Generated by Django 4.2.5 on 2023-10-12 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_productbicycle_bicycle_type_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAccessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessory_image', models.ImageField(blank=True, null=True, upload_to='store/products/accessories/%Y/%m/%d/')),
                ('accessory_type', models.CharField(blank=True, max_length=300, null=True)),
                ('accessory_price', models.IntegerField()),
                ('accessory_name', models.CharField(blank=True, max_length=300, null=True)),
                ('accessory_brand', models.CharField(blank=True, max_length=300, null=True)),
                ('accessory_size', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductClothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_image', models.ImageField(blank=True, null=True, upload_to='store/products/clothes/%Y/%m/%d/')),
                ('clothes_type', models.CharField(blank=True, max_length=300, null=True)),
                ('clothes_price', models.IntegerField()),
                ('clothes_name', models.CharField(blank=True, max_length=300, null=True)),
                ('clothes_brand', models.CharField(blank=True, max_length=300, null=True)),
                ('clothes_size', models.CharField(blank=True, max_length=300, null=True)),
                ('clothes_sex', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSparePart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spare_part_image', models.ImageField(blank=True, null=True, upload_to='store/products/spare_parts/%Y/%m/%d/')),
                ('spare_part_type', models.CharField(blank=True, max_length=300, null=True)),
                ('spare_part_price', models.IntegerField()),
                ('spare_part_name', models.CharField(blank=True, max_length=300, null=True)),
                ('spare_part_brand', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
