import re

ADDITION = ['addition','add','sum','plus','+']
SUBTRACTION = ['subtraction','subtract','minus','-']
MULTIPLICATION = ['times','multiply','*', 'multiplication']

def translate_text(text):
    operations = ADDITION+SUBTRACTION+MULTIPLICATION
    numbers = re.findall('[0-9]+', text)
    textList = text.split()
    command = ''
    for a in textList:
        if a in operations:
            command = a
        break    
    number1 = numbers[0]
    number2 = numbers[1]
    number1 = int(number1)
    number2 = int(number2)
    return {'operation_type':command, 'x':number1, 'y':number2}
