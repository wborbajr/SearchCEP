import requests


def locateCEP():
    req = None

    try:
        req = requests.get(' ')
    except:
        print('Error trying ....')
        exit()

    dictionary = json.loads(req.text)

    print(dictionary)


'''
main function

if __name__== "__main__":
'''
locateCEP()
