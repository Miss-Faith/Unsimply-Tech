import urllib.request,json
from .models import *

# Getting the quote base url
quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def configure_request(app):
    global quote_url
    quote_url = app.config['QUOTES_URL']

def get_quote():
    '''
    Function that gets the json response to our url request
    '''

    with urllib.request.urlopen(quote_url) as url:
        get_quote_data = url.read()
        quote = json.loads(get_quote_data)

    return quote