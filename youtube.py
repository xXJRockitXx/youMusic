#!/usr/bin/python3
from __future__ import unicode_literals
import youtube_dl
import os
from yt_dlp import YoutubeDL



class MyLogger(object):

    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Descarga completa, convirtiendo ...') 


ydl_opts = {
    'format': 'bestaudio/best',
    'writethumbnail': True,
    'addmetadata':True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }, {
        'key': 'EmbedThumbnail',
    }, {
        'key': 'FFmpegMetadata',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

url = input("Link: ")

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

nombres = os.listdir()      

print("\nRenombrando archivos ...")

for nombre in nombres:
    """ Eliminamos todos los caracteres que salen despues
    del guion mediano en el nombre de los archivos """
    if(nombre.endswith(".mp3")):
        tope = nombre.find("[")
        nuevoNombre = nombre[0:tope]
        os.rename(nombre, nuevoNombre + ".mp3")