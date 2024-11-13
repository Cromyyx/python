import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get('https://quotes.toscrape.com', headers=headers)

url = "https://brawlify.com/maps/#Brawl-Ball"
page = requests.get(url)
print(page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')

quotes = []
main_title_elements = soup.find(id='Brawl-Ball')
names = main_title_elements.find_all(class_='card-title mb-1')
times = main_title_elements.find_all(class_='card-img-overlay text-center')

list_name = []
list_time = []
for name in names:
    text_name = name.find('span', class_='badge map-name').text
    list_name.append(text_name)

for time in times:
    text_time = time.find('span', class_='badge map-name text-hp2')
    if text_time is None: #Aktive maps have "None" time, this changes them to 0
        list_time.append("0")
    else:
        text_time = time.find('span', class_='badge map-name text-hp2').text
        list_time.append(text_time)

list_fused = []
for i in range(11): #Brawball 8 active maps
    list_temp = []
    list_temp.append(list_name[i])
    list_temp.append(list_time[i])
    list_fused.append(list_temp)


def filter_list(lst):
    # initialize an empty list to store the filtered elements
    filtered = []
    # initialize a variable to store the previous time
    prev_time = None
    # loop through the original list
    for element in lst:
      # get the current element and its time
      time = element[1]
      # check if the current time is different from the previous time
      if time != prev_time:
        # append the element to the filtered list
        filtered.append(element)
        # update the previous time
        prev_time = time
    # return the filtered list
    return filtered


print(filter_list(list_fused))


