from django.db import models


class Setting(BaseModel):
    m_2hour = models.CharField(max_length=256, null=True, blank=True)
    m_4hour = models.CharField(max_length=256, null=True, blank=True)
    m_sameday = models.CharField(max_length=256, null=True, blank=True)
    c_2hour = models.CharField(max_length=256, null=True, blank=True)
    c_4hour = models.CharField(max_length=256, null=True, blank=True)
    c_sameday = models.CharField(max_length=256, null=True, blank=True)
    v_2hour = models.CharField(max_length=256, null=True, blank=True)
    v_4hour = models.CharField(max_length=256, null=True, blank=True)
    v_sameday = models.CharField(max_length=256, null=True, blank=True)
    t_2hour = models.CharField(max_length=256, null=True, blank=True)
    t_4hour = models.CharField(max_length=256, null=True, blank=True)
    t_sameday = models.CharField(max_length=256, null=True, blank=True)
    driver_percentage = models.CharField(max_length=256, null=True, blank=True)
    endtime_4hour = models.CharField(max_length=256, null=True, blank=True)
    endtime_sameday = models.CharField(max_length=256, null=True, blank=True)
    m_p_height = models.CharField(max_length=256, null=True, blank=True)
    m_p_length = models.CharField(max_length=256, null=True, blank=True)
    m_p_width = models.CharField(max_length=256, null=True, blank=True)
    m_p_weight = models.CharField(max_length=256, null=True, blank=True)
    c_p_height = models.CharField(max_length=256, null=True, blank=True)
    c_p_length = models.CharField(max_length=256, null=True, blank=True)
    c_p_width = models.CharField(max_length=256, null=True, blank=True)
    c_p_weight = models.CharField(max_length=256, null=True, blank=True)
    v_p_height = models.CharField(max_length=256, null=True, blank=True)
    v_p_length = models.CharField(max_length=256, null=True, blank=True)
    v_p_width = models.CharField(max_length=256, null=True, blank=True)
    v_p_weight = models.CharField(max_length=256, null=True, blank=True)
    t_p_height = models.CharField(max_length=256, null=True, blank=True)
    t_p_length = models.CharField(max_length=256, null=True, blank=True)
    t_p_width = models.CharField(max_length=256, null=True, blank=True)
    t_p_weight = models.CharField(max_length=256, null=True, blank=True)
    p_d_min_charge = models.CharField(max_length=256, null=True, blank=True)


class StandardParcel(BaseModel):
    height = models.CharField(max_length=256, null=True, blank=True)
    width = models.CharField(max_length=256, null=True, blank=True)
    length = models.CharField(max_length=256, null=True, blank=True)
    weight = models.CharField(max_length=256, null=True, blank=True)
    cost = models.CharField(max_length=256, null=True, blank=True)


class Subscription(BaseModel):
    details = models.CharField(max_length=256, null=True, blank=True)
    cost = models.CharField(max_length=256, null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)


class Card(BaseModel):
    user = models.ForeignKey(User)
    card_holder_name = models.CharField(max_length=100, null=True, blank=True)
    card_number = models.CharField(max_length=100, null=True, blank=True)
    expiry_month = models.CharField(max_length=50, null=True, blank=True)
    expiry_year = models.CharField(max_length=50, null=True, blank=True)
    status = models.BooleanField(default=False) # '0=''inactive'',1=''active'''


class Color(BaseModel):
    code = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)


class Faq(BaseModel):
    description = models.TextField()


class MinimumCharge(BaseModel):
    motorbike = models.CharField(max_length=256, null=True, blank=True)
    driver_distance = models.IntegerField(default=0)
    car = models.CharField(max_length=256, null=True, blank=True)
    van = models.CharField(max_length=256, null=True, blank=True)
    truck = models.CharField(max_length=256, null=True, blank=True)
    currency = models.CharField(max_length=256, null=True, blank=True)
    driver_percentage = models.IntegerField(default=0)
    standard_price1 = models.CharField(max_length=256, null=True, blank=True)
    standard_price2 = models.CharField(max_length=256, null=True, blank=True)
    standard_price3 = models.CharField(max_length=256, null=True, blank=True)
    plus_price1 = models.CharField(max_length=256, null=True, blank=True)
    plus_price2 = models.CharField(max_length=256, null=True, blank=True)
    plus_price3 = models.CharField(max_length=256, null=True, blank=True)
    premium1 = models.CharField(max_length=256, null=True, blank=True)
    premium2 = models.CharField(max_length=256, null=True, blank=True)
    premium3 = models.CharField(max_length=256, null=True, blank=True)



class DriverReport(BaseModel):
    order = models.ForeignKey(Order)
    driver = models.ForeignKey(Driver)
    comment = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)


class Notification(BaseModel):
    order = models.ForeignKey(Order)
    from_user = models.ForeignKey(user)
    to_user = models.ForeignKey(user)
    message = models.TextField()
    type = models.CharField(max_length=100, null=True, blank=True)


class Review(BaseModel):
    customer = models.ForeignKey(User)
    driver = models.ForeignKey(Driver)
    order = models.ForeignKey(Order)
    message = models.TextField(null=True, blank=True)
    driverRatting = models.CharField(max_length=256, null=True, blank=True)
    feedback = models.CharField(max_length=256, null=True, blank=True)
    serviceRatting = models.CharField(max_length=256, null=True, blank=True)


class StartEmail(BaseModel):
    name = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    contact = models.CharField(max_length=256, null=True, blank=True)
    project = models.CharField(max_length=256, null=True, blank=True)
    transport = models.CharField(max_length=256, null=True, blank=True)


class VehicleModel(BaseModel):
    make = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerFiled(default=0)
