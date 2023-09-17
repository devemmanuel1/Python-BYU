# Your assignment is to write a program that asks the user for a temperature and
# then shows the wind chill values for various wind speeds at that temperature.

# Your program should compute and display the wind chill for wind speeds
# of 5, 10, 15, ..., 60 miles per hour, just like the National Weather Service
# chart does. To help users who are more familiar with Celsius, your
# program should allow temperature to be entered in either Celsius or
# Fahrenheit, and if needed, convert the Celsius temperature to Fahrenheit
# before using the formula.



# FORMULA = Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
#   Where,T= Air Temperature (ºF) V= Wind Speed (mph)



# Write a function to calculate and return the wind chill based on a given temperature and wind speed.
wind_speeds = 0
Decision = "C", "F"
celsius_temperature = None

# Allow the user to enter the temperature in Celsius of Fahrenheit.  
# If they provide it in Celsius, first convert it to Fahrenheit before using the formula above.
celsius_temperature  = float(input("What is the temperature? "))
Decision = input("Fahrenheit or Celsius (F/C)? ") 


def calculate_wind_chill():
    windChill = 35.74 + 0.6215 * celsius_temperature - 35.75 * wind_speeds ** 0.16 + 0.4275 * celsius_temperature * wind_speeds ** 0.16 
    return windChill

# Write a function to convert from Celsius to Fahrenheit.
# The formula for this conversion is to multiply the Celsius temperature by (9/5) and then add 32.
def convert_celsius_to_fahrenhite():
    Fahrenheit = celsius_temperature * (9 / 5) + 32
    return Fahrenheit

def calculate_converted_wind_chill():
    Fahrenheit = celsius_temperature * (9 / 5) + 32
    chill = 35.74 + 0.6215 * Fahrenheit - 35.75 * wind_speeds ** 0.16 + 0.4275 * Fahrenheit * wind_speeds ** 0.16 
    return chill

# Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, 
# and calculate and display the wind chill for each of these wind speeds.
for wind_speeds in range(5,65,5):
    if Decision.lower() == "F": 
        calculate_wind_chill()
        # Display the wind chill value to 2 decimals of precision.
        print(f"At temperature {celsius_temperature}F, and wind speed {wind_speeds} mph, the windchill is: {calculate_wind_chill():.2f}F")

    elif Decision.lower() == "C":   
        convert_celsius_to_fahrenhite()
        calculate_wind_chill()
        # Display the wind chill value to 2 decimals of precision.
        print(f"At temperature {convert_celsius_to_fahrenhite()}F, and wind speed {wind_speeds} mph, the windchill is: {calculate_converted_wind_chill():.2f}F")