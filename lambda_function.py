import yfinance as yf

def lambda_handler(event, context):
    return {'statusCode': 200, 'body': yf.Ticker("TSLA").info['regularMarketPrice']}