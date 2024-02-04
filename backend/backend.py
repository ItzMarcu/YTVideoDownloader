from flask import Flask, request, jsonify, render_template
from pytube import YouTube

app = Flask(__name__)

@app.route('/static_web/index.html')
def index():
    return render_template('static_web\index.html')

@app.route('/download', methods = ['POST'])
def downloadVideo():
    try: 
        data = request.get_json()
        videoUrl = data["link-text"]

        yt = YouTube(videoUrl)
        video = yt.streams.get_highest_resolution()
        video.download('downloads')

        return jsonify({'succes': True, 'message': 'Download completato'})
    
    except Exception as e: 
        return jsonify({'succes': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug = True)