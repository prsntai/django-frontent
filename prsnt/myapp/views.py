from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import speech_recognition as sr
import json

def index(request):
    return render(request, 'index.html')

def docs(request):
    return render(request, 'docs.html')

def transcribe(request):
    data = json.loads(request.body.decode('utf-8'))
    switch_active = data.get('switchActive', False)

    if switch_active:
        response_data = {'status': 'success', 'transcription': 'on'}
    else:
        response_data = {'status': 'success', 'transcription': 'off'}

    return JsonResponse(response_data)

def ai(request):
    return render(request, 'ai.html')
