import datetime

today = datetime.date.today()

teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    },
    'sox': {
      '2B': 'Madrigal',
      'SS': 'Anderson',
      '3B': 'Moncada',
    }
  },
  {
    'angels': {
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
]

# print all the dictionaries in the list (index, value)
#for i, v in enumerate(teams):
    #print(v['id'], v['name'])
    #print(v)
 
 
print(teams[0]['sox']['2B'])
print(teams[1]['angels']['DH'])


# https://www.geeksforgeeks.org/python-get-values-of-particular-key-in-list-of-dictionaries/
# https://www.google.com/search?q=list+comprehension+and+.get()+method+if+item+equals+value&oq=list+comprehension+and+.get()+method+if+&gs_lcrp=EgZjaHJvbWUqBwgBECEYoAEyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigATIHCAUQIRirAjIHCAYQIRirAjIHCAcQIRifBTIHCAgQIRifBTIHCAkQIRifBdIBCDMzMTRqMGo3qAIIsAIB&client=ubuntu-chr&sourceid=chrome&ie=UTF-8


# Find all players who play SS
#for team, position in teams[].items():
    #if item == ('astros')('SS'):
 #   print(team)


#for position in teams:
#   print(team_data['team'], team_data['wins'])

# works:
'''
people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}


for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
    
    for key in p_info:
        print(key + ':', p_info[key])


result = [person.get("id") for person in employees if person.get("name") == "Joe"]
print(result)
print (result[0])

print (type(result[0]))

'''

#MOngo DB data (example from tutorial) - putting into list of dictionaries
posts  = [
  {'title': "Post Title 1", 'author': "Ashley"},
  {'body': "Body of post."},
  {'category': "News"},
  {'likes': 1},
  {'tags': ["news", "events"]},
  {'date': today}
]

print(posts[0]['title'])
print(posts[0]['author'])
print(posts[4]['tags'][1])

#can also put in just one dictionary
posts2 = [{
  'title': "Post Title 1",
  'body': "Body of post 1.",
  'category': "News",
  'likes': 1,
  'tags': ["news", "events"],
  'date': today
},
{
  'title': "Post Title 2",
  'body': "Body of post 2.",
  'category': "Sports",
  'likes': 4,
  'tags': ["sports", "events"],
  'date': today
}
]
print(posts2[0]['body'])
print(posts2[1]['tags'][0])

'''
result = [person.get("id") for person in employees if person.get("name") == "Joe"]
print(result)
print (result[0])
'''

'''
values = []
for key, value in posts2.items():
    if key.startswith('a') or key.startswith('c'):
        values.append(value)
print(values)
'''

#Get other key values using list commprehension:
#res = [d['likes'] for d in posts2 if d['title'] == 'Post Title 1']
#values3 = [value for key, value in posts2.items() if key == 'title']
'''values3 = []
for key, value in posts2():
  if value == 'Post Title 1':
    values3.append(posts2['likes'])
'''

#WOW - this works, it's LIST COMPREHENSION (looks like to for loops)
output = [
    x[field] for x in posts2 for field in ['tags'] if x['title'] == 'Post Title 2'
]

print(output)