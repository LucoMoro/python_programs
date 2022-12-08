import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser") 
#BeautifulSoup's input is a string that contains 
# html or xml and a parser

questions = soup.select(".question-summary")
#print(type(questions[0].get("id", 0)))
#print(type(questions[0].select(".question-hyperlink")))
#print(type(questions[0].select_one(".question-hyperlink").getText()))

for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())