from django.forms import ModelForm
from .models import Aliments

class AddAlimentForm(ModelForm):
    class Meta:
        model = Aliments
        fields = ["Nom", "Prix_par_aliment", "Quantite_dans_le_stock", "Quantite_vendus"]
        
class UpdateAlimentForm(ModelForm):
    class Meta:
        model = Aliments
        fields = ["Nom", "Prix_par_aliment", "Quantite_dans_le_stock", "Quantite_vendus"]