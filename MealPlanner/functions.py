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
    temp = []
    i = 0
    while i <3 and temp == []:
        temp = soup.find_all("div",{'class':"fela-_1qz307e"}) #Get ingredients
        if not temp:
            i+=1
            time.sleep(1)
    for x in temp:
        temp2 = x.find_all('p')
        for i in temp2:
            ingredients.append(i.text)

    try:
        i = 0
        for x in range(len(ingredients)):
            if x %2==0:
                ingredientList.append([ingredients[x],ingredients[x+1]])
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

def normalize_units(ingredients):
    consolidated = {}

    for x in ingredients:
        try:
            x[0] = uncode(x[0])
        except(TypeError):
            pass
        if x[2] not in consolidated:
            consolidated[x[2]] = {
                'amount' : float(x[0]),
                'measurement' : x[1]
            }
        else:
            if x[1] == consolidated[x[2]]['measurement']:
                consolidated[x[2]]['amount'] += float(x[0])
            else:
                consolidated[x[2]]['amount'] += float(x[0])
                consolidated[x[2]]['measurement'] += x[1]

    # if ingredient not in list, add it to list
    # if it is in list, check if units are the same
    # if yes, just combine amounts, if not 
    # 1 cup = 8 ounces
    # 1 tablespoon = .5 ounces
    # 1 teaspoon - 0.1666 ounces
    #ingredients = {}
    #TODO convert ingredients to normalized value (Grams?)
    return consolidated

def uncode(x):

    conversions = {
        188 : 0.25,
        189 : 0.5,
        190 : 0.75,
        8531 : 0.33,
        8532 : 0.66
    }
    if ord(x) in conversions:
        return conversions[ord(x)]

    return x

def test_get_meal():
    meal = get_meal('https://www.hellofresh.com/recipes/little-ears-pasta-5ab3bdd9ae08b53fd3288602')
    for x in meal:
        print(x,meal[x])

# test_get_meal()

# dscq dscv dsic dsaz dsbb dsbc dsid
# dsbz dsct dsfs dsbn dsbp dsbq dsft
# dscq dscv dsic dsaz dsbb dsbc dsid
# dsbz dsct dsfs dsbn dsbp dsbq dsft