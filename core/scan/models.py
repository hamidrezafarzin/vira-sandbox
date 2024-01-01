from django.db import models
from django.utils.translation import gettext_lazy as _
from validators.fieldvalidators import FieldValidators
import os 
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

# Create your models here.

class Scan(models.Model):
    class ScanStatus(models.TextChoices):
        LFS = "Load from source", _("بارگیری از مبدا")
        DTDS = "Delivery to the distribution system", _("تحویل به سیستم توزیع")
        DTS = "Delivery to the store", _("تحویل به فروشگاه")
    
    class ProductTypeStatus(models.TextChoices):
        ESl = "ESL milk", _("ESL شیر")
        pasteurized = "pasteurized Milk", _("شیر پاستوریزه")
        
    phone = models.CharField(
        _("Phone"),
        max_length=11,
        validators=[
            FieldValidators.iranian_phone_validator,
            FieldValidators.xss_validator,
        ],
        blank=False,
        null=False,
    )
    first_name = models.CharField(max_length=255, validators=[FieldValidators.xss_validator,], blank=False, null=False)
    last_name = models.CharField(max_length=255, validators=[FieldValidators.xss_validator,], blank=False, null=False)
    product_type = models.CharField(max_length=35, choices=ProductTypeStatus.choices)
    scan_part = models.CharField(max_length=35, choices=ScanStatus.choices)
    number_in_box = models.PositiveIntegerField(blank=False, null=False)
    manufacture_date = models.CharField(max_length=255, validators=[FieldValidators.xss_validator,], blank=False, null=False) #models.DateTimeField()
    photo = models.ImageField(upload_to="label", blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-created_date"]
        
    def __str__(self):
        return f"{self.phone}"
    

@receiver(models.signals.post_delete, sender=Scan)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)