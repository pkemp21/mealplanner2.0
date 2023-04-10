from multiprocessing.sharedctypes import Value
import requests
from bs4 import BeautifulSoup as bs

def get_meal(site):
    #TODO Hello fresh and BA in same function
    page        = requests.get(site)
    soup        = bs(page.content, 'html.parser')
    ingredientList = []

    imgUrl = soup.find(class_='fela-_14dtxzo') #Get image url TODO decide which resolution to grab(Split by space (width???), check length pick correct size)
    
    # mealTitle = soup.title.string.split('|')[0] #Get title TODO Delete if not needed

    tags = soup.find_all('span',{'class':'fela-_36rlri'}) #Get Tags
    if tags:
        for x in tags:
            print(x.get_text().strip('•'))
    
    ingredients = soup.find_all("p",{'class':"dsbz dsct dsfs dsbn dsbp dsbq dsft"}) #Get ingredients
    print(ingredients)
    try:
        for x in range(len(ingredients[::2])):
            ingredientList.append((ingredients[x].get_text(),ingredients[x+1].get_text()))
    except(ValueError):
        return

    print(ingredientList)
    # Meal dict - title(str), ingredients(dict?), meal url + image url, tags
        
    # meal = {
    #     'title'      : soup.title.string.split('|')[0],
    #     'Ingredients': ingredients,
    #     'imgUrl'     : soup.find(class_='fela-_14dtxzo'),
    #     'mealUrl'    : site,
    #     'tags'       : tags
    # }

    # print(meal)
    
    # return meal
    return

    

get_meal('https://www.hellofresh.com/recipes/cheese-tortelloni-in-a-mushroom-sauce-5d893112c6d5102c1923bdc5')

def normalize_units():
    #TODO convert ingredients to normalized value (Grams?)
    return