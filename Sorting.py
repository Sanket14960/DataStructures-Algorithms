numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

#Bubble Sort Implementation
def bubbleSort(array):
	for i in range(len(array) - 1):
		for k in range(len(array) - 1):
		
			greater = None
			lower = None
			
			if numbers[k] > array [k+1]:
				greater = array[k]
				lower = array [k+1]
				array[k] = lower
				array[k+1] = greater
			else:
				pass
	
	return array

#Selection Sort Implementation
def selectionSort(array):

	for i in range(len(array)):
		currentMinIndex = i
		for k in range(i, len(array)):
			if array[k] < array[currentMinIndex]:
				currentMinIndex = k

		array[i], array[currentMinIndex] = array[currentMinIndex], array[i]

	return array
