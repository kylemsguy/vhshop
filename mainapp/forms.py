from django import forms
from mainapp.models import Face

class GetFaceForm(forms.ModelForm):
    class Meta:
        model = Face
        fields = ()
