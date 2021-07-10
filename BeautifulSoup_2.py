
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def urldef(url,cnt,pos) :
    for num in range(int(cnt)):
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        count = 0
        for tag in tags:
            
            if count == int(pos) :
                break
            else :
                htag = tag.get('href', None)
                content = tag.contents[0]
            count = count + 1
            
        print('Retrieving : ',htag)
        url = htag
    return content



url = input('Enter website: ')
cnt = input('Enter Count: ')
pos = input('Enter Position : ')
name = urldef(url,cnt,pos)
print(name)







 
