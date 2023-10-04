from django.db import models


class ProductBicycle(models.Model):
    bicycle_image = models.ImageField(null=True, blank=True, upload_to='store/products/bicycles/%Y/%m/%d/')
    bicycle_price = models.IntegerField()
    bicycle_name = models.CharField(max_length=300)
    bicycle_frame_size = models.IntegerField()
    bicycle_number_of_speeds = models.IntegerField()
    bicycle_type = models.CharField(max_length=100)
    bicycle_class = models.CharField(max_length=100)
    bicycle_manufacturer_country = models.CharField(max_length=100)
    bicycle_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.bicycle_name
