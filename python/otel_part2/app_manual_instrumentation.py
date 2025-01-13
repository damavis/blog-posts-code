from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
console_exporter = ConsoleSpanExporter()
trace.get_tracer_provider().add_span_processor(SimpleSpanProcessor(console_exporter))

app = Flask(__name__)
@app.route("/server_request")
def manual_tracing():
    with tracer.start_as_current_span("manual_span") as span:
        span.set_attribute("custom_attribute", "Custom Value!!!")
        result = "Hello World from a manually traced endpoint!"
        span.add_event("processing complete")
    return result

if __name__ == "__main__":
    app.run(port=8082)