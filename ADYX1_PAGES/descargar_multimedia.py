from pytube import YouTube

def descargar_video(url, ruta):
    video = YouTube(url).streams.get_highest_resolution()
    video.download(ruta)

def descargar_audio(url, ruta):
    audio = YouTube(url).streams.filter(only_audio=True).first()
    audio.download(ruta)