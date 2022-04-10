from django.shortcuts import render

def inicio(request):
  return render(request, "indice/index.html", {})

def about(request):
  return render(request, "indice/about.html", {})