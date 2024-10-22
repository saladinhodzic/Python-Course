# objects or dictionary in python

json={
    'bug':'mouse'
}

print(json['bug'])

# setting new value into the object
json['something']='something'

# looping through objects will only loop through the keys

for thing in json:
    print(thing)