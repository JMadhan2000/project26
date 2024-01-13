from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_Topic(request):
    ELTO=TopicForm()
    d={'ELTO':ELTO}
    if request.method=='POST':
        TLDO=TopicForm(request.POST)
        if TLDO.is_valid():
            tn=TLDO.cleaned_data['Topic_name']
            TO=Topic.objects.get_or_create(Topic_name=tn)[0]
            TO.save()
            return HttpResponse('Table created')
        return HttpResponse('Table not created')
    return render(request,'insert_Topic.html',d)

def insert_WebPage(request):
    ELWO=WebPageForm()
    d={'ELWO':ELWO}
    if request.method=='POST':
        WLDO=WebPageForm(request.POST)
        if WLDO.is_valid():
            t=WLDO.cleaned_data['Topic_name']
            TO=Topic.objects.get(Topic_name=t)
            n=WLDO.cleaned_data['Name']
            u=WLDO.cleaned_data['Url']
            e=WLDO.cleaned_data['Email']
            WO=WebPage.objects.get_or_create(Topic_name=TO,Name=n,Url=u,Email=e)[0]
            WO.save()
            return HttpResponse('WebPage created')
        return HttpResponse('WebPage not created')
    return render(request,'insert_WebPage.html',d)

def insert_AccessRecord(request):
    ELAO=AccessRecordForm()
    d={'ELAO':ELAO}
    if request.method=='POST':
        ALDO=AccessRecordForm(request.POST)
        if ALDO.is_valid():
            n=ALDO.cleaned_data['Name']
            A=WebPage.objects.get(Name=n)
            a=ALDO.cleaned_data['Author']
            d=ALDO.cleaned_data['Date']
            AO=AccessRecord.objects.get_or_create(Name=A,Author=a,Date=d)[0]
            AO.save()
            return HttpResponse('AccessRecord is created')
        return HttpResponse('AccessRecord is not created')
    return render(request,'insert_AccessRecord.html',d)
