from django.db import models


class Transaction(BaseModel):
    email = models.CharField(max_length=256, null=True, blank=True)
    paid_amount = models.IntegerField(default=0)
    txn_id = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.PositiveSmallIntegerField(choices=)


class DriverPayment(BaseModel):
    driver = models.ForeignKey(Driver)
    payment = models.FloatField(default=0.0)
