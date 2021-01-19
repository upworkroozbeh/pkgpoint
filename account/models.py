from django.db import models


class CustomUser(AbstractUser, BaseModel):
    verify = models.CharField(max_length=256, null=True, blank=True)
    device_token = models.CharField(max_length=256, null=True, blank=True)
    facebook_id = models.CharField(max_length=256, null=True, blank=True)
    social_type = models.CharField(max_length=256, null=True, blank=True)
    social_id = models.CharField(max_length=256, null=True, blank=True)
    firstname = models.CharField(max_length=256, null=True, blank=True)
    lastname = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    paypal_email = models.CharField(max_length=256, null=True, blank=True)
    password = models.CharField(max_length=256, null=True, blank=True)
    country_code = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    latitude = models.CharField(max_length=256, null=True, blank=True)
    longitude = models.CharField(max_length=256, null=True, blank=True)
    dob = models.CharField(max_length=50, null=True, blank=True)
    user_status = models.BooleanField(default=True) # '1=active,2=inactive'
    reg_type = models.CharField(max_length=256, null=True, blank=True)
    type = models.PositiveSmallIntegerField(choices=) # '1=admin,0=other',
    user_type = models.PositiveSmallIntegerField(choices=) # '1=customer,2=delivery_boy',
    vehicle_type = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.TextField(null=True, blank=True)
    image_type = models.PositiveSmallIntegerField(choices=) # '0=normal,1=fb',
    licence_image_front = models.CharField(max_length=256, null=True, blank=True)
    licence_image_back = models.CharField(max_length=256, null=True, blank=True)
    kyc_image1 = models.CharField(max_length=256, null=True, blank=True)
    kyc_image2 = models.CharField(max_length=256, null=True, blank=True)
    kyc_image3 = models.CharField(max_length=256, null=True, blank=True)
    licence_plate_no = models.CharField(max_length=256, null=True, blank=True)
    hst_no = models.CharField(max_length=256, null=True, blank=True)
    unit_no = models.CharField(max_length=256, null=True, blank=True)
    house_no = models.CharField(max_length=256, null=True, blank=True)
    street_name = models.CharField(max_length=256, null=True, blank=True)
    company_address1 = models.CharField(max_length=256, null=True, blank=True)
    company_address2 = models.CharField(max_length=256, null=True, blank=True)
    company_address3 = models.CharField(max_length=256, null=True, blank=True)
    company_address4 = models.CharField(max_length=256, null=True, blank=True)
    company_address5 = models.CharField(max_length=256, null=True, blank=True)
    company_lat1 = models.CharField(max_length=256, null=True, blank=True)
    company_long1 = models.CharField(max_length=256, null=True, blank=True)
    company_lat2 = models.CharField(max_length=256, null=True, blank=True)
    company_long2 = models.CharField(max_length=256, null=True, blank=True)
    company_lat3 = models.CharField(max_length=256, null=True, blank=True)
    company_long3 = models.CharField(max_length=256, null=True, blank=True)
    company_lat4 = models.CharField(max_length=256, null=True, blank=True)
    company_long4 = models.CharField(max_length=256, null=True, blank=True)
    company_lat5 = models.CharField(max_length=256, null=True, blank=True)
    company_long5 = models.CharField(max_length=256, null=True, blank=True)
    subscription_cost = models.CharField(max_length=256, null=True, blank=True)
    subscription_title = models.CharField(max_length=256, null=True, blank=True)
    street_suf = models.CharField(max_length=256, null=True, blank=True)
    country_name = models.CharField(max_length=256, null=True, blank=True)
    vehicle_no = models.CharField(max_length=256, null=True, blank=True)
    vehicle_reg_no = models.CharField(max_length=256, null=True, blank=True)
    year = models.CharField(max_length=50, null=True, blank=True)
    make = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    company_name = models.CharField(max_length=256, null=True, blank=True)
    abn_no = models.CharField(max_length=256, null=True, blank=True)
    gst = models.CharField(max_length=256, null=True, blank=True)
    gst_no = models.CharField(max_length=256, null=True, blank=True)
    land_line_no = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=100, null=True, blank=True)
    suburb = models.CharField(max_length=100, null=True, blank=True)
    device_type = models.PositiveSmallIntegerField(choices=) # 'ios','android'
    admin_type = models.PositiveSmallIntegerField(choices=) # 'super','normal'
    login_status = models.BooleanFiled() # '"yes=login","no=logout"',
    forget_timestamp = models.CharField(max_length=256, null=True, blank=True)


class Address(BaseModel):
    user = models.ForeignKey(User)
    location = models.PointField(null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    firstname = models.CharField(max_length=256, null=True, blank=True)
    lastname = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=256, null=True, blank=True)
    country_code = models.CharField(max_length=256, null=True, blank=True)
    company_name = models.CharField(max_length=256, null=True, blank=True)
    sender_company_name = models.CharField(max_length=256, null=True, blank=True)
    receiver_company_name = models.CharField(max_length=256, null=True, blank=True)
    sender_contact_number = models.CharField(max_length=256, null=True, blank=True)
    receiver_contact_number = models.CharField(max_length=256, null=True, blank=True)
    sender_name = models.CharField(max_length=256, null=True, blank=True)
    receiver_name = models.CharField(max_length=256, null=True, blank=True)


class Mobile(BaseModel):
    user = models.ForeignKey(user)
    number = models.IntegerFiled()
    verification_code = models.IntegerFiled()
    verified = models.BooleanField(default=False)


class AdminUser(BaseModel):
    user = models.ForeignKey(User)
    email = models.CharField(max_length=256, null=True, blank=True)
    password = models.CharField(max_length=256, null=True, blank=True)
    type = models.PositiveSmallIntegerField(choices=)
    logged_in = models.??
