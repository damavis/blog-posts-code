from flask import Flask, request
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

trace.set_tracer_provider(TracerProvider())
tracer_provider = trace.get_tracer_provider()

console_exporter = ConsoleSpanExporter()
tracer_provider.add_span_processor(SimpleSpanProcessor(console_exporter))


app = Flask(__name__)

FlaskInstrumentor().instrument_app(app)

@app.route("/server_request")
def server_request():
    print(request.args.get("param"))
    return "served"


if __name__ == "__main__":
    app.run(port=8082)