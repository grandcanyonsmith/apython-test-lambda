import json
import requests

def lambda_handler(event, context):
    body = json.loads(event['body'])
    symbol = body['symbol']

    url = "https://alpha-vantage.p.rapidapi.com/query"
    querystring = {"function":"GLOBAL_QUOTE","symbol":symbol,"datatype":"json"}
    headers = {
        "X-RapidAPI-Key": "0519a48ad0msh3652be7be3a1163p1b2223jsn9212f364e710",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return {'statusCode': 200, 'body': response.json()}