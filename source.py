# imported scraping modules
from googlesearch import search
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
temperature = parts[0]
summary = parts[1]
# get rain chance
precip_temp = soup.find('div', class_='CurrentConditions--precipValue--3nxCj').text
aye = precip_temp.index('%')
precipitation_chance = precip_temp[0, aye+1]
print(precipitation_chance)

'''
result = requests.get(url)  # creates requests object
print("URL: {}".format(url))

url_status = result.status_code  # creates status code variable
print("Status Code: {}".format(url_status))
if url_status >= 200 and url_status < 300:
    # successful status codes for http begin with 2--
    print("Link is valid")
else:
    print("Error with the link")

# creates soup object from web source
soup = bs4.BeautifulSoup(result.content, 'lxml')
dd_tags = soup.find_all('dd')
for tag in dd_tags:
    print(tag)
'''
 