'''calculating wind-chill, where T = temperature and V = speed'''

#computing the windchill
def compute_windchill(T, V):
	wind_chill = 35.74 + (0.6215 * T) - 35.75 * (V** 0.16) + (0.4275 * T) * (V**0.16)
	return wind_chill
	#converting from celsius to fahrenheit
def converting_C_to_F (Celsius_T):
	fahrenheit_T = (Celsius_T * 9/5) + 32
	return fahrenheit_T
#prompting the user for a temperature value
temperature_unit = input ("is the temperature in Celsius or Fahrenheit, c/f ? ")
#looping through the values and calling the functions
if temperature_unit.lower() == "f":
		fahrenheit_temperature = float (input ("enter temperature: "))
		
		for speed in range (5,65,5):
			wind_chill_result = compute_windchill (fahrenheit_temperature, speed)
			print()
			print(f"at {fahrenheit_temperature}F and speed {speed}mph, wind-chill is {wind_chill_result:.2f}F ")
		
elif temperature_unit.lower() == "c":
		celcius_temperature = float(input("enter temperature: "))
		
		for speed in range (5,65,5):
			convert=converting_C_to_F(celcius_temperature)
			wind_chill_result = compute_windchill (convert, speed)
			print ()
			print(f"at {convert}F and speed {speed}mph, wind-chill is {wind_chill_result:.2f}F ")
else:
	print("enter f or c only")