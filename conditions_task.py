# Enter the first number: 4
# Enter the second number: 6
# Choose the operation (+, -, /, *):*
# The answer is 24
while True:
	number1 = input('Enter the first number: ')
	if number1.isnumeric():
		number1 = int(number1)
		break
while True:
	number2 = input('Enter the second number: ')
	if number2.isnumeric():
		number2 = int(number2)
		break

op = input('Choose the operation (+, -, /, *): ')
if op == '+':
	answer = number1 + number2
	print('The answer is %d' % (answer))

elif op == '-':
	answer = number1 - number2
	print('The answer is %d' % (answer))

elif op == '/':
	answer = float(number1) / number2
	print('The answer is %f' % (answer))

elif op == '*':
	answer = number1 * number2
	print('The answer is %d' % (answer))
else:
	print('Operation is not valid.')
