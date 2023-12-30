from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import speech_recognition as sr
import json

r = sr.Recognizer()
running = False
spoken_text = ''

def listen():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            return str(text)
    except:
        return ''

def index(request):
    return render(request, 'index.html')

def docs(request):
    return render(request, 'docs.html')

@csrf_exempt
def transcribe(request):
    global running, spoken_text
    
    data = json.loads(request.body.decode('utf-8'))
    switch_active = data.get('switchActive', False)

    if switch_active:
        if not running:
            running = True
            spoken_text = listen().capitalize() + '.'
            running = False
    else:
        running = False
        spoken_text = ''

    response_data = {'status': 'success', 'transcription': spoken_text}
    return JsonResponse(response_data)

def ai(request):
    return render(request, 'ai.html')
