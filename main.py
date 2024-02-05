from error_handling import requestExceptionHandling
from data_save import getKey, storeKey, apiKeyHandle
from temperature_conversion import convertCelsiusToRandomScale
import requests

# Query local storage for an API key, and request for one if none exist
def requestAPIKey(retry):
    apiKey = getKey(apiKeyHandle)
    if (apiKey is None):
        statementMod = ""
        if retry:
            statementMod = "re-"
        apiKey = input(f"Could you please {statementMod}input your OpenWeatherMap API key: ")
        storeKey(apiKeyHandle, apiKey)
    return apiKey

# The "overall" function that ties everything together, preforming the request and handling errors
# The retry paramater defined whether this is the second time preforming this request, tailoring the experience slightly to that fact
def initiateAPIRequest(retry = False):
    apiKey = requestAPIKey(retry)
    location = input("Enter the location you want to learn the location of:")
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={apiKey}&units=metric'
    response = requests.get(url)
    data = response.json()

    try:
        # Everything went well!
        currentTemperature = data['main']['temp']
        formattedConvertedTemperature = convertCelsiusToRandomScale(currentTemperature)
        print(f'Current temperature in {location} is {formattedConvertedTemperature}')
    except:
        # Handle instances where there is no internet
        requestExceptionHandling(data)

initiateAPIRequest()