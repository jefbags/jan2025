quote = {'Global Quote1': 
         {'01. symbol': 'IBM', '02. open': '220.5500', '03. high': '223.6600', '04. low': '220.5500', 
          '05. price': '222.6500', '06. volume': '3873578', '07. latest trading day': '2025-01-03', 
          '08. previous close': '219.9400', '09. change': '2.7100', '10. change percent': '1.2322%'},
          'Global Quote2':
          {'01. symbol': 'ABC', '02. open': '220.5500', '03. high': '223.6600', '04. low': '220.5500', 
          '05. price': '222.6500', '06. volume': '3873578', '07. latest trading day': '2025-01-03', 
          '08. previous close': '219.9400', '09. change': '2.7100', '10. change percent': '1.2322%'}
          }

print (quote['Global Quote1']['01. symbol'])

# cool!
for (outer_k, outer_v) in quote.items():
    for (inner_k, inner_v) in outer_v.items():
        if inner_v == 'IBM':
            print(outer_v['05. price'])



#result = [person.get("id") for person in employees if person.get("name") == "Joe"]
#print(result)

#esult = [quote.get("05. price") for quote in quote if quote.get("01. symbol") == "IBM"]

#output = [
 #   x[field] for x in quote for field in ['05. price'] if x['01. symbol'] == 'IBM']

'''
output = [
    x[field] for x in posts2 for field in ['tags'] if x['title'] == 'Post Title 2'
]
'''

nested_dict = {'first':{'a':1}, 'second':{'b':2}}

# how to execute a nested for loop 
for (outer_k, outer_v) in nested_dict.items():
    for (inner_k, inner_v) in outer_v.items():
        if inner_k == 'a':
            print(inner_v)

# Cool to know - update values in a nested dictionary
for (outer_k, outer_v) in nested_dict.items():
    for (inner_k, inner_v) in outer_v.items():
        outer_v.update({inner_k: float(inner_v)})
nested_dict.update({outer_k:outer_v})

print(nested_dict)