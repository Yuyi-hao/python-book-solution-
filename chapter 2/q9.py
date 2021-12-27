# Science: wind-chill temperature

temperature = eval(input("Enter the temperature in Fahrenheit betwen -58 and 41 : "))
windSpeed = eval(input("Enter the wind speed in miles per hour : "))

windChillTemperature = 35.74+(0.6215*temperature)-(35.75*(windSpeed**0.16))+(0.4275*temperature*(windSpeed**0.16))

print('the wind chill index is {:.5f}'.format(windChillTemperature))
