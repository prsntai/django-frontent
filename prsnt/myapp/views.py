from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def docs(request):
    return render(request, 'docs.html')

def ai(request):
    return render(request, 'ai.html')