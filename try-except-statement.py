firstNumber = float(input('Input the first number: '))
secondNumber = float(input ('Input the second number: '))

try:
    result = firstNumber / secondNumber
    print(result)
except :
    error = sys.exc_info()[0]
    print('I am sorry something went wrong')
    print(error)
finally:
    print('I will always run')
