from flask import Flask, render_template, request, redirect
from descargar_multimedia import descargar_video, descargar_audio
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        tipo = request.form.get('tipo')
        ruta = request.form.get('ruta')
        if tipo == 'video':
            descargar_video(url, ruta)
        elif tipo == 'audio':
            descargar_audio(url, ruta)
        return redirect(request.url)
    return render_template('descargador_youtube.html')

if __name__ == '__main__':
    app.run(debug=True)