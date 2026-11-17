# convert celsius to fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

input = int(input("Enter temperature in Celsius: "))

converted_temperature = celsius_to_fahrenheit(input)

print(f'{input} in celsius degree is equal to {converted_temperature} in fahrenheit degree.')