from django.shortcuts import render
from bs4 import BeautifulSoup
from django.shortcuts import render,redirect
import requests
import csv
import re
# Create your views here.

def webscrapping_views(request):
    html_response = requests.get("https://www.sastra.edu")
    # print(html_response)

    # html5lib <--> html.parser
    soup = BeautifulSoup(html_response.content, 'html.parser')

    news = []

    div = soup.find('div', attrs={'class': 'moduletable'})

    # print(soup.prettify())

    news_a = soup.findAll('a', attrs={'class': 'mod-articles-category-title'})
    # for i in news_a:
    #     print(i.getText())  # to get News Content
    #     print(i)  # to get News Content with html code [tags & href]

    for row in news_a:
        news_dict = {}
        news_dict['HtmlLink'] = "https://www.sastra.edu" + row['href']
        news_dict['News'] = row.getText()
        news.append(news_dict)
    # for i in news:
    #     print(i)
    dict = {
        'data':news,
    }
    print(dict)
    return render(request,'display2.html',{'links':news})