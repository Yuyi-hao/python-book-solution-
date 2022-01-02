# Science: wind-chill temperature

temperature = eval(input("Enter the temperature in Fahrenheit betwen -58 and 41 : "))
windSpeed = eval(input("Enter the wind speed in miles per hour : "))

if  (temperature > 41 or temperature < -58) and windSpeed >2 :
    print("Wrong input for both temperature and wind speed")
elif windSpeed > 2:
    print("Invalid input for wind speed")
elif temperature > 41 or temperature < -58 :
    print("Invalid input for temperature")
else: 
    windChillTemperature = 35.74+(0.6215*temperature)-(35.75*(windSpeed**0.16))+(0.4275*temperature*(windSpeed**0.16))

    print('the wind chill index is {:.5f}'.format(windChillTemperature))
