from django import forms
from .models import IndustryMentor

class IndustryMentorForm(forms.ModelForm):
    class Meta:
        model = IndustryMentor
        fields = '__all__'
