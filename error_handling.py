# Depending on the response from the API request, handle the error properly.
def requestExceptionHandling(data, location):
    message = data['message']
    print(f"Attempt to access \"{location}\" failed: " + message)

    # Outside of communicating the error, see if any actionable steps could be taken
    # from main import initiateAPIRequest
    message = message.lower()
    if ('invalid' in message and 'key' in message):
        print("A re-input of your API key is needed.")
        # initiateAPIRequest(retry = True)