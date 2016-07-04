from django import forms
from musicplayer.models import Tracks,Genre_id
from dal import autocomplete 

class Add_genre_form(forms.Form):
    Genre_name = forms.CharField(label='Genre', max_length=100)

class Add_track_form(forms.ModelForm):
	Genre=forms.ModelChoiceField(queryset=Genre_id.objects.all())
	class Meta:
		model=Tracks
		fields=['Track_name','Track_title','Rating','Track',]

class Search_track_form(forms.Form):
	Search_track=forms.ModelChoiceField(queryset=Tracks.objects.all(),widget=autocomplete.ModelSelect2(url='auto-complete'))

class Search_genre_form(forms.Form):
	Search_genre=forms.ModelChoiceField(queryset=Genre_id.objects.all(),widget=autocomplete.ModelSelect2(url='auto-complete-genre'))
