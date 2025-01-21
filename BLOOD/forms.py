from django import forms
from.models import Recipient, Blood, Hospital
from bootstrap_datepicker_plus.widgets import DatePickerInput

# class DonorForm(forms.ModelForm):
#     class Meta:
#         model=Donor
#         exclude=('donor_name',)
#         fields='__all__'
#         # widgets={
#         #     "recipient_name":forms.TextInput(attrs={"class":"form-control mt-2", "id":"name"}),
#         #     "quantity":forms.NumberInput(attrs={"class":"form-control mt-2", "id":"name"}),
#         #     "blood_type":forms.TextInput(attrs={"class":"form-control mt-2", "id":"name"}),
#         #     "rist_factor":forms.TextInput(attrs={"class":"form-control mt-2", "id":"name"}),
#         #     }
        
#     def __init__(self, *args, **kwargs):
#         super(DonorForm, self).__init__(*args, **kwargs)    
#         for field in self.fields.values():
#             field.widget.attrs['class']='form-control'
            
            
            
            
class RecipientForm(forms.ModelForm):
    class Meta:
        model=Recipient
        exclude=('is_complete',)
        fields='__all__'
        widgets = {
            'date':DatePickerInput(),
        }
        # widgets={
        #     "quantity":forms.NumberInput(attrs={"class":"form-control mt-2", "id":"name"}),
        #     "blood_type":forms.TextInput(attrs={"class":"form-control mt-2", "id":"name"}),
        #     "location":forms.TextInput(attrs={"class":"form-control mt-2", "id":"name"}),
        #     "date":forms.DateTimeInput(attrs={"class":"form-control mt-2", "id":"name"}),
        #     }
        
        
    def __init__(self, *args, **kwargs):
        super(RecipientForm, self).__init__(*args, **kwargs)    
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'


class BloodForm(forms.ModelForm):
    class Meta:
        exclude=('image',)
        model = Blood
        fields = "__all__"
        widgets = {
            'exp_date': DatePickerInput(),  # Assuming DatePickerInput is defined correctly
        }
        
    def __init__(self, *args, **kwargs):
        super(BloodForm, self).__init__(*args, **kwargs)
        
        # Remove help_text for all fields
        for field in self.fields.values():
            field.help_text = None
        
        # Add 'form-control' class to all fields
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            
class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(HospitalForm, self).__init__(*args, **kwargs)

        # Remove help_text for all fields
        for field in self.fields.values():
            field.help_text = None  # Or use "" if you want an empty string instead

        # Add 'form-control' class to all fields
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
