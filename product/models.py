from django.db import models


class ProductImage(BaseModel):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    product_image = modelsCharField(max_length=256, null=True, blank=True)
    type = models.CharField(max_length=256, null=True, blank=True)


class Product(BaseModel):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    colour = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    length = models.CharField(max_length=256, null=True, blank=True)
    height = models.CharField(max_length=256, null=True, blank=True)
    width = models.CharField(max_length=256, null=True, blank=True)
    weight = models.CharField(max_length=256, null=True, blank=True)
    seller_name = models.CharField(max_length=256, null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=) # enum('Active','Inactive','Deleted','') NOT NULL DEFAULT 'Active',


class Parcel(BaseModel):
    order = models.ForeignKey(Order)
    item_description = models.CharField(max_length=256, null=True, blank=True)
    item_dimension = models.CharField(max_length=256, null=True, blank=True)
    item_weight = models.CharField(max_length=256, null=True, blank=True)
    dropoffadress = models.CharField(max_length=256, null=True, blank=True)
    dropoff_lat = models.CharField(max_length=256, null=True, blank=True)
    dropoff_long = models.CharField(max_length=256, null=True, blank=True)
    receiver_name = models.CharField(max_length=256, null=True, blank=True)
    receiver_number = models.CharField(max_length=256, null=True, blank=True)
    lbs = models.CharField(max_length=256, null=True, blank=True)
    inches = models.CharField(max_length=256, null=True, blank=True)
