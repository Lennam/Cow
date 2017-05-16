from django.shortcuts import render
from models import Fodder, Reslut, Vol
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse,render_to_response
from datetime import datetime
import json


# Create your views here.


def home(request):
    return render(request, 'home.html')


def news(request):
    return render(request, 'news.html')


def cal(request):
    return render(request, 'cal.html')


def fodder(request):
    if request.method == "POST":
        date = request.POST['date']
        tdnfc = request.POST['tdnfc']
        tdcpf = request.POST['tdcpf']
        tdcpc = request.POST['tdcpc']
        tdfa = request.POST['tdfa']
        tdndf = request.POST['tdndf']
        tdn = request.POST['tdn']
        dex = request.POST['de1x']
        mep = request.POST['mep']
        nelp = request.POST['nelp']
        nameone = request.POST['nameOne']
        nametwo = request.POST['nameTwo']
        namethree = request.POST['nameThree']
        namefour = request.POST['nameFour']
        namefive = request.POST['nameFive']
        volone = request.POST['volone']
        voltwo = request.POST['voltwo']
        volthree = request.POST['volthree']
        volfour = request.POST['volfour']
        volfive = request.POST['volfive']
        Fodder.objects.create(date=date, nameOne=nameone, nameTwo=nametwo, nameThree=namethree, nameFour=namefour, nameFive=namefive)
        Reslut.objects.create(date=date, tdnfc=tdnfc, tdcpf=tdcpf, tdcpc=tdcpc, tdfa=tdfa, tdndf=tdndf, tdn=tdn, de1x=dex, mep=mep, nelp=nelp)
        Vol.objects.create(date=date, volOne=volone, volTwo=voltwo, volThree=volthree, volFour=volfour, volFive=volfive)
    return render(request, 'fodder.html')


def dataIn(request):
    return render(request, 'dataIn.html')


def dataOut(request):
    return render(request, 'dataOut.html')


def info(request):
    names = Fodder.objects.all()
    results = Reslut.objects.all()
    vols = Vol.objects.all()
    content1 = []
    tdnfc = []
    tdcpf = []
    tdcpc = []
    tdfa = []
    tdndf = []
    tdn = []
    nelp = []
    date = []
    de1x = []
    mep = []
    for re in results:
        tdnfc.append(re.tdnfc)
        tdcpf.append(re.tdcpf)
        tdcpc.append(re.tdcpc)
        tdfa.append(re.tdfa)
        tdndf.append(re.tdndf)
        tdn.append(re.tdn)
        nelp.append(re.nelp)
        de1x.append(re.de1x)
        mep.append(re.mep)
        date.append(re.date.strftime("%Y-%m-%d"))
    Tdnfc = json.dumps(tdnfc)
    Tdcpf = json.dumps(tdcpf)
    Tdcpc = json.dumps(tdcpc)
    Tdfa = json.dumps(tdfa)
    Tdndf = json.dumps(tdndf)
    Tdn = json.dumps(tdn)
    Nelp = json.dumps(nelp)
    Dat = json.dumps(date)
    De1x = json.dumps(de1x)
    Mep = json.dumps(mep)
    print Dat
    for name, vol in zip(names, vols):
        s = {}
        s['id'] = name.id
        s['date1'] = name.date
        s['nameOne'] = name.nameOne
        s['nameTwo'] = name.nameTwo
        s['nameThree'] = name.nameThree
        s['nameFour'] = name.nameFour
        s['nameFive'] = name.nameFive
        s['date2'] = vol.date
        s['volOne'] = vol.volOne
        s['volTwo'] = vol.volTwo
        s['volThree'] = vol.volThree
        s['volFour'] = vol.volFour
        s['volFive'] = vol.volFive
        content1.append(s)
    # for vol in vols:
    #     w = {}
    #     w['volOne'] = vol.volOne
    #     w['volTwo'] = vol.volTwo
    #     w['volThree'] = vol.volThree
    #     w['volFour'] = vol.volFour
    #     w['volFive'] = vol.volFive
    #     content1.append(w)
    return render_to_response('info.html', locals())


def dmi(request):
    return render(request, 'dmi.html')


def fcm(request):
    return render(request, 'fcm.html')


def de1x(request):
    return render(request, 'de1x.html')


def tdn(request):
    return render(request, 'tdn.html')


def tdnpre(request):
    return render(request, 'tdnpre.html')


def ne(request):
    return render(request, 'ne.html')


def nfc(request):
    return render(request, 'nfc.html')
