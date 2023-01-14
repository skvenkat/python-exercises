# movie-service/app/api/service.py

import os
import httpx

CAST_SERVICE_HOST_URL = "http://localhost:8082/api/v1/casts"
url = os.getenv("CAST_SERVICE_HOST_URL") or CAST_SERVICE_HOST_URL

def is_cast_present(cast_id: int):
    #resp = httpx.get(f'{url}/{cast_id}')
    resp = httpx.get(f'http://cast_service:8082/api/v1/casts/{cast_id}')
    return True if r.status_code == 200 else False
