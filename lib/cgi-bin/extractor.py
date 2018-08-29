# URL extraction from website
#

import cgi
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import ssl

print('Content-type: text/html\n\n')
print('<H3>URL Extractor</H3>')
print() 
form = cgi.FieldStorage()

protocol = form['protocol'].value
host = form['host'].value
port = form['port'].value
filter = form['filter'].value
uri = form['uri'].value
file = form['file'].value
nav_urls = []
PDP_urls = []
urls = []

# funciton to parse url
def html_parser(url):
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    usock = urllib.request.urlopen(url, context = gcontext)
    data = usock.read()
    usock.close()
    soup = BeautifulSoup(data, 'html.parser')
    return soup
	
url = str(protocol + '://' + host + ':' + port + uri) # write the url here
soup_home = html_parser(url)
div_list = soup_home.find_all('div')

# function to remove duplicated value from list
def remove_duplicate(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

# extract urls from navigation bar
for item in div_list:
    div_soup = BeautifulSoup(str(item), 'html.parser')
    if 'navigationbarcollectioncomponent' in str(div_soup.div):
        divNav_soup = BeautifulSoup(str(div_soup), 'html.parser')
	for a_link in divNav_soup.find_all('a'):
            nav_urls.append(str(a_link.get('href')))
	break
			
# extract urls from PLP
for i in range(len(nav_urls)):
    full_nav_url = str(protocol + '://' + host + ':' + port + nav_urls[i])
    PLP_soup = html_parser(full_nav_url)
    for PLP_A_link in PLP_soup.find_all('a'):
        PDP_link = str(PLP_A_link.get('href'))
        if filter in PDP_link:
            PDP_urls.append(PDP_link)

# meger and remove duplicated urls
urls = remove_duplicate(values = nav_urls + PDP_urls)
for n in range(len(urls)):
    print('<h5>%s</h5>' % urls[n])
print('<h3>Total : %d</h3>' % n)

# extract urls from PDP

# extract urls from 

# generate csv 
with open (str(file), 'wt') as wf:
    for url in urls:
        wf.write(url + '\n')
    wf.close()
print('<h3>%s generated! </h3>' % str(file))


