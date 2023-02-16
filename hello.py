import requests
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# Make a request to the Weatherstack API
api_key = os.getenv("API_KEY") 
city = 'New York'
response = requests.get(f'http://api.weatherstack.com/current?access_key={api_key}&query={city}')

# Convert the response to a dictionary
data = response.json()

# Extract the temperature and humidity values from the data
temp = data['current']['temperature']
humidity = data['current']['humidity']

# Plot the temperature and humidity data as a bar chart
plt.bar(['Temperature', 'Humidity'], [temp, humidity])
plt.title(f'Current weather in {city}')
plt.show()