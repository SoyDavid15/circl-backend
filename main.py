from fastapi import FastAPI
import httpx

WEATHER_KEY = "6cc9ccedd6de5691035785e3983f1048"

app = FastAPI()

@app.get('/')
async def get_data_weather(lat: float = 10.9639, lon: float = -74.7964):

    URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=es&appid={WEATHER_KEY}"

    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        return response.json()

    