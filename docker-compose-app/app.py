from flask import Flask
import redis
import datetime

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    visits = cache.incr('visits')
    return f"""
    <h1>🐍 Pipeline is Working!</h1>
    <p>Total visits: {visits}</p>
    <p>Current time: {datetime.datetime.now()}</p>
    """

@app.route('/health')
def health():
    return {{"status": "healthy"}}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
