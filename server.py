from os import path, listdir, getcwd
from flask import Flask, redirect, render_template, request, send_from_directory, send_file


def get_local_ip():
    from socket import socket, AF_INET, SOCK_DGRAM
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    return s.getsockname()[0]


PORT = 5000
HOST = get_local_ip()

app = Flask(__name__)


@app.get('/', defaults={"user_path": ""})
@app.get('/<path:user_path>')
def home(user_path: str):
    current_path = extract_path(user_path)
    if not path.exists(current_path):
        return "404"
    if path.isdir(current_path):
        return render_template(
            'index.html',
            files=map(lambda x: {"url": path.join(user_path, x), "name": x},listdir(current_path)),
            address=f'http://{HOST}:{PORT}',
            path=user_path,
        )
    else:
        return send_file(current_path)

def extract_path(user_path: str):
    if user_path == "":
        return getcwd()
    else:
        return path.join(getcwd(), user_path)

@app.post('/', defaults={"user_path": ""})
@app.post('/<path:user_path>')
def upload(user_path: str):
    current_path = extract_path(user_path)
    uploaded_file = request.files['file']
    print(f'{uploaded_file=} -- {uploaded_file.filename=}')
    if uploaded_file.filename:
        uploaded_file.save(path.join(current_path, uploaded_file.filename))
    return redirect(f'/{user_path}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
