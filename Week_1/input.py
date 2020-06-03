name = input("What's your name? ")
age = float(input("How old are you? "))
#User input will always come in string value
#Use int() to convert string to integer
#best to put int() around variable assignment i.e. age = int(input(blah, blahS))

age_in_dog_years = age * 7

print(f"{name}, you are {age_in_dog_years} years old in dog years!")