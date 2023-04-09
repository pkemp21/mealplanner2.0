import requests
from bs4 import BeautifulSoup as bs

def get_hf_meal(site):
    page = requests.get(site)
    soup = bs(page.content, 'html.parser')

    print(soup.title.string.split('|')[0])
    temp = soup.find_all("div",{'class':"dsbz dsct dsfs dsbn dsbp dsbq dsft"})
    for x in temp:
        print(x)

get_hf_meal('https://www.hellofresh.com/recipes/peppercorn-steak-w06-5857fcd16121bb11c124f383')