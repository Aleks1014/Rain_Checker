# Rain_Checker


## Introduction
Simple Python app that check what the weather is going to be and if it's going to rain it will send SMS to the user to inform them. It's using Open Weather API to get the lattitude and longtitude of the location and get the weather report and Twilio API to send the notification.

## Getting Started
- Clone the repository
- Install the needed packages (pip install -r requirements.txt)

## Getting API keys
### Open Weather
First, you need to create an account at https://openweathermap.org/ . Once you've confirmed your account, you can find the API key under your profile -> My API keys.

### Twilio
Register your account at 

## Running the app
Currently, the app will require the user to provide:
- Twilio account_sid
- Twilio auth_token
- Your phone number
- Open Weather api key
- City (and Country)

## Room for development
The api keys and tokens can be set as environment variables for better security. The app can also be deployed to a server or cloud-based platform (for example pythonanywhere.com) to automate it.


