from django import forms

from .models import Fichier

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(
        label="Sélectionnez un fichier CSV",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )



class FichierForm(forms.ModelForm):
    class Meta:
        model = Fichier
        fields = ['nom', 'fichier']

