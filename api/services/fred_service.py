import requests
from django.conf import settings

BASE_URL = "https://api.stlouisfed.org/fred"

def get_fred_series(series_id: str):
    url = f"{BASE_URL}/series/observations?series_id={series_id}&api_key={settings.FRED_API_KEY}&file_type=json"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()
