import json
import urllib.request, urllib.parse, urllib.error
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
    info = json.loads(data)
    list_data = info["comments"]
    add = 0
    count = 0
    for item in list_data:
        count = count +1
        num = item["count"]
        add = add + int(num)
    print("Count: ",count)
    print("Sum: ",add)
    
        
