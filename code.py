def celcius_to_fahrenheit(temp):
    formula_c = (temp * 9 / 5) + 32
    return f"{formula_c:.2f} F"

def fahrenheit_to_celcius(temp):
    formula_f = (temp - 32) * 5 / 9
    return f"{formula_f:.2f} C"

while True:
    temp = int(input("Please input the temperature: "))
    a = input("Now enter C or F: ")
    if a == 'F':
        print(fahrenheit_to_celcius(temp))
    elif a == 'C':
        print(celcius_to_fahrenheit(temp))
    b = input('Do you want to exit y/n: ')
    if b == 'y':
        break
    elif b == 'n':
        continue
