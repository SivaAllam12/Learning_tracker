from django import forms
from .models import Course
from .models import Entry

class Courseform(forms.ModelForm):
    class Meta:
        model=Course
        fields=['course_name']
        labels={'course_name':'Course Name'}

class Entryform(forms.ModelForm):
    class Meta:
        model=Entry
        fields=['course_id','Date','Hours_spent','status']
