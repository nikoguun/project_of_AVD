from django.db import models
from django.core.exceptions import ValidationError

def validate_file_type(value):
    if not value.name.endswith('.csv'):
        raise ValidationError('Seuls les fichiers CSV sont autorisés.')

class Fichier(models.Model):
    nom = models.CharField(max_length=255)
    fichier = models.FileField(upload_to='uploads/', validators=[validate_file_type])
    date_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
