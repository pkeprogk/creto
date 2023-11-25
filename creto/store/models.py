from django.db import models
from django.contrib.auth.models import User


class ProductBicycle(models.Model):
    bicycle_image = models.ImageField(null=True, blank=True, upload_to='store/products/bicycles/%Y/%m/%d/')
    bicycle_image1 = models.ImageField(null=True, blank=True, upload_to='store/products/bicycles/%Y/%m/%d/')
    bicycle_image2 = models.ImageField(null=True, blank=True, upload_to='store/products/bicycles/%Y/%m/%d/')
    bicycle_image3 = models.ImageField(null=True, blank=True, upload_to='store/products/bicycles/%Y/%m/%d/')
    bicycle_image4 = models.ImageField(null=True, blank=True, upload_to='store/products/bicycles/%Y/%m/%d/')
    bicycle_type_image = models.ImageField(null=True, blank=True, upload_to='store/products/bicycles/%Y/%m/%d/')
    bicycle_price_old = models.IntegerField(null=True)
    bicycle_price_new = models.IntegerField(null=True)
    bicycle_name = models.CharField(max_length=300, null=True, blank=True)
    bicycle_brand = models.CharField(max_length=300, null=True, blank=True)
    bicycle_frame_sizes = models.ManyToManyField('FrameSize', blank=True)
    bicycle_wheel_sizes = models.ManyToManyField('WheelSize', blank=True)
    bicycle_number_of_speeds = models.IntegerField()
    bicycle_type = models.CharField(max_length=100)
    bicycle_class = models.CharField(max_length=100)
    bicycle_manufacturer_country = models.CharField(max_length=100)
    bicycle_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.bicycle_name


class FrameSize(models.Model):
    FRAME_SIZES = {
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    }

    frame_size = models.CharField(max_length=10, choices=FRAME_SIZES)

    def __str__(self):
        return self.frame_size


class WheelSize(models.Model):
    WHEEL_SIZES = {
        ('24', '24'),
        ('26', '26'),
        ('28', '28'),
    }

    wheel_size = models.CharField(max_length=10, choices=WHEEL_SIZES)

    def __str__(self):
        return self.wheel_size


class ProductAccessory(models.Model):
    accessory_image = models.ImageField(null=True, blank=True, upload_to='store/products/accessories/%Y/%m/%d/')
    accessory_type = models.CharField(max_length=300, null=True, blank=True)
    accessory_price = models.IntegerField()
    accessory_name = models.CharField(max_length=300, null=True, blank=True)
    accessory_brand = models.CharField(max_length=300, null=True, blank=True)
    accessory_size = models.CharField(max_length=300, null=True, blank=True)
    accessory_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.accessory_name


class ProductClothes(models.Model):
    clothes_image = models.ImageField(null=True, blank=True, upload_to='store/products/clothes/%Y/%m/%d/')
    clothes_type = models.CharField(max_length=300, null=True, blank=True)
    clothes_price = models.IntegerField()
    clothes_name = models.CharField(max_length=300, null=True, blank=True)
    clothes_brand = models.CharField(max_length=300, null=True, blank=True)
    clothes_size = models.CharField(max_length=300, null=True, blank=True)
    clothes_sex = models.CharField(max_length=300, null=True, blank=True)
    clothes_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.clothes_name


class ProductSparePart(models.Model):
    spare_part_image = models.ImageField(null=True, blank=True, upload_to='store/products/spare_parts/%Y/%m/%d/')
    spare_part_type = models.CharField(max_length=300, null=True, blank=True)
    spare_part_price = models.IntegerField()
    spare_part_name = models.CharField(max_length=300, null=True, blank=True)
    spare_part_brand = models.CharField(max_length=300, null=True, blank=True)
    spare_part_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.spare_part_name


class Message(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    comments = models.TextField()
    submission_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductBicycle, on_delete=models.CASCADE)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
