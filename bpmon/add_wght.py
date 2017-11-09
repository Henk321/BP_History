from django import forms

from .models import Weight


class PostWght(forms.ModelForm):

    class Meta:
        model = Weight
        fields = ('wght', 'date',)
