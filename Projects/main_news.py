import requests
query = input("Enter the topic you want to search for: ")
api = "3ffeacf1892443298d8a3ceab7828b98"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-05&sortBy=publishedAt&apiKey={api}"

r = requests.get(url)

data = r.json()

articles = data["articles"]

for index, articles in enumerate(articles):
    print(index + 1 ,articles["title"] , articles["url"])
    print("\n***************************\n")