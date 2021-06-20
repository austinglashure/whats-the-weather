
# imported scraping modules
import requests
import bs4

# verified that modules are loaded properly
print("Requests: {}".format(requests.__version__))
print("Beautiful Soup: {}".format(bs4.__version__))

# verifies that URL is valid
url = "https://www.google.com"  # will eventually be page with requisite weather data
result = requests.get(url)  # creates requests object
print("URL: {}".format(url))
url_status = result.status_code  # creates status code variable
print("Status Code: {}".format(url_status))
if url_status == 200:
    print("Link is valid")
else:
    print("Error with the link")

