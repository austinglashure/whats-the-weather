# imported scraping modules
from googlesearch import search
from datetime import datetime, date
import requests
import bs4

# verified that modules are loaded properly
print("Requests: {}".format(requests.__version__))
print("Beautiful Soup: {}".format(bs4.__version__))

# get the link
search_text = "weather.com today oviedo fl"
links_list = search(search_text, stop=15)
link = ''
for foo in links_list:
    if 'today' in foo:
        link = foo
        break

# make scrape objects
req = requests.get(link)
soup = bs4.BeautifulSoup(req.content, 'lxml')

# parse relevant info
foo = soup.find('div', class_='CurrentConditions--primary--2SVPh')
fub = foo.text
parts = fub.split('°')
# said relevant info
temperature = parts[0] + " degrees"
summary = parts[1]
precip_chance = soup.find('div', class_='CurrentConditions--precipValue--3nxCj').text
now = datetime.now()
time_and_date = now.strftime("%d/%m/%Y %H:%M:%S")

# put it into a text file for posterity
file = open('weather.txt', 'a+')
file.write('\n')
file.write(time_and_date)
file.write("\n")
file.write(temperature)
file.write("\n")
file.write(precip_chance)
file.write("\n")
file.write(summary)
file.write("\n")
file.write("--------------")
'''
file.writelines(temperature)
file.writelines(precip_chance)
file.writelines(summary)
file.writelines("\n")'''
file.close()
