import requests, re
from bs4 import BeautifulSoup
url = 'http://www.google.com/search'
web= raw_input('Enter your search parameter')
payload = { 'q' : web }
my_headers = { 'User-agent' : 'Mozilla/11.0' }
r = requests.get( url, params = payload, headers = my_headers )
soup = BeautifulSoup( r.text, 'html.parser' )
h3tags = soup.find_all( 'h3', class_='r' )
for h3 in h3tags:
    try:
	print
	
        print (re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1))
	
    except:
        continue



