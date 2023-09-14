import requests
from pprint import pprint

#   global variables
url = "https://jsonplaceholder.typicode.com/comments"
params = {'userId': 1, 'postId': 1}

#   connect to the API
response = requests.get(url=url, params=params)

#   where magic happens
if response.status_code == 200:
    data = response.json()
    pprint(data)
else:
    print(response.status_code)


