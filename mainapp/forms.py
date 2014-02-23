from django import forms

class FaceForm(forms.ModelForm):
    class Meta:
        model = Face
