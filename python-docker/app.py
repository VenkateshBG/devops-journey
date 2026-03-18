from flask import Flask
import datetime
import platform

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>🐍 Pipeline is Working!</h1>
    <p>Current time: {datetime.datetime.now()}</p>
    <p>Python version: {platform.python_version()}</p>
    <p>Running on: {platform.system()} {platform.release()}</p>
    """

@app.route('/health')
def health():
    return {"status": "healthy", "timestamp": str(datetime.datetime.now())}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
