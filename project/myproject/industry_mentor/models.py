from django.db import models

# Create your models here.

class IndustryMentor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    job_role = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    expertise = models.TextField()
    pan_number = models.CharField(max_length=10, unique=True)
    bank_account = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=255)
    ifsc = models.CharField(max_length=11)
    linkedin = models.URLField(blank=True, null=True)
    passbook_image = models.ImageField(upload_to='passbooks/')
    pan_card_image = models.ImageField(upload_to='pan_cards/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

