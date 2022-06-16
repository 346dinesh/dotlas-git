import json
import requests,sys
from bs4 import BeautifulSoup
from pprint import pprint

path = 'results.txt'
sys.stdout = open(path, 'w')

##urls are taken manually this also can be taken from a file also.
urls=[
    'https://www.talabat.com/uae/restaurant/621133/ginos-deli-jlt?aid=1308',
    'https://www.talabat.com/uae/restaurant/645430/pasta-della-nona-jlt-jumeirah-lakes-towers?aid=1308',
    'https://www.talabat.com/uae/restaurant/50445/pizzaro-marina-3?aid=1308',
    'https://www.talabat.com/uae/restaurant/605052/the-pasta-guyz-dubai-marina?aid=1308',
    'https://www.talabat.com/uae/restaurant/621796/pizza-di-rocco-jumeirah-lakes-towers--jlt?aid=1308',
    'https://www.talabat.com/uae/restaurant/667927/tarboush-express-jumeirah-1?aid=1308',
    'https://www.talabat.com/uae/restaurant/666576/prept-restaurant-business-bay-4?aid=1308',
    'https://www.talabat.com/uae/restaurant/616372/manaesho-business-bay?aid=1308',
    'https://www.talabat.com/uae/restaurant/664823/society-pizza-al-satwa?aid=1308',
    'https://www.talabat.com/uae/restaurant/623767/biryani-pot-jumeirah-1?aid=1308'
]

# this code is written as basic where we need to collect data from all 10 url given and prints all data about restaurants from talabat.com 
# it mainly returns name,logo url,cuisines,latitude,longitude of restuarants and items in the menu of each restaurant

# Details also from the menu is given for each items returns its name,price,description and item_image url


def Restaurant(data):
    restaurant_details=dict()
    restaurant_details[data['name']]=[]
    restaurant_details[data['name']].append(data['logo'])
    restaurant_details[data['name']].append([data['cuisineString']])
    restaurant_details[data['name']].append([data['latitude'],data['longitude']])
    return restaurant_details

def RestaurantMenu(data):
    menu_details=dict()
    for i in data:
        menu_details[i['name']]=[]
        menu_details[i['name']].append(i['description'])
        menu_details[i['name']].append(i['price'])
        menu_details[i['name']].append(i['image'])
    return menu_details


for i in urls:
    print('####',urls.index(i)+1)
    response = requests.get(i)

    soup = BeautifulSoup(response.content, 'html.parser')

    h=soup.find('script',id='__NEXT_DATA__').text
    stud_obj = json.loads(h)
    data=stud_obj['props']['pageProps']['initialMenuState']
    restaurant_details=Restaurant(data['restaurant']) ## this function return all restaurant details with name,logo,cuisines offered and location
    print("restaurant_details:")
    pprint(restaurant_details) #pprint to get output in better way
    menu_details=RestaurantMenu(data['menuData']['items']) ##this function returns all menu items in the restaurant with every item specific price,description and iamge logo.
    print("menu_items:")
    print(list(menu_details.keys()))
    print('menu_details:')
    pprint(menu_details) 

    print()
    print()