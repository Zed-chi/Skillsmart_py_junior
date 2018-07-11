"""
Web Scraping task

BeautifulSoup module
"""
import requests
from bs4 import BeautifulSoup as web

##Проверка успешного пост запроса
def post_req():
    print("Проверка статуса запроса на http://httpbin.org/post :")
    response = requests.post('http://httpbin.org/post',
                  data = {'UserId':'12345', 'Status':'On'})
    if response.status_code == 200:
        print("Запрос прошел, статус - %d"%response.status_code)
    else:
        print("Запрос Не прошел, статус - %d"%response.status_code)

##Получение новинок издательства BHV
def books_scraping():
    response = requests.get("http://bhv.ru")

    if response.status_code == 200:
        response.encoding = "cp1251"
        content = web(response.text, "html.parser")
        books = content.select("#pageRightColumn > .infoBlock > .bookInfo")
        print("===Новинки издательства===\n")
        for book in books:
            author =  book.select(".bookAuthor")[0].getText()
            title = book.select(".bookTitle > a")[0].getText()
            print(author, "->", title )