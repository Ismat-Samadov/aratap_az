import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://aratap.az/dasinmaz-emlak/4441-torpaq.html'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the <a> element with class 'products-link'
a_element = soup.find('a', class_='products-link')

# Extract the value of the 'href' attribute
href_value = a_element['href']

print("Scraped href value:", href_value)
