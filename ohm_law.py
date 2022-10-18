# Ohm law image: https://bit.ly/3MDmq74
def ohm_law():
    """ohm_law calculates the voltage, current or resistance depending on the choice
    """
    print(''' \n¿What do you want to calculate? 
        1   Voltage
        2   Current
        3   Resistance
        
        ''')
    option = int(input('Select an option: '))
    while option <= 0 or option >= 4:
        print('Invalid value')
        option = int(input('Select an option: '))
    else:
        number1 = int(input('Enter the first value '))
        number2 = int(input('Enter the second value '))

        if option == 1:
            voltage = number1 * number2
            print(f'Voltage: {voltage:.2f}')
        elif option == 2:
            current = number1 / number2
            print(f'Current: {current:.2f}')
        elif option == 3:
            resistance = number1 / number2
            print(f'Resistance: {resistance:.2f}')

if __name__ == '__main__':
    ohm_law()
