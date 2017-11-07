from django import forms
from .models import Pressure


class PostForm(forms.ModelForm):

    class Meta:
        model = Pressure
        fields = ('systolic', 'diastolic', 'rate', 'date',)
        # model_w = Weight
        # field_w = ('wght', 'date')
