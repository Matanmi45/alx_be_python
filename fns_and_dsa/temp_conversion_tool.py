FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    #global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    return celsius

def convert_to_fahrenheit(celsius):
    #global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 
    return fahrenheit

temp = int(input('Enter the temperature to convert: '))
temp_unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').strip().upper()

match temp_unit:
    case "F":
        celsius = convert_to_celsius(temp)
        print(f"{temp}{chr(176)}F is {celsius}{chr(176)}C")
    case "C":
        farhenheit = convert_to_fahrenheit(temp)
        print(f"{temp}\N{DEGREE SIGN}C is {farhenheit}\N{DEGREE SIGN}F")
    case _:
        print("Enter the correct letter F or C")
        #quit()
        
    

        
    
        
    

        
    

