# This is a simple flask app to quickly share files on your local network.

This is very simple app without any extra features. Checkout [https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask](https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask) for better implementation.


## Installation

Requirements:
- Python 3.6+
- virtualenv
- git

```bash
git clone https://github.com/Ar0manKhan/FileSharerLocally.git
cd FileSharerLocally
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
Note:
If you don't have git installed, you can download the zip file from the github page.
and then extract it and follow the rest of the steps.

## Usage

For windows:
```bash
python server.py
```

For Unix and Linux based systems:
```bash
python3 server.py
```