from django.shortcuts import render, redirect, HttpResponse
from gtts import gTTS
import string
import random
import os
import shutil
import PyPDF2


def index(request):
    return render(request,'TextsAudio/index.html')

def result(request):
    if request.method == "POST":
        letters = string.ascii_lowercase

        file_name = f"{''.join(random.choice(letters) for i in range(10))}.mp3"

        text = request.POST['text']
        lang = request.POST['lang']

        tts = gTTS(text,lang=lang)
        tts.save(file_name)

        dir = os.getcwd()
        full_dir = os.path.join(dir, file_name)

        dest = shutil.move(full_dir, os.path.join(dir, "TextsAudio\static\TextsAudio"))

        data = {"loc" :file_name}
        return render(request,'TextsAudio/Result.html',data)

