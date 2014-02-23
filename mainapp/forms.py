from django import forms
from mainapp.models import Face

class FaceForm(forms.ModelForm):
    class Meta:
        model = Face
        fields = ['image']

class FaceDataForm(forms.ModelForm):
	class Meta:
		model = Face
		fields = ['left_side_x', 'left_side_y',
					'right_side_x', 'right_side_y',
					'left_corner_x', 'left_corner_y',
					'right_corner_x', 'right_corner_y']
