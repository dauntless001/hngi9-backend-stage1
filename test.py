import requests

url = 'https://hngi9.herokuapp.com/arithmetic/'
res = requests.post(url, data={})
print(res.json())