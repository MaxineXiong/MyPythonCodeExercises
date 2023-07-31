# get text content from a URL
import requests

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get('https://pythonhow.com/media/data/universe.txt', headers = headers)
c = r.content
print(c)
