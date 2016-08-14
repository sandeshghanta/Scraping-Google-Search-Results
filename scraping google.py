import requests, re
from bs4 import BeautifulSoup

url = 'http://www.google.com/search'
query = raw_input('Enter your search parameter: ')
payload = { 'q' : query }

my_headers = { 'User-agent' : 'Mozilla/11.0' }
r = requests.get( url, params = payload, headers = my_headers )

soup = BeautifulSoup( r.text, 'html.parser' )
h3tags = soup.find_all( 'h3', class_='r' )

for h3 in h3tags:
  if h3:
    print h3.a['href'].split('q=')[1].split('/')[2]
