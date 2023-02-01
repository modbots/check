from subprocess import Popen
Popen(f"gunicorn server.server:app --bind 0.0.0.0:8080", shell=True)
Popen("python3 bot.py", shell=True)
