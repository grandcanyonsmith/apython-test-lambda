from bs4 import BeautifulSoup
import requests

def lambda_handler(event, context):
    url = "https://www.coursecreator360.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    image_links = [img['src'] for img in images if 'src' in img.attrs and 'assert' in img['src']]
    return {"statusCode": 200, "body": image_links}