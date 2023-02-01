from django.shortcuts import render
from app.forms import *
# Create your views here.


def django_form(request):
    form=Employee()
    d={'form':form}
    if request.method=='POST':
        data=Employee(request.POST)
        if data.is_valid():
            name=data.cleaned_data['name']
            number=data.cleaned_data['number']
            email=data.cleaned_data['email']
            add=data.cleaned_data['address']
            gen=data.cleaned_data['gender']
            lan=data.cleaned_data['language']
            d1={'name':name,'number':number,'email':email,'address':add,'gender':gen,'language':lan}
            return render(request,'display.html',d1)
    return render(request,'django_form.html',d)