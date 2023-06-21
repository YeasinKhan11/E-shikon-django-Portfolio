from django.http import HttpResponse
from django.shortcuts import render

from . import models

# def index(request):
#   return HttpResponse(' Hello Evan ')

def index(request):
  return render(request,'myfile.html')

def about(request):
  return render(request,'Admin/about.html')

def store(request):
  Name = request.POST.get('name')
  Death_Of_Birth = request.POST.get('Death Of Birth')
  phone = request.POST.get('number')
  Description = request.POST.get('Description')
  info = [Name,Death_Of_Birth,phone,Description]

  about = models.about()
  about.Name = Name
  about.Death_Of_Birth = Death_Of_Birth
  about.phone = phone
  about.Description = Description
  about.save()

  return HttpResponse(info)
  # return render(request,'myfile.html')