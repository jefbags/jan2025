import requests

my_api_key = '84G52UQAIPPMMFR4'

'''
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=84G52UQAIPPMMFR4'
r = requests.get(url)
data = r.json()

print(data)
'''

# Company Overview
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey={my_api_key}'
r = requests.get(url)
data = r.json()

print(data['DividendYield'])

div_per = float(data['DividendYield']) * 100
print (div_per)

