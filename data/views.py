from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from weather_app.settings import WEATHER_API_KEY

# import request library to call the url.
import requests


# Create your views here.
@api_view(["GET"])
def fetch_data(request):
    lat = request.data.get("latitude")
    lon = request.data.get("longitude")

    if lat and lon:
        # building the url which needs to be called. Url structure obtained from the weather api docs.
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}"

        # Add .json() at the end to get the data json.
        data = requests.get(url).json()

        payload = {
            "city": data.get("name"),
            "country": data.get("sys").get("country"),
            "coordinates": data.get("coord"),
            # using round to get only 2 decimal places. Subtracting 273 to get Celsius instead of kelvin.
            "temp_min": round(data.get("main").get("temp_min") - 273, 2),
            "temp_max": data.get("main").get("temp_max") - 273,
            "clouds": data.get("weather")[0].get("description"),
            "humidity": data.get("main").get("humidity"),
        }

        return Response({"payload": payload, "data": data})
    return Response({"message": "Please enter latitude and longitude"})
