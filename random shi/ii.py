import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
data ={
    'userId':'2',
    'id':'3',
    'title':'hshs',
    'body':'hejfd',
    'msg':'hello stranger'

    }
response = requests.put(url, json=data)
print(response.status_code)
print(response.json())