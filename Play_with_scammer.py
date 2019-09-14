import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://www.nutaku.net/login/failed/?title_id=booty-calls'

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))
    #username = name.lower
    username = name.lower() + name_extra + '@yahoo.com'
    password = ''.join(random.choice(chars) for i in range(10))


    requests.post(url, allow_redirects=False, data={
		'mailAddress:': username,
		'password': password,
        'autoLogin': 0
	})

    print('sending username %s and password %s' % (username, password))

