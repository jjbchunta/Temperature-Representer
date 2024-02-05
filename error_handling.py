# Depending on the response from the API request, handle the error properly.
def requestExceptionHandling(data):
    message = data['message']
    print(message)

    # Outside of communicating the error, see if any actionable steps could be taken
    from main import initiateAPIRequest
    message = message.lower()
    if ('invalid' in message and 'key' in message):
        print("Suggest a re-input of the API key")
        initiateAPIRequest(retry = True)