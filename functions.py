# Use def to start function
def greet(name):
	return f"Hey {name}!"

def concatenate(word_one, word_two):
	return word_one + word_two
def age_in_dog_years(age):
	return age * 7

# Print has to be outside function block
# Calling "Greet" in print will call back function
print(greet('Brendan'))
print(concatenate('Brendan', 'Seth'))
print(age_in_dog_years(27))
# If return is left out, function will give "none"
# Functions can only return 1 thing

#### Challenge! ####
# Create function called uppercase_reverse that will take text, uppercase all, and reverse

#Using "Slicing" to reverse string
###stringname[::-1]  Define string and use [::-1] to reverse
#str="Python" # initial string
#stringlength=len(str) # calculate length of the list
#slicedString=str[stringlength::-1] # slicing 
#print (slicedString) # print the reversed string

def uppercase_reverse(words):
	revwords = words[::-1]
	return revwords.upper()

print(uppercase_reverse('Do not go gentle into that good night'))


