from os import path, listdir
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', files=listdir('uploads'))


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
    app.run(debug=True)
