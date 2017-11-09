from django import forms
from .models import Pressure


class PostBP(forms.ModelForm):

    class Meta:
        model = Pressure
        fields = ('systolic', 'diastolic', 'rate', 'date',)
