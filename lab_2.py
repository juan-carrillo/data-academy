def sum_up_two_numbers(num1, num2):
	return num1 + num2


def read_txt_file(file_path):
	file = open(file_path)
	content =  file.read()
	file.close()

	return content

def write_new_line_into_txt_file(file_path, new_content):
	file = open(file_path, 'a')
	content =  file.write('\n' + str(new_content))
	file.close()


def sum_up_array(array_values):
	sum_up = 0

	for value in array_values:
		sum_up += int(value)

	return sum_up


def calculate_mean(values):
	return sum_up_array(values) / len(values)



if __name__ == '__main__':
	array_content = read_txt_file("numbers_back.txt").split(',')
	print(f'File content: {array_content}')
	calculated_mean = calculate_mean(array_content)
	print(f'Mean: {calculated_mean}')

	write_new_line_into_txt_file('numbers.txt', 'General Kenobi')

	print(read_txt_file('numbers.txt'))

	print('End of Main method')
