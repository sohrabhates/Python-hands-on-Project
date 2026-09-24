import requests

query = input("Enter the topic you want to search for: ")
api = "66feefb6ae24409595130cc6b5049463"


url = f"https://newsapi.org/v2/everything?q={query}&from=2026-06-28&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index,article in enumerate(articles):
    print(index + 1,article["title"]),print(article["url"])
    print("\n---------------------------------------------------\n")