from django import forms

class FaceUpload(forms.Form):
	file = forms.FileField

class FaceForm(forms.ModelForm):
    class Meta:
        model = Face
