import urllib.request, json
from .models import Article, Source
from dateutil import parser

# Getting api key
api_key = None

# Getting the news base url
base_url = None

# Getting the src base url
src_aticles_base_url = None

# Getting the search base url
search_base_url = None

def configure_src_request(app):
    global api_key, base_url, src_aticles_base_url, search_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SRC_API_BASE_URL']
    src_aticles_base_url = app.config['ARTICLES_FROM_SRC_BASE_URL']
    search_base_url = app.config['SEARCH_BASE_URL']

    