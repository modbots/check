from flask import *
import requests
from subprocess import Popen
app = Flask(__name__)
Popen(f"gunicorn server.server:app --bind 0.0.0.0:8080", shell=True)
if __name__=="__main__":
    app.run()
