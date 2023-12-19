import json
import requests


response = requests.post("http://10.13.13.254/login",
                         json={'username': "a"*1024, 'password': "1"*1024},
                         allow_redirects=False)

print(json.dumps(response.json(), indent=4))