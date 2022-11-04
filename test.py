import requests

url = 'https://hngi9.herokuapp.com/arithmetic/'
res = requests.post(url, data={'operation_type':'the addition of certain two numbers of which the first one is 14 and the second one is 20 is?'})
print(res.json())