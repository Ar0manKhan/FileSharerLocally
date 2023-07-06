from os import path, listdir
from flask import Flask, render_template, request, send_from_directory


def get_local_ip():
    from socket import socket, AF_INET, SOCK_DGRAM
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    return s.getsockname()[0]


PORT = 5000
HOST = get_local_ip()

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(f'{request.host_url=}')
    return render_template(
        'index.html',
        files=listdir('uploads'),
        address=f'http://{HOST}:{PORT}'
    )


@app.post('/upload')
def upload():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(path.join('uploads', uploaded_file.filename))
    return render_template('index.html')


@app.get('/uploads/<filename>')
def download(filename):
    return send_from_directory('uploads', filename)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
