from django.db import models

# Create your models here 2.

class data_sensor(models.Model):
      ketinggian_air = models.CharField(max_length=10)
      curah_hujan = models.CharField(max_length=10)
      tanggal_input = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return str(self.tanggal_input)

class data_permenit (models.Model):
      ketinggian_air = models.CharField(max_length=10)
      Curah_hujan = models.CharField(max_length=10)
      tanggal_input = models.DateTimeField(auto_now_add= True)

      def __str__(self):
          return str(self.tanggal_input)

class data_perjam (models.Model):
      ketinggian_air = models.CharField(max_length=10)
      curah_hujan = models.CharField(max_length=10)
      tanggal_input = models.DateTimeField(auto_now_add= True)

      def __str__(self):
          return str(sel.tanggal_input)

class data_perhari (models.Model):
      ketinggian_air = models.CharField(max_length=10)
      curah_hujan = models.CharField(max_length=10)
      tanggal_input = models.DateTimeField(auto_now_add= True)

      def __str__ (self):
          return str(self.tanggal.input)

class daftar_sensor (models.Model):
      nama_sensor = models.CharField(max_length=50)
      deskripsi = models.CharField(max_length=512)
      model_sensor = models.CharField(max_length=50)

      def __str__ (self):
          return str(self.nama_sensor)
