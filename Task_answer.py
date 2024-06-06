#1
'''dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 25, 'c': 35, 'd': 40}
merged_dict = dict1.copy()
for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key]+= value
    else:
        merged_dict[key] = value
        print(merged_dict)'''


#2
'''empty_dict = {}
print(empty_dict)
'''

#3
'''about_me = {
    'name' : 'Fatih',
    'age' : 20,
    'city' : 'Baku'
}
for key, value in about_me.items():
    print(f" key : {key}, value : {value}")'''



#4
'''about_me = {
    'name' : 'Fatih',
    'age' : 20,
    'city' : 'Baku'
}
about_me.pop('age')
print(about_me)'''

#5
'''unsorted_dict = {
    'banana': 3,
    'apple': 5,
    'cherry': 2,
    'date': 4
}
sorted_dict = dict(sorted(unsorted_dict.items()))
print(sorted_dict)'''

#6
'''results_of_students = {
    'Alice': 85,
    'Bob': 90,
}
results_of_students.update({"Alice" : 95})
results_of_students.update({"Charlie" : 60})
print(results_of_students)'''

#7
'''unsorted_dict = {
    'banana': 3,
    'apple': 5,
    'cherry': 2,
    'date': 4
}
for value in unsorted_dict.values():
    print(unsorted_dict)'''

#8
item_prices = {'apple': 1.00, 'banana': 0.50}
total_price = sum(item_prices.values())
print(f"Total price of all items: ${total_price:.2f}")
discount_rate = 0.10
for item in item_prices:
    item_prices[item] *= (1 - discount_rate)

    

### Additional task 
#1
about_friend = {
    'first_name' : 'Suleyman',
    'last_name' : 'Dadashov',
    'age' : 20,
    'city' : 'Baku'
}
print(about_friend)

#2
friends_numbers = {
    'Vusal' : 7,
    'Murad' : 1,
    'Omer' : 5,
    'Aqil' : 8,
    'Subhan' : 3
}
for name, number in friends_numbers.items():
    print(f"{name}'s favorite number is {number}.")

#3
glossary = {
    'Variable': 'A container for storing data values.',
    'String': 'A sequence of characters.',
    'List': 'An ordered collection of items.',
    'Dictionary': 'A collection of key-value pairs.',
    'Function': 'A block of code that performs a specific task.'
}
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")

#4
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}
people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'mike', 'anna']
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person}, for already taking the poll!")
    else:
        print(f"{person}, please take the favorite languages poll!")

#5
pets = {
    "pet_1" : {
    'kind': 'dog',
    'owner': 'Alish'
},
    "pet_2" : {
    'kind': 'cat',
    'owner': 'Baghir'
},
    "pet_3" : {
    'kind': 'rabbit',
    'owner': 'Cavid'
},
    "pet_4" : {
    'kind': 'parrot',
    'owner': 'Davud'
},
    "pet_5" : {
    'kind': 'hamster',
    'owner': 'Elza'
 }
}        
for pet in pets:
    print(f"Kind of animal: {pet['kind']}")
    print(f"Owner: {pet['owner']}\n")

#6   
favorite_places = {
    'John': ['Paris'],
    'Mia': ['London'],
    'Liam': ['Rome']
}
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"- {place}")
    print()


#7
cities = {
    'Paris': {
        'country': 'France',
        'population': '2.16 million',
        'fact': 'Known as the "City of Light".'
    },
    'London': {
        'country': 'United Kingdom',
        'population': '8.98 million',
        'fact': 'Home to the historic Tower of London.'
    },
    'Rome': {
        'country': 'Italy',
        'population': '2.87 million',
        'fact': 'Famous for its ancient Colosseum.'
    }
}
for city, info in cities.items():
    print(f"{city}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")
    