
op = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
}



def calculate(arg):

	# stack for calculator
	stack = []

	# tokenize input
	tokens = arg.split()

	# provess tokens 
	while len(stack) > 1:
		try: 
			value = int(token)
			stack.append(value)
		except ValueError:
			val2 = int(stack.pop())
			val1 = int(stack.pop())
			#look up function in table
			func = op[token]
			result = func(val1, val2)

			stack.append(result)

			return stack[0]


def main():
	while True:
		result = calculate(input('rpn calc> '))
		print(result)



if __name__ == '__main__':
	main()