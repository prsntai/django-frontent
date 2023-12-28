from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .thread import prsntThread

prsnt_thread = prsntThread()

def index(request):
    if prsnt_thread.started:
        prsnt_thread.stop = True
        prsnt_thread.join()

    return render(request, 'index.html')

def docs(request):
    if prsnt_thread.started:
        prsnt_thread.stop = True
        prsnt_thread.join()

    return render(request, 'docs.html')

def ai(request):
    global prsnt_thread
    
    if prsnt_thread.started:
        prsnt_thread.stop = True
        prsnt_thread.join()
    
    prsnt_thread = prsntThread()
    if request.method == 'POST':
        if 'start_thread' in request.POST:
            if not prsnt_thread.started:
                prsnt_thread.start()
        elif 'stop_thread' in request.POST:
            if prsnt_thread.started:
                prsnt_thread.stop = True
                prsnt_thread.join()

    return render(request, 'ai.html')
