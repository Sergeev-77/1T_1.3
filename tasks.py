def multiply(string1, string2):
    '''
    функция принимает в качестве аргументов две непустые строки, состоящие из '0' и '1',
    воспринимает  в качестве чисел в двоичной форме, перемножает их, и возвращает результат
    в двоичном виде.
    '''
    
    def _decimal(string):
        return sum([int(value) * (2**idx)  for idx, value in enumerate(string[::-1])])
    
    num = _decimal(string1) * _decimal(string2)
    answer = ''
    
    while num > 0:
        answer = str(num % 2) + answer
        num = num // 2

    print(string1, string2, answer)


multiply('111', '101')


def is_palindrom(phrase):
    '''
    функция определяет является ли аргумент фразой - палиндромом. пробелы исключаются.
    '''
    print(phrase,
       phrase.replace(' ', '') == phrase.replace(' ', '')[::-1]
    )


is_palindrom("taco cat")
is_palindrom("rotator")
is_palindrom("black cat")


def romanize(number):
    '''
    функция принимает число, записанное арабскими цифрами и возвращает его римское представление.
    работает для целых чисел в интервале от 1 от 1999
    '''
    
    if (not type(number) is int) or number < 1 or number > 1999:
        print('требуется целое число в интервале 1-1999')
        return

    _MAP = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    residuals = number
    answer = ''
    while residuals > 0:
        for i in sorted(_MAP.keys(), reverse=True):
            if residuals//i > 0:
                answer += _MAP[i]
                residuals -= i
                break
    print(answer)            


romanize(3)
romanize(9)
romanize(1945)
romanize('asdasd')
romanize(0)
romanize(1.5)
romanize(2000)


def check_brackets(string):
    '''
    функция проверяет является ли последовательность скобок валидной.
    в качестве аргумента ожидается строка из символов {}[]()
    '''
    
    _BRACKETS = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
    
    if len(string) % 2 == 1:
        print (string, False)    
        return
    
    stack = []
    answer = True
    
    for bracket in string:
        if len(stack) == 0 and bracket in _BRACKETS.keys():
            answer = False
        elif bracket in _BRACKETS.values():
            stack.append(bracket)
        else:
            answer = (stack.pop() == _BRACKETS[bracket])
        if not answer:
            break        
    print (string, answer)


check_brackets("[{}({})]")
check_brackets("{]")
check_brackets("{")
check_brackets("(())")
