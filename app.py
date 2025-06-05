import streamlit as st
import requests
import os

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

st.title("🌦️ Weather App")

city = st.text_input("Enter a city name")

if city:
    data = get_weather(city)
    if data:
        st.subheader(f"Weather in {city.title()}")
        st.write(f"**Temperature:** {data['current']['temp_c']} °C")
        st.write(f"**Humidity:** {data['current']['humidity']}%")
        st.write(f"**Wind Speed:** {data['current']['wind_kph']} km/h")
    else:
        st.error("City not found or error retrieving data.")
