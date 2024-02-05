import os
import json
from cryptography.fernet import Fernet, InvalidToken

fileName = 'state.json'
kernetKeyHandle = 'fernet_key'
apiKeyHandle = 'api_key'

def getFilePath():
    directory = os.getcwd()
    filePath = os.path.join(directory, fileName)
    return filePath

def generateKey():
    return Fernet.generate_key()

def getOrCreateFernetKey():
    fernet_key_str = getKey(kernetKeyHandle)
    if fernet_key_str is None:
        new_key = generateKey()
        storeKey(kernetKeyHandle, new_key.decode())
        cipher_suite = Fernet(new_key)
    else:
        cipher_suite = Fernet(fernet_key_str.encode())
    return cipher_suite

# Function to get a specific key from the file. If it doesn't exist, returns None.
def getKey(key_name):
    filePath = getFilePath()
    if os.path.exists(filePath):
        with open(filePath, 'r') as file:
            data = json.load(file)
            if key_name in data:
                if key_name == kernetKeyHandle:
                    return data[key_name]
                
                try:
                    cipher_suite = getOrCreateFernetKey()
                    encrypted_key = data[key_name].encode()
                    decrypted_key = cipher_suite.decrypt(encrypted_key).decode()
                    return decrypted_key
                except InvalidToken as e:
                    print(f"Error decrypting key \"{key_name}\": Error - {str(e)}")
                    return None
    return None

# Function to store any key in the file, to which is encrypted by default if it's not the Fernet key itself.
def storeKey(key_name, key_value):
    filePath = getFilePath()
    data = {}
    if os.path.exists(filePath):
        with open(filePath, 'r') as file:
            data = json.load(file)
    if key_name != kernetKeyHandle:
        cipher_suite = getOrCreateFernetKey()
        encrypted_key = cipher_suite.encrypt(key_value.encode()).decode()
        data[key_name] = encrypted_key
    else:
        data[key_name] = key_value
    with open(filePath, 'w') as file:
        json.dump(data, file)