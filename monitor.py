from flask import Flask
import psutil

app = Flask(__name__)

@app.route('/')
def monitor():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return f"CPU használat: {cpu}%<br>Memória használat: {mem}%"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
