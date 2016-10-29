import requests
from bs4 import BeautifulSoup



name = input("Type user ID ")


def get_repositories(name):
    source_code = requests.get('https://github.com/' + str(name))
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    
    for contents in soup.find_all(class_="text-bold"):
        print ("Repository: ")
        print (contents)
    

get_repositories(name)

