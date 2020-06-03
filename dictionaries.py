# List of states

# states = ['NY', 'PA', 'CA']
# states = ['New York', 'Pennsylvania', 'California']
# states = ['New York', 'NY', 'Pennsylvania', 'PA', 'California', 'CA']

# Use curly brackets {} to create dictionary
# Value on left is Key and HAS to be string. Value on right can be any data type
states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}
print(states)

# Use square brackets to pull out Key
print(states['NY'])

# Getting "KeyError" tells you that Key is missing from Dictionary

# Using .get will return None if key is not in dict, instead of causing error
print(states.get('FL'))
print(states.get('NY'))

# Using .keys will give list of all keys
print(states.keys())

# Can use variable assignment to add to dict
states['GA'] = 'Georgia'
print(states)

# Use dicts to assign descriptions to variable
user = {'name' : 'Brendan', 'height' : '5 Feet 10 Inches'}
print(user.get('name'))

# Can put dicts in lists and lists in dicts
animal_sounds = {

   "cat": ["meow", "purr"],

   "dog": ["woof", "bark"],

   "fox": []

}
print("What sounds does a cat make?", animal_sounds.get("cat"))

#Can print entire dict by making and printing list
mattan = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}
chris = {'name': 'Chris', 'height': 68, 'shoe size': 10, 'hair': 'Brown', 'eyes': 'Brown'}
sarah = {'name': 'Sarah', 'height': 72, 'shoe size': 8, 'hair': 'Brown', 'eyes': 'Brown'}

people = [mattan, chris, sarah]
print(people)

# Can print values from keys in list using for loop
for person in people:
	print(person.get('name'), person.get('height'))