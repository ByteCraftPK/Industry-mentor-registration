from django.contrib import admin

# Register your models here.

from .models import IndustryMentor

@admin.register(IndustryMentor)
class IndustryMentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'job_role', 'organization', 'expertise','pan_number','bank_account','bank_name','ifsc','linkedin','passbook_image','pan_card_image','created_at')

