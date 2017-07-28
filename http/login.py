# -*- coding: UTF-8 -*- 
import requests
import json
Base_Host = "http://httpbin.org/get"
headers = {'user-agent': 'my-app/0.0.1'}
payload = {'key1': 'value1', 'key2': 'value2'}
payload2 = (('key1', 'value1'), ('key1', 'value2'))
url = 'https://api.github.com/some/endpoint'
payload3 = {'some': 'data'}
r = requests.get(Base_Host, params=payload2,headers=headers)
r1 = requests.post(url, json=payload3)
print r1.url
print r1.json()
print "**********************"
print r.json(),r.status_code
print r.text
print r.url
print 


