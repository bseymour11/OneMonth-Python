# Strings are text surrounded by quotes
# Both single (') or double (") or triple (""") quotes are used
# examples: "dinosaurs", '2112', "I'm lovin' it!"

kanye_quote1 = "my greatest pain in live is that I will never be able to see myself perform live"

print(kanye_quote1) 

#To separate lines in string, use """S
kanye_quote2 = """My greatest pain in life
is that I will never be able
to see myself perform live."""

print(kanye_quote2) 

print()

# Using \ before quotes will let 2nd quotes be interpreted as string valuesS
hamilton_quote1 = "Well, the word got around, they said, \"This kid's insane, man\""

print(hamilton_quote1)

#Using triple quotes work too
hamilton_quote2 = """Well, the word got around, they said, "This kid's insane, man"""

print(hamilton_quote2)

print()
print()

name = "Brendan Seymour"
orphan_fee = 200
teddy_bear_fee = 121.80

total = orphan_fee + teddy_bear_fee

# Using f and {} will make varible not part of string, and input variable instead
# To Round variable use :.2f in {} with variable
print(f"{name} the total will be {total:.2f}")
