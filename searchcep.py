import requests


req = None

try:
    req = requests.get(' ')
except:
    print('Error trying ....')
    exit()

dictionary = json.loads(req.text)

print(dictionary)