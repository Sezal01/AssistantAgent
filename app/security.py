from fastapi import HTTPException

API_KEY = "your-secure-api-key"

def validate_api_key(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key
