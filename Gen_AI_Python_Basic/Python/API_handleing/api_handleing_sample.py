import json
import requests

url = 'https://jsonplaceholder.typicode.com/todos'
res = requests.get(url)

todos = json.loads(res.text)
print(todos)

for todo in todos:
    print(todo)