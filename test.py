# test script to see how to make a request to the JSONPlaceholder API

import requests

res = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(res.json())
