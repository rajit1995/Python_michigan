import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    data_read = data.decode()
    stuff = ET.fromstring(data_read)
    lst = stuff.findall('comments/comment')
    print('Count: ',len(lst))
    add = 0
    for item in lst:
        
        add = add + int(item.find('count').text)
    print('Sum : ',add)
        
