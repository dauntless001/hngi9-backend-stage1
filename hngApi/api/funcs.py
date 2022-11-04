import re

ADDITION = ['addition','add','sum','plus','+', 'added']
SUBTRACTION = ['subtraction','subtract','minus','-', 'subtracted']
MULTIPLICATION = ['times','multiply','*', 'multiplication', 'multiplied']

def translate_text(text):
    operations = ADDITION+SUBTRACTION+MULTIPLICATION
    text = re.sub(r'[^\w]', ' ', text)
    numbers = re.findall('[0-9]+', text)
    # remove all symbols then split
    textList = text.split()
    command = ''
    for a in textList:
        print(a)
        if a.lower() in operations:
            command = a
    number1 = numbers[0]
    number2 = numbers[1]
    number1 = int(number1)
    number2 = int(number2)
    return {'operation_type':command, 'x':number1, 'y':number2}
