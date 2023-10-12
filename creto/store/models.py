from django.db import models


class ProductBicycle(models.Model):
    bicycle_image = models.ImageField(null=True, blank=True, upload_to='store/products/bicycles/%Y/%m/%d/')
    bicycle_type_image = models.ImageField(null=True, blank=True, upload_to='store/products/bicycles/%Y/%m/%d/')
    bicycle_price = models.IntegerField()
    bicycle_name = models.CharField(max_length=300, null=True, blank=True)
    bicycle_brand = models.CharField(max_length=300, null=True, blank=True)
    bicycle_frame_size = models.IntegerField()
    bicycle_wheel_size = models.IntegerField(null=True)
    bicycle_number_of_speeds = models.IntegerField()
    bicycle_type = models.CharField(max_length=100)
    bicycle_class = models.CharField(max_length=100)
    bicycle_manufacturer_country = models.CharField(max_length=100)
    bicycle_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.bicycle_name


class ProductAccessory(models.Model):
    accessory_image = models.ImageField(null=True, blank=True, upload_to='store/products/accessories/%Y/%m/%d/')
    accessory_type = models.CharField(max_length=300, null=True, blank=True)
    accessory_price = models.IntegerField()
    accessory_name = models.CharField(max_length=300, null=True, blank=True)
    accessory_brand = models.CharField(max_length=300, null=True, blank=True)
    accessory_size = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.bicycle_name


class ProductClothes(models.Model):
    clothes_image = models.ImageField(null=True, blank=True, upload_to='store/products/clothes/%Y/%m/%d/')
    clothes_type = models.CharField(max_length=300, null=True, blank=True)
    clothes_price = models.IntegerField()
    clothes_name = models.CharField(max_length=300, null=True, blank=True)
    clothes_brand = models.CharField(max_length=300, null=True, blank=True)
    clothes_size = models.CharField(max_length=300, null=True, blank=True)
    clothes_sex = models.CharField(max_length=300, null=True, blank=True)


class ProductSparePart(models.Model):
    spare_part_image = models.ImageField(null=True, blank=True, upload_to='store/products/spare_parts/%Y/%m/%d/')
    spare_part_type = models.CharField(max_length=300, null=True, blank=True)
    spare_part_price = models.IntegerField()
    spare_part_name = models.CharField(max_length=300, null=True, blank=True)
    spare_part_brand = models.CharField(max_length=300, null=True, blank=True)