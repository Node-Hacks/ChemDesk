# forms.py
from django import forms
from structures.models import *

class structuresform(forms.ModelForm):

	class Meta:
		model = structures1
		fields = ['name', 'hotel_Main_Img']
