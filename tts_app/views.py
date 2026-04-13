
from django.shortcuts import render
from gtts import gTTS
import os
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def speak(request):
    text = request.POST.get('text')
    if text:
        tts = gTTS(text=text, lang='en')
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        path = os.path.join(settings.MEDIA_ROOT, 'speech.mp3')
        tts.save(path)
        return render(request, 'index.html', {'audio': settings.MEDIA_URL + 'speech.mp3'})
    return render(request, 'index.html')
