# I added extra creativity from Line 16 to line 30.

#Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.
child_meal_price = float(input("what is The price of a child's meal? $"))
adult_meal_price = float(input("What is The price of an adult's meal? $"))

#Ask the user for the number of adults and children and store these values properly into variables as integers.
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

#Ask the user for the sales tax rate and store the value properly as a floating point number.
sales_tax_rate = float(input("What is the sales tax rate? %"))

"""Extra creativity

   the price of desert for everyone is same price
   multuplied by the total number of Adult added       to that of Children
"""

price_of_desert = float(input('what is the price of desert/person? $'))

tip_percentage = float(input("how much tip would you like to offer? %"))

#calculate the total cost of child meal and the total cost of adult meal
child_meal_total = child_meal_price * number_of_children
adult_meal_total = adult_meal_price * number_of_adults

total_number_people = number_of_children + number_of_adults

total_desert_amount = int(total_number_people) * price_of_desert

'''=============end of extra creativity========'''

#Compute and display the subtotal (don't worry about rounding to two decimals at this point).
print("\n \n")
sub_total = float(child_meal_total) + float(adult_meal_total)
print(f"Subtotal ${sub_total:.2f}")

#Compute and display the sales tax.
sales_tax = sub_total * sales_tax_rate / 100
print("Sales Tax ${:.2f}".format(sales_tax))

#The customer mught be willing to tip the waiter or waitress that served them for doing a good job so i decided to include that in the bill, even tho its optional
tip_amount = sub_total * tip_percentage / 100
print("You tiped ${:.2f}".format(tip_amount))

'''They might have taken desert before theeal was ready'''
print(f"Desert amount ${total_desert_amount}")

#Compute and display the total.
total = sub_total + sales_tax + tip_amount + total_desert_amount
print("Grand total ${:.2f}".format(total))

#Ask the user for the payment amount and store the value properly as a floating point number.
payment_amount = float(input('How much are you paying with? $'))

#Compute and display the change.
change = payment_amount - total
print("Your change is ${:.2f}".format(change))

#Include a dollar sign ($) before each displayed value.✅

#Display each value to two decimals.✅

#Double check that the calculations are correct.✅

#Show creativity and exceed the core requirements by adding additional features.✅

#Use good style in your program, including variable names and whitespace.✅