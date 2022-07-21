# program to fetch top news headlines for a specified country
# results are from https://newsapi.org/

import requests

# the function returns a list of dictionaries each dictionary representing information about an article.
# each dictionary has 3 keys (source, title, link/url)
# the function takes two parameters a country code and an api_key

def top_headlines(country: str, api_Key: str):
    lst = []

    endpoint = "https://newsapi.org/v2/top-headlines"
    parameters = {"country": country, "apiKey": api_Key}
    request = requests.get(endpoint, params=parameters)
    articles_list = request.json()['articles']

    for article in articles_list:
        article_dict = {
            'source': article['source']['name'],
            'title': article['title'],
            'link': article['url']
        }
        lst.append(article_dict)
    
    return lst

# the following searches for news articles for a specified topic 
def news(api_key: str, topic: str, domain: str = None, from_date: str = None, to_date: str = None,
         language: str = "en",
         sortby: str = "publishedAt"):
    lst = []
    endpoint = "https://newsapi.org/v2/everything"
    parameters = {"apiKey": api_key, "q": topic, "domains": domain, "from": from_date, "to": to_date,
                  "language": language, "sortBy": sortby}
    request = requests.get(endpoint, params=parameters)
    articles_list = request.json()['articles']

    for article in articles_list:
        article_dict = {
            'source': article['source']['name'],
            'title': article['title'],
            'link': article['url'],
            'date': article['publishedAt'][:10]
        }
        lst.append(article_dict)
    return lst
