from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse


# Create your views here.
def recipes(request):
    if request.method=="POST":

        resi_name=request.POST.get('resi_name')
        res_discription=request.POST.get('res_discription')
        res_image = request.FILES.get('res_image')

        Res.objects.create(
            res_name=resi_name,
            res_description=res_discription,
            res_image = res_image,
            )
        return redirect('/recipes/')
       
    queryset = Res.objects.all()

    if request.GET.get('search'):
        queryset=queryset.filter(res_name__icontains = request.GET.get('search'))

    context = {'recipes':queryset}

    return render(request,'recipes.html',context)

def update_recipe(request,id):

    queryset = Res.objects.get(id=id)
    if request.method=="POST":

        resi_name=request.POST.get('resi_name')
        res_discription=request.POST.get('res_discription')
        res_image = request.FILES.get('res_image')
    
        queryset.res_name=resi_name
        queryset.res_description=res_discription
        
        if res_image:
            queryset.res_image=res_image

        queryset.save()
        return redirect('/recipes/')
        
        
        

    context = {'recipe':queryset}

    return render(request,'update_recipes.html',context)

def delete_recipe(request,id):
    queryset = Res.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')