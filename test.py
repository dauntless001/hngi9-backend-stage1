import requests

url = 'http://hngi9.herokuapp.com/arithmetic/'
res = requests.post(url, json={'x' : 10, 'y' : 20, 'operation_type' : 'addition'})
print(res.json())