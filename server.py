from os import path, listdir
import os
from flask import Flask, redirect, render_template, request, send_from_directory
import flask


def get_local_ip():
    from socket import socket, AF_INET, SOCK_DGRAM
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    return s.getsockname()[0]


PORT = 5000
HOST = get_local_ip()

app = Flask(__name__)


@app.route('/', defaults={"user_path": ""})
@app.route('/<path:user_path>')
def home(user_path: str):
    current_path = "./"
    cwd = os.getcwd()
    if user_path != "":
        current_path = path.join(cwd, user_path)

    if not path.exists(current_path):
        return "404"
    if path.isdir(current_path):
        return render_template(
            'index.html',
            files=map(lambda x: {"url": path.join(user_path, x), "name": x},listdir(current_path)),
            address=f'http://{HOST}:{PORT}'
        )
    else:
        return flask.send_file(current_path)


@app.post('/upload')
def upload():
    uploaded_file = request.files['file']
    if uploaded_file.filename != None:
        uploaded_file.save(path.join('uploads', uploaded_file.filename))
    return redirect('/')


@app.get('/uploads/<filename>')
def download(filename):
    return send_from_directory('uploads', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
