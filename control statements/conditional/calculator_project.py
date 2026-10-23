num_1 = float(input('enter num 1 = '))
num_2 = float(input('enter num 2 = '))
operation = input('enter operation (+, -, *, /):  ')

if operation == '+':
 result = num_1 + num_2
 print('result =', result)
elif operation == '-':
 result = num_1-num_2
 print('result =', result)
elif operation == '*':
 result = num_1*num_2       
 print('result =', result)
elif operation == '/':
    result = num_1/num_2
    print('result =', result)
else:
    print('invalid operation')