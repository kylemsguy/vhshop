from django import forms

class GetFaceForm(forms.ModelForm):
    class Meta:
        model = Face
        fields = ()
