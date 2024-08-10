from django.shortcuts import render , get_object_or_404 , redirect
from .models import Aliments 
from django.contrib.auth.decorators import login_required
from .forms import AddAlimentForm , UpdateAlimentForm
from django.contrib import messages



@login_required
def aliment_list(request): 
    aliments=Aliments.objects.all() #recuperation des donnees
    context={
        'title':'Liste des aliments',
        'aliments': aliments, #La liste de tous les objets Aliments récupérés précédemment à partir de la base de données.
    }
    return render(request , 'restaurantmanagement/aliment_list.html',context=context)  #générer une réponse HTTP qui renvoie le contenu HTML basé sur le template

@login_required
def per_product_view(request, pk): #récupére un objet specifique de Aliments correspondant à la clé primaire (pk) spécifiée dans la requête
    aliment=get_object_or_404(Aliments , pk=pk)
    context={
        'aliment':aliment
    }
    return render(request , 'restaurantmanagement/per_product.html', context=context)

@login_required
def add_aliment(request):
    if request.method == "POST": #verification de la methode de la requete : POST= formulaire doit etre traite pour ajouter un aliment , GET= accede a la page pour la premiere fois
        add_form = AddAlimentForm(data=request.POST)
        if add_form.is_valid():
            new_aliment = add_form.save(commit=False) #pas encore enregistré en base de données 
            new_aliment.save()
            messages.success(request,'Successfully Added Aliment')
            return redirect("/aliments/")
    else:
        add_form = AddAlimentForm()

    return render(request, "restaurantmanagement/aliment_add.html", {'form' : add_form})

@login_required()
def delete_aliment(request, pk):
    aliment = get_object_or_404(Aliments, pk=pk)
    aliment.delete()
    
    return redirect("/aliments/")

@login_required()
def update_aliment(request, pk):
    aliment = get_object_or_404(Aliments, pk=pk)
    if request.method == "POST":
        updateForm = UpdateAlimentForm(data=request.POST)
        if updateForm.is_valid():
            aliment.Nom = updateForm.data['Nom']
            aliment.Quantite_dans_le_stock = updateForm.data['Quantite_dans_le_stock']
            aliment.Quantite_vendus = updateForm.data['Quantite_vendus']
            aliment.Prix_par_aliment = updateForm.data['Prix_par_aliment']
            aliment.save()
            messages.success(request, 'Aliment Updated')#Le formulaire est pré-rempli avec les détails de l'aliment existant (instance=aliment)
            return redirect(f"/aliments/per_product/{pk}")
    else:
        updateForm = UpdateAlimentForm(instance=aliment)
    context={'form' : updateForm}
    return render(request, "restaurantmanagement/aliment_update.html", context=context)

