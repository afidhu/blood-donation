from django.db import models
from ACCOUNT.models import Users
# Create your models here.

# RIST_FACTOR=[
#     ('CANCER', 'CANCER'),
#     ('HIV', 'HIV'),
#     ('MALARIA', 'MALARIA'),
# ]

BLOOD_TYPE=[
    ('A', 'A'),
    ('B', 'B'),
    ('AB', 'AB'),
    ('o+', 'o+'),
    ('o-', 'o-'),
]

    
class Blood(models.Model):
    user=models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    blood_type=models.CharField(max_length=100, choices=BLOOD_TYPE)
    quantity=models.IntegerField()
    image=models.ImageField(upload_to='image/', blank=True, null=True)
    start_date=models.DateField(auto_now_add=True)
    exp_date=models.DateField(auto_now_add=False, default='00/00/00', null=True, blank=True)
    
    
    def __str__(self):
        return self.blood_type

class Hospital(models.Model):
    blood = models.ManyToManyField(Blood)  # Multiple Blood types can be associated
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=False)
    exp_date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f"Hospital with {self.blood.count()} blood types"



    
class Recipient(models.Model):
    recipient_name=models.ForeignKey(Users,  on_delete=models.SET_NULL, null=True)
    quantity=models.IntegerField()
    blood_type=models.ForeignKey(Hospital, on_delete=models.CASCADE)
    location=models.CharField(max_length=20, blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)
    is_complete=models.BooleanField(default=False)
    
    def __str__(self):
        return self.recipient_name.username
