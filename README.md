# Temperature Representer
 Pass a location, and have the temperature of that place accessed from real-time data assigned a completely random (and maybe obscure) temperature scale.

# How to Use
No file manipulation is needed. All interactions can happen through the console window.

On start, you'll be requested for an API key for OpenWeatherMap.org (You can get one directly from them for free: https://openweathermap.org/api).
Once entered, this key will be locally stored and you won't be asked for it again.

You'll then be requested for a location.
Respond to the prompt, and on completion, you'll recieve a formatted output similar to one detailed below:
```
Current temperature in [LOCATION] is [ADJUSTED_TEMP][SCALE] ([ORIGINAL_TEMP]°C)
```