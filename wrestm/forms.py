from django.db import models
from django.forms import fields
from wrestm.models import Student
from django import forms

class StudentForm(forms.ModelForm):
    def clean_marks(self):
        inputmarks = self.cleaned_data['marks']
        if inputmarks<50:
            raise forms.ValidationError('marks should be >= 35')
        return inputmarks
    class Meta:
        model =Student
        fields = '__all__'

