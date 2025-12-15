# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Order(models.Model):

    #__Order_FIELDS__
    order_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    order_number = models.CharField(max_length=255, null=True, blank=True)
    order_total = models.IntegerField(null=True, blank=True)
    order_status = models.CharField(max_length=255, null=True, blank=True)
    customer_id = models.IntegerField(null=True, blank=True)

    #__Order_FIELDS__END

    class Meta:
        verbose_name        = _("Order")
        verbose_name_plural = _("Order")


class Orderitem(models.Model):

    #__Orderitem_FIELDS__
    item_name = models.CharField(max_length=255, null=True, blank=True)
    item_url = models.CharField(max_length=255, null=True, blank=True)
    item_description = models.CharField(max_length=255, null=True, blank=True)
    item_quantity = models.IntegerField(null=True, blank=True)
    item_price = models.IntegerField(null=True, blank=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

    #__Orderitem_FIELDS__END

    class Meta:
        verbose_name        = _("Orderitem")
        verbose_name_plural = _("Orderitem")



#__MODELS__END
