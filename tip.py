# Script to calculate how much tip to give on a bill

# Asks user to input the total of their bill
bill_input = input("How much was the bill total? ")

# Use .replace command to remove $ from user input to be able to convert string value to float
bill_amount = float(bill_input.replace('$',''))

# Next 3 lines calculate amount of tip at 15%, 18%, and 20%
tip_15 = bill_amount * 0.15
tip_18 = bill_amount * 0.18
tip_20 = bill_amount * 0.20

# Adds space in printout to make easier to read
print()

# Prints title of next section
print("Here are some recommended tip amounts!")

#Prints values of tips depending on tip percentage and bill amountS
print(f"To tip 15%, add ${tip_15:.2f} to your bill.")
print(f"To tip 18%, add ${tip_18:.2f} to your bill.")
print(f"To tip 20%, add ${tip_20:.2f} to your bill.")