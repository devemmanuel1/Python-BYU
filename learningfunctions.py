import math
'''def display_regular(message):
	print(message)
def display_uppercase(message):
	print(message.upper())
def display_lowercase(message):
	print(message.lower())

message = input("what is your message ")
display_regular(message)
display_uppercase(message)
display_lowercase(message)'''

def compute_area_square(value):
	area_of_square = value **2
	return area_of_square
	
def compute_area_rectangle (value_length, value_width):
	area_of_rectangle = value_length * value_width
	return area_of_rectangle

def compute_area_circle(value_radius):
	circle_area = value_radius**2 * (math.pi)
	return circle_area
shape = " "

while shape != "quit":
	shape = input ("what shape do you have? ")
	if shape.lower() == "square":
		square_length = int(input("enter length of square: "))
		square_area = compute_area_square(square_length)
		print(f"area of the square is {square_area}cm²")
		print ()
		
	elif shape.lower() == "rectangle":
		rectangle_length = int (input("enter length of rectangle: "))
		rectangle_width = int (input("enter width of rectangle: "))
		area_rectangle = compute_area_rectangle(rectangle_length, rectangle_width)
		print(area_rectangle)
		print ()
	
	elif shape.lower() == "circle":
		circle_radius = int(input("enter radius: "))
		area_of_circle = compute_area_circle(circle_radius)
		print(f" Area of the circle is {area_of_circle:.2f} ")
		print()
		
	elif shape.lower() == "quit":
		print ()
		print("goodbye")
	
	else:
		print("shape isn't available now ")
		