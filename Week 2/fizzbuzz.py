# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers that are multiples of both three and five print "FizzBuzz".

# Tip: % (modulo) tells you what's left over when you divide one number by another
# ex. number % 3 == 0

print(list(range(1,101)))

for num in range(1,101):
	if num%3 == 0 and num%5 ==0:
		print("FizzBuzz")
	elif num%3 == 0:
		print("Fizz")
	elif num%5 ==0:
		print("Buzz")

	else:
		print(num)
