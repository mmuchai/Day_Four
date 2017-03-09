def find_missing(array_one, array_two):
	the_difference = set(array_one) ^ set(array_two)
	if (array_one and array_two) == [ ]:
		return 0
	elif array_one == array_two:
		return 0
	else:
		return (list(the_difference) [0])