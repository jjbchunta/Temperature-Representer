from error_handling import requestExceptionHandling
from data_save import getKey, storeKey, apiKeyHandle
from temperature_conversion import convertCelsiusToRandomScale
import requests
import asyncio

# Query local storage for an API key, and request for one if none exist
def requestAPIKey(retry):
    apiKey = getKey(apiKeyHandle)
    if (apiKey is None):
        statementMod = ""
        if retry:
            statementMod = "re-"
        apiKey = input(f"Could you please {statementMod}input your OpenWeatherMap API key (You can get one here for free: https://openweathermap.org/api): ")
        storeKey(apiKeyHandle, apiKey)
    return apiKey

# Make an asyncronous request (along with potentially others) to Open Weather Map and automatically handle the proceeding conversion and printing
async def backgroundAPIRequest(apiKey, location):
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
        requestExceptionHandling(data, location)

# The "overall" function that ties everything together, preforming the request and handling errors
# The retry paramater defined whether this is the second time preforming this request, tailoring the experience slightly to that fact
async def initiateAPIRequest(retry = False):
    apiKey = requestAPIKey(retry)
    rawLocations = input("Enter the location you want to learn the temperature of (Seperate several with a \";\"): ")
    locationsMap = rawLocations.split(";")
    tasks = []
    for location in locationsMap:
        tasks.append(backgroundAPIRequest(apiKey, location.strip()))

    await asyncio.gather(*tasks)

asyncio.run(initiateAPIRequest())