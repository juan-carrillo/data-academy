def get_even_numbers_from_array(array_values):
	return [item for item in array_values if item%2 == 0]


def reorder_two_items(item_1, item_2):
	if item_1 > item_2:
		return [item_2, item_1]

	return [item_1, item_2]


def sort_array(array_values):
	new_array = [None for i in array_values]

	n_items = len(array_values)
	last_ith_idx = n_items - 1

	for ith_idx in range(n_items // 2):
		mirror_idx = abs((ith_idx + 1) - n_items)
		# print(f'{ith_idx} | {mirror_idx}')
		print('{} <> {}'.format(array_values[ith_idx], array_values[mirror_idx]))
		sorted_items = reorder_two_items(array_values[ith_idx], array_values[mirror_idx])
		print('{} \n'.format(sorted_items))
		new_array[ith_idx], new_array[mirror_idx] = sorted_items

	return new_array


class ArrayHandler(object):
	"""docstring for ClassName"""
	def __init__(self, array_like):
		self.array_like = array_like

	def __str__(self):
		return f'{self.array_like}'

	def get_array_with_reversed_order(self):
		return self.array_like[::-1]

	def find_item_index(self, item):
		for idx in range(len(self.array_like)):
			if self.array_like[idx] == item:
				return idx

		return None
				

	def find_minimum_value(self):
		desired_value = self.array_like[0]
		for item in self.array_like[1:]:
			if item < desired_value:
				desired_value = item

		return desired_value

	def find_maximum_value(self):
		desired_value = self.array_like[0]
		for item in self.array_like[1:]:
			if item > desired_value:
				desired_value = item

		return desired_value


	def get_sorted_array(self):
		new_array = sort_array(self.array_like)

		n_items = len(self.array_like)

		for ith_idx in range(n_items // 2):
			print('==================')
			print(new_array)
			new_array = sort_array(new_array)

		return new_array
		

if __name__ == '__main__':

	array_handler = ArrayHandler((0,9,1,8,2,7,3,6,4,5))
	print(array_handler)
	print('Minimum value of whole set: {}'.format(array_handler.find_minimum_value()))
	print('Maximum value of whole set: {}'.format(array_handler.find_maximum_value()))
	print('Index of value: 1 found in: {} position'.format(array_handler.find_item_index(1)))
	print('Array of even elements: {}'.format(get_even_numbers_from_array(array_handler.array_like)))

	reverse_array = array_handler.get_array_with_reversed_order()
	print(f'Original array with reversed order {reverse_array}')

	print('Sorting algorithm: {}'.format(array_handler.get_sorted_array()))

	print('End of Main method')
	