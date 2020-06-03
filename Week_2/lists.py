the_count = [1, 2, 3, 4, 5]
stocks = ["AAPL", "GOOG", "TSLA"]
random_things = ["Puppies", 55, "Anthony Weiner", 1/2, ["Oh no", "A list inside a list"]]

# this for-loop goes through a list
for number in the_count:
	print("This is count", number)

# same as above
for stock in stocks:
	print("Stock ticker:", stock)


# Y has to be a list that already exists. X is new variable assignment from existing list
# for x in y:

# we can go trhough mixed lists too
# I called it i (short for item) since I don't know what is in it

for i in random_things:
	print("Here's a random thing:", i)

# we can build lists too
people = []

people.append("Mattan")
people.append("Sarah")
people.append("Chris")

# print list
print(people)

# remove from list
people.remove("Sarah")
print(people)

for person in people:
	print("person is:", person)

# to do math inside print and print square of each value in list
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use list and range command to create list between range of numbers
for n in range(1,11):
	print(n, "squared is", n*n)

print(list(range(1,11)))

# How to access elements of a list
animals = ['bear', 'tiger', 'penguin', 'zebra']

first_animal = animals[0]
third_animal = animals[2]
print(first_animal)
print(third_animal)

print("There are this many animals", len(animals))
print("The variable Animals is a", type(animals))

#Using -1 gives last element in list
print(animals)
print(animals[-1])