import requests

OWM_Endpoint = "https://api.openweathermap.org/data/4.0/onecall/current"
api_key = "88c3c99247eede21805a6383a7b80d48"

weather_params = {
    "lat": 51.359909,
    "lon": -0.149890,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
print(response.json())
