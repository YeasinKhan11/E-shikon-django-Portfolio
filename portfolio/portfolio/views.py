from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#   return HttpResponse(' Hello Evan ')

def index(request):
  return render(request,'myfile.html')