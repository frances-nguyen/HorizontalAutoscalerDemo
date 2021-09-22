from metrics import REQUEST_COUNT
from flask import request
import os

def record_request_data(response):
    REQUEST_COUNT.labels("hpa_app", request.method, request.path, response.status_code).inc()
    return response

def setup_metrics(app):
    app.after_request(record_request_data)