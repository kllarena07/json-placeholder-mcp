# test script to see how to make a request to the JSONPlaceholder API

import requests

res = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(res.json())

# output:
# {
#   'userId': 1,
#   'id': 1,
#   'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
#   'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'
# }
