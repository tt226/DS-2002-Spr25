#!/usr/bin/env python3


import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
print(f"My GitHub username is: {GHUSER}")

url = 'http://api.github.com/users/{0}/events'.format(GHUSER)

print(url)

r = json.loads(requests.get(url).text)

for x in r[:5]:
    event = x['type'] + ' :: ' + x['repo']['name']
    print(event)

print(r)
