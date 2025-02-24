""" 
Author: Oghenefejiro Edjemere
Purpose: write a program that asks the user for a temperature and 
then show the wind chill values for various wind speeds at that temperature."""

# Function to convert celcius to fahrenheit
def convert_celcius_to_fahrenheit(celcius, value):
    return celcius + value

# Function to calculate windchill
def calculate_wind_chill(temperature, windspeed, value1, value2, value3, value4):
    return value1 + value4 * temperature - value2 * windspeed + value3 * temperature * windspeed

your_temperature = float(input("What is the temperature? "))
type = input("Fahrenheit or Celcius (F/C)? ")
type = type.lower()

# Convert celcius to fahrenheit and calculate windchill
if type == "c":
    celcius = (your_temperature * 9/5)
    value = 32
    temperature = convert_celcius_to_fahrenheit(celcius, value)
    windspeed = (5**0.16)
    value1 = 35.74
    value2 = 35.75
    value3 = 0.4275
    value4 = 0.6215
    windchill = calculate_wind_chill(temperature, windspeed, value1, value2, value3, value4) 
    print(f"At temperatre {temperature}F, and wind speed 5 mph, the windchill is: {windchill:.2f}F")
    
    windspeed1 = (10**0.16)
    windchill1 = calculate_wind_chill(temperature, windspeed1, value1, value2, value3, value4) 
    print(f"At temperatre {temperature}F, and wind speed 10 mph, the windchill is: {windchill1:.2f}F")

    windspeed2 = (15**0.16)
    windchill2 = calculate_wind_chill(temperature, windspeed2, value1, value2, value3, value4) 
    print(f"At temperatre {temperature}F, and wind speed 15 mph, the windchill is: {windchill2:.2f}F")

    windspeed3 = (20**0.16)
    windchill3 = calculate_wind_chill(temperature, windspeed3, value1, value2, value3, value4) 
    print(f"At temperatre {temperature}F, and wind speed 20 mph, the windchill is: {windchill3:.2f}F")

    windspeed4 = (25**0.16)
    windchill4 = calculate_wind_chill(temperature, windspeed4, value1, value2, value3, value4) 
    print(f"At temperatre {temperature}F, and wind speed 25 mph, the windchill is: {windchill4:.2f}F")

    windspeed5 = (30**0.16)
    windchill5 = calculate_wind_chill(temperature, windspeed5, value1, value2, value3, value4) 
    print(f"At temperatre {temperature}F, and wind speed 30 mph, the windchill is: {windchill5:.2f}F")

    windspeed6 = (35**0.16)
    windchill6 = calculate_wind_chill(temperature, windspeed6, value1, value2, value3, value4) 
    print(f"At temperatre {temperature}F, and wind speed 35 mph, the windchill is: {windchill6:.2f}F")

    windspeed7 = (40**0.16)
    windchill7 = calculate_wind_chill(temperature, windspeed7, value1, value2, value3, value4) 
    print(f"At temperatre {temperature}F, and wind speed 40 mph, the windchill is: {windchill7:.2f}F")

    windspeed8 = (45**0.16)
    windchill8 = calculate_wind_chill(temperature, windspeed8, value1, value2, value3, value4) 
    print(f"At temperatre {temperature}F, and wind speed 45 mph, the windchill is: {windchill8:.2f}F")

    windspeed9 = (50**0.16)
    windchill9 = calculate_wind_chill(temperature, windspeed9, value1, value2, value3, value4) 
    print(f"At temperatre {temperature}F, and wind speed 50 mph, the windchill is: {windchill9:.2f}F")

    windspeed10 = (55**0.16)
    windchill10 = calculate_wind_chill(temperature, windspeed10, value1, value2, value3, value4) 
    print(f"At temperatre {temperature}F, and wind speed 55 mph, the windchill is: {windchill10:.2f}F")

    windspeed11 = (60**0.16)
    windchill11 = calculate_wind_chill(temperature, windspeed11, value1, value2, value3, value4) 
    print(f"At temperatre {temperature}F, and wind speed 60 mph, the windchill is: {windchill11:.2f}F")

# Calculate windchill using fahrenheit
if type == "f":
    windspeed_5 = (5**0.16)
    value1 = 35.74
    value2 = 35.75
    value3 = 0.4275
    value4 = 0.6215
    windchill = calculate_wind_chill(your_temperature, windspeed_5, value1, value2, value3, value4) 
    print(f"At temperatre {your_temperature}F, and wind speed 5 mph, the windchill is: {windchill:.2f}F")
    
    windspeed_10 = (10**0.16)
    windchill_10 = calculate_wind_chill(your_temperature, windspeed_10, value1, value2, value3, value4) 
    print(f"At temperatre {your_temperature}F, and wind speed 10 mph, the windchill is: {windchill_10:.2f}F")

    windspeed_15 = (15**0.16)
    windchill_15 = calculate_wind_chill(your_temperature, windspeed_15, value1, value2, value3, value4) 
    print(f"At temperatre {your_temperature}F, and wind speed 15 mph, the windchill is: {windchill_15:.2f}F")

    windspeed_20 = (20**0.16)
    windchill_20 = calculate_wind_chill(your_temperature, windspeed_20, value1, value2, value3, value4) 
    print(f"At temperatre {your_temperature}F, and wind speed 20 mph, the windchill is: {windchill_20:.2f}F")

    windspeed_25 = (25**0.16)
    windchill_25 = calculate_wind_chill(your_temperature, windspeed_25, value1, value2, value3, value4) 
    print(f"At temperatre {your_temperature}F, and wind speed 25 mph, the windchill is: {windchill_25:.2f}F")

    windspeed_30 = (30**0.16)
    windchill_30 = calculate_wind_chill(your_temperature, windspeed_30, value1, value2, value3, value4) 
    print(f"At temperatre {your_temperature}F, and wind speed 30 mph, the windchill is: {windchill_30:.2f}F")

    windspeed_35 = (35**0.16)
    windchill_35 = calculate_wind_chill(your_temperature, windspeed_35, value1, value2, value3, value4) 
    print(f"At temperatre {your_temperature}F, and wind speed 35 mph, the windchill is: {windchill_35:.2f}F")

    windspeed_40 = (40**0.16)
    windchill_40 = calculate_wind_chill(your_temperature, windspeed_40, value1, value2, value3, value4) 
    print(f"At temperatre {your_temperature}F, and wind speed 40 mph, the windchill is: {windchill_40:.2f}F")

    windspeed_45 = (45**0.16)
    windchill_45 = calculate_wind_chill(your_temperature, windspeed_45, value1, value2, value3, value4) 
    print(f"At temperatre {your_temperature}F, and wind speed 45 mph, the windchill is: {windchill_45:.2f}F")

    windspeed_50 = (50**0.16)
    windchill_50 = calculate_wind_chill(your_temperature, windspeed_50, value1, value2, value3, value4) 
    print(f"At temperatre {your_temperature}F, and wind speed 50 mph, the windchill is: {windchill_50:.2f}F")

    windspeed_55 = (55**0.16)
    windchill_55 = calculate_wind_chill(your_temperature, windspeed_55, value1, value2, value3, value4) 
    print(f"At temperatre {your_temperature}F, and wind speed 55 mph, the windchill is: {windchill_55:.2f}F")

    windspeed_60 = (60**0.16)
    windchill_60 = calculate_wind_chill(your_temperature, windspeed_60, value1, value2, value3, value4) 
    print(f"At temperatre {your_temperature}F, and wind speed 60 mph, the windchill is: {windchill_60:.2f}F")










