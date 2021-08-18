# Step 1
def chuck_norris_joke():
    return "Chuck Norris does not do push ups. He moves the earth up and down."

def dad_joke():
    return "What do call a man with no body and no nose? Nobody knows"

def random_fact():
    return "We are 13.7 billion light years from edge of the observable universe"

def lambda_handler(event, context):
    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "PlainText"
            }
        }
    }
    print(event)
    if event["currentIntent"]["name"] == "FactsIntent":
        response["dialogAction"]["message"]["content"] = random_fact()
    else:
        if event["currentIntent"]["slots"]["joketype"] == "chuck norris":
            response["dialogAction"]["message"]["content"] = chuck_norris_joke()
        else:
            response["dialogAction"]["message"]["content"] = dad_joke()
    return response



# Step 2
import json
import requests

def chuck_norris_joke():
    try:
        URL = 'https://api.chucknorris.io/jokes/random'
        r = requests.get(url = URL)
        data = r.json()
        print(data)
        return data['value']
    except:
        return "Chuck Norris does not do push ups. He moves the earth up and down."

def dad_joke():
    try:
        URL = 'https://icanhazdadjoke.com/'
        r = requests.get(url = URL, headers = {'Accept':'application/json'})
        data = r.json()
        print(data)
        return data['joke']
    except:
        return "What do call a man with no body and no nose? Nobody knows"

def random_fact():
    try:
        URL = 'https://uselessfacts.jsph.pl/random.json?language=en'
        r = requests.get(url = URL)
        data = r.json()
        print(data)
        return data['text']
    except:
        return "We are 13.7 billion light years from edge of the observable universe"


def lambda_handler(event, context):
    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "PlainText"
            }
        }
    }
    print(event)
    if event["currentIntent"]["name"] == "FactsIntent":
        response["dialogAction"]["message"]["content"] = random_fact()
    else:
        if event["currentIntent"]["slots"]["joketype"] == "chuck norris":
            response["dialogAction"]["message"]["content"] = chuck_norris_joke()
        else:
            response["dialogAction"]["message"]["content"] = dad_joke()
    return response



