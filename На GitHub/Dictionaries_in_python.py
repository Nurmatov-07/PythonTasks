person = {
    'first name': 'Jack',
    'last name': 'Brown',
    'age': '43',
    'hobbies': ['football', 'singing', 'chess'],
    'children': {'son': 'Michael', 'daughter': 'Pamela'}
    }

print(person)
print(person['age'])
print(person['hobbies'])
hobbies = person['hobbies']
print('hobbies[2]')

print(person['hobbies'][2])\

children = person['children']   
print(children['son'])

print(person['children']['son'])

person['car'] = 'Mazda'
print(person)
person['hobbies'][0] = 'basketball'
print(person)

print(person.keys())
print(person.values())
print(person.items())