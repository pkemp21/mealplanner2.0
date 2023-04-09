import requests
from bs4 import BeautifulSoup as bs

def get_hf_meal(site):
    #TODO Hello fresh and BA in same function
    page = requests.get(site)
    soup = bs(page.content, 'html.parser')

    imgUrl = soup.find(class_='fela-_14dtxzo') #Get image url TODO 
    for x in imgUrl:
        print(x)
    print(soup.title.string.split('|')[0]) #Get title
    temp2 = soup.find_all('span',{'class':'fela-_36rlri'}) #Get Tags
    if temp2:
        for x in temp2:
            print(x.get_text().strip('•'))

    # temp = soup.find_all("p",{'class':"dsbz dsct dsfs dsbn dsbp dsbq dsft"}) #Get ingredients
    # for x in temp:
        # print(x.get_text())
    #Meal dict - title(str), ingredients(dict?), meal url + image url, tags

get_hf_meal('https://www.hellofresh.com/recipes/cheese-tortelloni-in-a-mushroom-sauce-5d893112c6d5102c1923bdc5')

def normalize_units():
    #TODO convert ingredients to normalized value (Grams?)
    return