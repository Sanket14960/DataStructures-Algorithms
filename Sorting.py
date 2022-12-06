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

#Insertion Sort Implementation 
def insertionSort(array):
	for i in range(len(array)):
		currentValue = i
		
		for k in range(0,i):
			if array[k] == array[currentValue]:
				pass
			elif array[k] < array[currentValue]:
				pass
			else:
				array[currentValue], array[k] = array[k], array[currentValue]
				
	return array

#Merge Sort Implementation 
import math
	
def mergeSort(array):
	if len(array) == 1:
		return array

	# Split Array into right and left 
	length = len(array)
	middle = math.floor(length/2)
	left = array[0:middle]
	right = array[middle:]

	return merge(
		mergeSort(left),
		mergeSort(right)
	)

def merge(left, right):
	result = []
	leftIndex = 0
	rightIndex = 0

	while leftIndex < len(left) and rightIndex < len(right):
		if left[leftIndex] < right[rightIndex]:
			result.append(left[leftIndex])
			leftIndex += 1
		else:
			result.append(right[rightIndex])
			rightIndex += 1

	return result + left[leftIndex:] + right[rightIndex:]

print(mergeSort(numbers))
