from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
from bs4 import NavigableString
import re
import json


def urlify(s):
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)
    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '', s)
    return s

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

def has_attr_data_ingredient(tag):
    return tag.has_attr('data-ingredient')

recipe_path = "/Users/ben/Developer/chewigy/data/raw"
output_path = "/Users/ben/Developer/chewigy/data/json"

for file in listdir(recipe_path):
    print(file)
    if file == ".DS_Store":
        continue
    file_path = join(recipe_path, file)
    write_path = join(output_path, file+".json")
    raw_html = open(file_path, 'r', encoding='utf-8', errors='ignore')
    f = open(write_path, 'w')
    soup = BeautifulSoup(raw_html, 'html.parser')
    recipe_title = soup.find('h1')
    if recipe_title is None:
        recipe_title = ""
    else:
        recipe_title = recipe_title.string

    # print('title: ' + recipe_title.string)
    # f.write(recipe_title.string)

    ready_in_ele = soup.find('div',class_="recipe-cooktime")
    if ready_in_ele is None:
        ready_in = "n/a"
    else:
        ready_in = ready_in_ele.text.rstrip()
        ready_in = urlify(ready_in)[7:]
    # ready_in = urlify(ready_in)
    # f.write("\n")
    # f.write(ready_in)

    serving_ele = soup.find('li',id="yield-servings")
    serving_str = cleanhtml(str(serving_ele))
    serving_str = urlify(serving_str)[8:]
    # print('serves: ' + serving_str)

    ingredient_list = soup.find_all(has_attr_data_ingredient)
    ingredients = list()
    for ingredient in ingredient_list:
        desc = cleanhtml(str(ingredient))
        ingredients.append(desc)
    
    directions = list()
    for direction in soup.select('ol > li'):
        directions.append(cleanhtml(str(direction)))
    directions = directions[:len(directions)-1]

    info = json.dumps({
        'url': 'http://www.food.com/recipe/'+file,
        'title': recipe_title,
        'ready_in': ready_in,
        'serves': serving_str,
        'ingredients': ingredients,
        'directions': directions
    }, indent=4)
    
    f.write(info+'\n')
    f.close()

    # direction = soup.find('ol')
    # lis = direction.find_all(True, recursive=False)
    # print(len(lis))
    # i = 0
    # while i < len(lis) - 1:
    #     li = lis[i]
    #     f.write("\n")
    #     f.write(li.string)
    #     i += 1
    # f.close()