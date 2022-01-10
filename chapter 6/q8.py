def celsiusToFahrenheit(celsius):
    fahrenheit = (9/5)*celsius+32
    return fahrenheit

def FahrenheitToCelsius(fahrenheit):
    celsius = (5/9)*(fahrenheit-32)
    return celsius

def main():
    print('Celsius \tfahrenheit\t|\tFahrenheit \tCelsius')
    print()
    for i in range(0,10,1):
        cel = FahrenheitToCelsius(120-i*10)
        fah = celsiusToFahrenheit(40-i)
        print('{:3.1f} \t \t {:3.1f} \t \t| \t {:3.1f} \t \t{:3.1f}'.format(40-i,fah,120-i*10,cel))

main()