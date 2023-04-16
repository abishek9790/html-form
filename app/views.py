from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST.get('tn')
        to=topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        return HttpResponse("insert_topic inserted succcessfully")
    return render(request, 'insert_topic.html')

def insert_webpage(request):
    tom=topic.objects.all()
    d={'topics':tom}
    if request.method=='POST':
        tn=request.POST.get('tn')
        name=request.POST.get('name')
        url=request.POST.get('url')
        email=request.POST.get('email')
        ta=topic.objects.get(topic_name=tn)
        wo=webpage.objects.get_or_create(topic_name=ta,name=name,url=url,email=email)[0]
        wo.save()
        return HttpResponse("inserted webpage is successfully")
    return render(request, 'insert_webpage.html',d)
        
def insert_accessrecords(request):
    wpo=webpage.objects.all()
    d={'webpages':wpo}
    if request.method=='POST':
        name=request.POST.get('name')
        date=request.POST.get('date')
        ac=webpage.objects.get(name=name)
        aco=accessrecords.objects.get_or_create(name=ac,date=date)[0]
        aco.save()
        return HttpResponse("inserted accessrecords is successfully")
    return render(request, 'insert_accessrecords.html',d)




def retrive_data(request):
    do=topic.objects.all()
    d={'displays':do}
    if request.method=='POST':
        tn=request.POST.getlist('tn')
        print(tn)
        webqueryset=webpage.objects.none()
        for x in tn:
            webqueryset=webqueryset|webpage.objects.filter(topic_name=x)
        d1={'web':webqueryset}
        return render(request, 'display_topic.html',d1)

    return render(request, 'retrive_data.html',d)

def checkbox(request):
    co=topic.objects.all()
    d={'top':co}
    return render(request, 'checkbox.html',d)


def radio(request):
    ro=topic.objects.all()
    d={'ra':ro}
    return render(request, 'radio.html',d)