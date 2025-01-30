from flask import Flask, Response
from prometheus_client import Counter, generate_latest, REGISTRY

app = Flask(__name__)

request_counter = Counter('app_requests_total', 'Total requests', ['method', 'endpoint'])

@app.route('/')
def home():
    request_counter.labels(method='GET', endpoint='/').inc()
    return "Hi Prometheus!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(REGISTRY), mimetype='text/plain; version=0.0.4; charset=utf-8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)