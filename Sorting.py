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
