
def true(a):
    x = "lovey"
    return x+a

y = "precious"



teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angels': {
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
]


# List of dictionaries
# https://www.scaler.com/topics/list-of-dictionaries-in-python/

# Data to be served by the API
employees = [
            {'id': 1, 'name': 'Ashley'},
            {'id': 2, 'name': 'Kate'},
            {'id': 3, 'name': 'Joe'},
            {'id': 4, 'name': 'James'},
            {'id': 5, 'name': 'Joe'}
]
#print(employees[0]['id'])
#print(employees[0]['name'])

# print all the dictionaries in the list (index, value)
for i, v in enumerate(employees):
    print(v['id'], v['name'])
 
# https://www.geeksforgeeks.org/python-get-values-of-particular-key-in-list-of-dictionaries/
# https://www.google.com/search?q=list+comprehension+and+.get()+method+if+item+equals+value&oq=list+comprehension+and+.get()+method+if+&gs_lcrp=EgZjaHJvbWUqBwgBECEYoAEyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigATIHCAUQIRirAjIHCAYQIRirAjIHCAcQIRifBTIHCAgQIRifBTIHCAkQIRifBdIBCDMzMTRqMGo3qAIIsAIB&client=ubuntu-chr&sourceid=chrome&ie=UTF-8


result = [person.get("id") for person in employees if person.get("name") == "Joe"]
print(result)
print (result[0])

print (type(result[0]))

# print specific ID from the list of dictionaries
#print (employees[3]['id'])

#for index, employee in enumerate(employees):
        #print(f"Index: {index}, Employee: {employee}")
        #print("This works - noisy, turn back on later") 

#for i in employees:
#    print(employees[i])
