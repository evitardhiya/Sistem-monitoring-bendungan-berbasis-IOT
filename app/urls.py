from django.urls import path
from TA_app import views

app_name = 'TA_app'

urlpatterns = [
    path('', views.Dashboard, name='Dashboard'),
    path('home', views.Dashboard, name='Dashboard'),
    path('home/stream', views.stream, name='stream'),
    path('jenis_sensor/', views.jenis_sensor, name='Jenis Sensor'),
    path('grafik_data/', views.grafik_data, name='Grafik Data'),
    path('tabel_data/', views.tabel_data, name='Tabel Data'),
]

