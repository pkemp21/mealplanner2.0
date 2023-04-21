from multiprocessing.sharedctypes import Value
import requests, time
from bs4 import BeautifulSoup as bs

def get_meal(site):
    #TODO Hello fresh and BA in same function

    #Hello fresh TODO Add parser to differenciate BA and HF
    page           = requests.get(site)
    soup           = bs(page.content, 'html.parser')
    ingredientList = []
    tagList        = []

    imgUrl = soup.find(class_='fela-_14dtxzo').get_text #Get image url 
    for x in str(imgUrl).split():
        if 'src=' in x:
            imgUrl = x.split('=')[1].strip('"')
            break

    tags = soup.find_all('span',{'class':'fela-_36rlri'}) #Get Tags
    if tags:
        for x in tags:
            tagList.append((x.get_text().strip('•')))

    #Get ingredients TODO error handle
    ingredients = []
    i = 0
    while i <3 and ingredients == []:
        ingredients = soup.find_all("p",{'class':"dsbz dsct dsfs dsbn dsbp dsbq dsft"}) #Get ingredients
        if not ingredients:
            page = requests.get(site)
            soup = bs(page.content, 'html.parser')
            i+=1
            time.sleep(1)
    
    
    try:
        i = 0
        for x in range(len(ingredients)):
            if x %2==0:
                ingredientList.append((ingredients[x].get_text(),ingredients[x+1].get_text()))
    except(ValueError):
        return
   
    meal = {
        'title'      : soup.title.string.split('|')[0],
        'ingredients': ingredientList,
        'imgUrl'     : imgUrl,
        'mealUrl'    : site,
        'tags'       : tagList
    }

    # print(meal)
    
    return meal

# meal = get_meal('https://www.hellofresh.com/recipes/cheese-tortelloni-in-a-mushroom-sauce-5d893112c6d5102c1923bdc5')
# for x in meal:
#     print(x,meal[x])

def normalize_units(ingredients):

    #ingredients = {}
    #TODO convert ingredients to normalized value (Grams?)
    return