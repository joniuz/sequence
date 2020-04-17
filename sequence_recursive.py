# Sequence of numbers
# Every element is calculated based on the sum of the last two elements

import time

# Recursive algorithm
def sequence(position):
	if position <= 2:
		return 2
	else:
		return sequence(position-1) + sequence(position-2)

if __name__ == '__main__':
	# Main program
	try:
		# Ask to the user about the position to calculate
		position = int(input("Enter the element position: "))

		if position <= 0:
			print("\nPlease enter a positive integer.")
		else:
			# Record the initial time to calculate the execution time
			start_time = time.time()
			print("\nThe value is: " + str(sequence(position)))
			print("--- %s seconds ---" % (time.time() - start_time))

	except ValueError:
		print("\nPlease enter a valid number.")
