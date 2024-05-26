import requests
from twilio.rest import Client
import os

account_sid = input('Your Twilio account sid:')
auth_token = input('Your Twilio auth token:')
receiver_number = input('Your phone number:')

# os.environ['account_sid'] = account_sid
# os.environ['auth_token'] = auth_token

app_id = input('Your Open Weather api key:')
# os.environ['app_id'] = app_id
searched_location = input('Enter city and country (ex: London,UK):')


location_response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={searched_location}&appid={app_id}')
location_data = location_response.json()

location_lat = location_data[0]['lat']
location_lon = location_data[0]['lon']

api_params = {
    'appid': app_id,
    'lat': location_lat,
    'lon': location_lon,
    'cnt': 4,
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast?', params=api_params)
response.raise_for_status()
weather_data = response.json()

weather_list = weather_data['list']
bring_umbrella = False

for hour_data in weather_list:
    condition_code = int(hour_data['weather'][0]['id'])
    if condition_code < 700:
        bring_umbrella = True

if bring_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"It's going to rain today in {searched_location}. Bring your umbrella.☔",
        from_='+447397828139',
        to=receiver_number,
    )

    print(message.status)
