from django.shortcuts import render
from bs4 import BeautifulSoup
import pandas as pd
import requests
# Create your views here.
def webScraping(request):
    url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'html.parser')
    a_tag = soup.find_all('a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
    # print(a_tag[:5])
    a_href = []
    text = []

    for link in a_tag[:20]:
        a_href.append(f"https://www.amazon.in{link.get('href')}")
        text.append(link.get_text())

    rating_tag = soup.find_all(class_="a-icon-alt")
    rating = []
    for rate in rating_tag[:20]:
        rating.append(rate.get_text())

    price_tag = soup.find_all(class_="a-price-whole")
    price = []

    for data in price_tag[:20]:
        price.append(data.get_text())

    review_list = []
    review_tag = soup.find_all(class_="a-size-base s-underline-text")
    for data in review_tag[:20]:
        review_list.append(data.get_text())
    print(price)
    return render(request, 'homepage.html', {'urls':a_href, 'texts':text, 'ratings':rating, 'prices':price, 'reviews':review_list, 'num':range(20)})

