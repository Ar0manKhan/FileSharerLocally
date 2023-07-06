# This is a simple flask app to quickly share files on your local network.

This is very simple app without any extra features. Checkout [https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask](https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask) for better implementation.


## Installation

Requirements:
- Python 3.6+
- virtualenv
- git

```bash
git clone
cd FileSharerLocally
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

For windows:
```bash
python server.py
```

For Unix and Linux based systems:
```bash
python3 server.py
```