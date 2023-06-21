from django.db import models

class about (models.Model):
  id  = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=500)
  Death_Of_Birth = models.CharField(max_length=500)
  phone = models.CharField(max_length=20)
  Description = models.CharField(max_length=500)

  class education (models.Model):
    id  = models.AutoField(primary_key=True)
    DEPERTMENT = models.CharField(max_length=500)
    DEGREE = models.CharField(max_length=500)
    RESULT = models.CharField(max_length=20)
    INSTETUDE = models.CharField(max_length=500)
    STATUS = models.CharField(max_length=500)