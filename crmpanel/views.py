from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Module
# Create your views here.
from django.http import HttpResponse
from django.template import loader

def home(request):
  modules = Module.objects.all().values()
  context = {
      "modules":modules
  }
  return render(request,"home.html",context)
  # template = loader.get_template('home.html')
  # return HttpResponse(template.render())