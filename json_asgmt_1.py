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
    print('Count:', len(info["comments"]))
    add = 0
    for item in info["comments"]:
        add = add + int(item["count"])
    print("Sum: ",add)
    
        
