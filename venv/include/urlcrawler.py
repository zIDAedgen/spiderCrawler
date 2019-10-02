from bs4 import BeautifulSoup
import urllib.request
import requests
import lxml
url = "https://www.airbnb.com.au/rooms/13903327?previous_page_section_name=1000"
r = requests.get(url)
r.endoding = 'utf-8'
r = r.text
print(r)
soup = BeautifulSoup(r, 'lxml')
print(soup.prettify())
