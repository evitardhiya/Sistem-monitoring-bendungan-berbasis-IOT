from django.shortcuts import render
from django.http import StreamingHttpResponse
from TA_app.models import *
from TA_app import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time
import datetime
import mysql.connector

# Create your views here.

def Dashboard(request):
    return render(request, 'Dashboard.html')

def stream(request):
    def event_stream():
        db = mysql.connector.connect(user = 'xxxxx',password = 'xxxx!',database = 'xxxxx',host = 'xxxxxx',port = 3306)
        cursor = db.cursor()
        while True:
            dat = data_sensor.objects.latest('id')
            data = [dat.ketinggian_air,
            dat.curah_hujan,dat.tanggal_input]
            kirim = ''
            for i in data:
                kirim += str(i) + ","
            time.sleep(1)
            yield 'data: %s\n\n' %kirim
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')

def jenis_sensor(request):
    return render(request, 'jenis_sensor.html')

def grafik_data(request):
    tanggal_awal = request.GET.get('awal')
    tanggal_akhir = request.GET.get('akhir')
    data = models.data_perjam.objects.filter(tanggal_input__range=[tanggal_awal,tanggal_akhir])
    tanggal = []
    hujan = []
    air = []
    for i in data:
        tanggal.append(i.tanggal_input)
        hujan.append(i.curah_hujan)
        air.append(i.ketinggian_air)
    return render(request, 'grafik_data.html',{'tanggal':tanggal,'hujan':hujan,'air':air})

def tabel_data(request):
    tanggal_awal = request.GET.get('awal')
    tanggal_akhir = request.GET.get('akhir')
    data = models.data_perjam.objects.filter(tanggal_input__range=[tanggal_awal,tanggal_akhir])
    return render(request, 'tabel_data.html',{'datas':data})

