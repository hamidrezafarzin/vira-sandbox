from django import forms
from .models import Scan

class ScanForm(forms.ModelForm):
    class Meta:
        model = Scan
        fields = ["phone", "first_name", "last_name", "product_type", "scan_part", "number_in_box", "manufacture_date", "photo"]