from django.db import models

class Aliments(models.Model):
    Nom=models.CharField(max_length=100,null=False,blank=False)
    Prix_par_aliment=models.DecimalField(max_digits=19,decimal_places=2,null=False,blank=False)
    Quantite_dans_le_stock=models.IntegerField(null=False,blank=False)
    Quantite_vendus=models.IntegerField(null=False,blank=False)
    Date_du_stock=models.DateField(auto_now_add=True)
    Derniere_date_de_vente=models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.Nom

# Create your models here.
