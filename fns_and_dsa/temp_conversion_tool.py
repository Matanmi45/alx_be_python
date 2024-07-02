FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    #global FAHRENHEIT_TO_CELSIUS_FACTOR
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    #global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

temp = int(input('Enter the temperature to convert: '))
temp_unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').strip().upper()

match temp_unit:
    case "F":
        celsius = convert_to_celsius(temp)
        print(f"{temp}{chr(176)}F is {celsius}")
    case "C":
        farhenheit = convert_to_fahrenheit(temp)
        print(f"{temp}\N{DEGREE SIGN}C is {farhenheit}")
    case _:
        print("Enter the correct letter F or C")
        #quit()
        
    

        
    

