import bs4
import requests
import pprint
WORDS = ['дизайн', 'фото', 'web', 'python']

HEADERS = {
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua-mobile': '?0',
     'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

base_url = 'https://habr.com'
url = base_url + '/ru/all/'

response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")

articles = soup.find_all("article")
for article in articles:
    article_text = article.find(class_='tm-article-body tm-article-snippet__lead')
    article_text = [info.text.strip() for info in article_text]
    for info in article_text:
        info_list = info.split()
        for word in info_list:
            if word in WORDS:
                title = article.find("h2").article.find("span").text
                href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
                link = base_url + href
                date = article.find(class_="tm-article-snippet__datetime-published").attrs["date"]
                print(f"Статья - {title} ===> {link}, дата размещения - {date}.")







