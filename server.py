import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.post('/upload')
def upload():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join('uploads',uploaded_file.filename))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)