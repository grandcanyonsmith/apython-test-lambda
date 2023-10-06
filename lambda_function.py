import json
from bs4 import BeautifulSoup
import requests

def lambda_handler(event, context):
    event_body = json.loads(event['body'])
    url = event_body['website_url']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    image_links = [img['src'] for img in images if img.has_attr('src')]
    return {"statusCode": 200, "body": json.dumps(image_links)}