from django.forms import ModelForm
from csms.models import Inmate

class InmateForm(ModelForm):
    class Meta:
        model = Inmate
        fields = ['first_name', 'last_name', 'date_of_birth', 'inmate_id', 'facility', 'gender', 'admission_date', 'release_date']


# class CorrectionalOfficerForm(ModelForm):
#     class Meta:
#         model = CorrectionalOfficer
#         fields = ['first_name', 'last_name', 'badge_number', 'rank', 'hire_date']