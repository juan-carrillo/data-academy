num_1, num_2 = 2, 3


def is_num_1_greter_than_num_2(num1, num2, display_result=False):
	result = num1 > num2
	msg = f'{num1} is greater than {num2}' if result else f'{num1} is not greater than {num2}'
	if display_result:
		print(msg)

	return result


def is_num_1_equals_to_num_2(num1, num2):
	if num1 == num2:
		print(f'{num1} equals to {num2}')
		return True
	else:
		print(f'{num1} and {num2} are not equal')
		return False


def print_numbers_given_max_limit():
	pass


if __name__ == '__main__':
	user_number = int(input('Hi there, please type any number and hit enter: '))

	is_num_1_greter_than_num_2(user_number, 6, True)
	is_num_1_equals_to_num_2(user_number, 6)

	for i in range(1, user_number + 1):
		print(i)
		print("================================\n")
