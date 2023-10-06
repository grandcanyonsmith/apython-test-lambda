import requests


def lambda_handler(event, context):
    url = "https://www.coursecreator360.com/"
    response = requests.get(url)
    return {"statusCode": 200, "body": response.text}
