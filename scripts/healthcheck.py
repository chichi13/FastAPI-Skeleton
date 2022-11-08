import requests

url = "http://127.0.0.1:8000/api/v1/health"

try:
    r = requests.get(url)
    r.raise_for_status()
except requests.exceptions.HTTPError as e:
    raise SystemExit(e)
