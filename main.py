from fastapi import FastAPI
import os
import httpx
from dotenv import load_dotenv
load_dotenv()

WEATHER_KEY = os.getenv("WEATHER_KEY")

app = FastAPI()


@app.get('/weather')
async def get_data_weather(lat: float = 10.9639, lon: float = -74.7964):

    URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=es&appid={WEATHER_KEY}"

    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        return response.json()

@app.get('/news')
async def get_news_data():
    URL = "https://newsdata.io/api/1/latest?apikey=pub_cae0254cbf7144f7abc4712d69937803&q=barranquilla%20AND%20hurto%20OR%20recompensa%20OR%20ultima%20hora%20OR%20asalto%20OR%20atentado%20OR%20alerta%20OR%20robo&country=co&language=es&category=crime&removeduplicate=1"

    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        return response.json()