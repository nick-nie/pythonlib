import cgi
from bs4 import BeautifulSoup
import urllib2
import ssl
import pathlib

print 'Content-type: text/html\n\n'
print '<H3>URL Extractor</H3>'
print 
form = cgi.FieldStorage()

protocol = form['protocol'].value
host = form['host'].value
port = form['port'].value
pattern = form['pattern'].value
dir = form['dir'].value
file = form['file'].value

url = str(protocol + '://' + host + ':' + port + dir) # write the url here
print 
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
usock = urllib2.urlopen(url, context=gcontext)
data = usock.read()
usock.close()
soup = BeautifulSoup(data, 'html.parser')

with open(str(file), 'wt') as wf:
    for link in soup.find_all('a'):
        tmp = str(link.get('href'))
        if tmp.startswith(pattern): 
	    print '%s<br>' % tmp
	    wf.write(tmp + '\n')
    wf.close()
fileUrl = pathlib.Path(file).as_uri()
print '<H3>URL generated in <a href = fileUrl>%s</a></H3>' % fileUrl

