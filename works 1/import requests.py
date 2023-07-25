import requests

def get_news(api_key):
    url = f"https://newsapi.org/docs/endpoints/top-headlines={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        articles = data["articles"]
        for article in articles:
            title = article["title"]
            description = article["description"]
            source = article["source"]["name"]
            print(f"Title: {title}\nSource: {source}\nDescription: {description}\n")
    else:
        print("Failed to fetch news")

# Set your NewsAPI API key here
api_key = ("G7HtkOKEkkkmVyU2pjyar2GIUn80gU0R")

get_news(api_key)
