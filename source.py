
# imported scraping modules
import requests
import bs4

# verified that modules are loaded properly
print("Requests: {}".format(requests.__version__))
print("Beautiful Soup: {}".format(bs4.__version__))

# creates requests object and verifies link is valid
url = "https://orange.weatherstem.com/ucf"  # will page with requisite weather data
result = requests.get(url)  # creates requests object
print("URL: {}".format(url))

url_status = result.status_code  # creates status code variable
print("Status Code: {}".format(url_status))
if url_status >= 200 and url_status < 300:
    # successful status codes for http begin with 2--
    print("Link is valid")
else:
    print("Error with the link")

# create web source variable
source = result.content

# creates soup object from web source
soup = bs4.BeautifulSoup(source, 'html.parser')
