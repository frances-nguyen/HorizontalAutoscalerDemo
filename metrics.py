from prometheus_client import Counter

REQUEST_COUNT = Counter(
    "request_count", "App Request Count",
    ["app_name", "method", "endpoint", "http_status"]
)