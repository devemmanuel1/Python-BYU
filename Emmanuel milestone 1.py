#Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.
child_meal_price = float(input("what is The price of a child's meal? $"))
adult_meal_price = float(input("What is The price of an adult's meal? $"))


#Ask the user for the number of adults and children and store these values properly into variables as integers.
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))


#Ask the user for the sales tax rate and store the value properly as a floating point number.
sales_tax_rate = float(input("What is the sales tax rate? $"))


#extra creativity
tip_percentage = float(input("how many percent of the bill would you like to tip? "))


#calculate the total cost of child meal and the total cost of adukt meal
child_meal_total = child_meal_price * number_of_children
adult_meal_total = adult_meal_price * number_of_adults


#Compute and display the subtotal (don't worry about rounding to two decimals at this point).
print("\n \n")
sub_total = float(child_meal_total) + float(adult_meal_total)
print(f"Subtotal  {sub_total}")