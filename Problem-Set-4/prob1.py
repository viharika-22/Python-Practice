'''There is a list which comprises of quantity of ingredients to be bought for a recipe given by [2,3,4,12,4,7,8,1].
 But the guy bought had - [2,4,1,7,5,9,2,5]. Find which ingredient was bought in scare and what ingredient was bought more.
l1=[2,3,4,12,4,7,8,1]
l2=[2,4,1,7,5,9,2,5]
g=[]
l=[]
for i in range(len(l1)):
    if l1[i]>l2[i]:
        g.append(l1[i]-l2[i])
    elif l1[i]<l2[i]:
        l.append(l2[i]-l1[i])
    else:
        continue
print(max(g))
print(min(l))
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))
    location = js['results'][0]['place_id']
    print(location)'''
import urllib.request as ur
import json

url = input("Enter location: ")
print("Retrieving ", url)
data = ur.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

sum = 0
total = 0

for comment in json_obj["comments"]:
    sum += int(comment["count"])
    total += 1

print('Count:', total)
print('Sum:', sum)
