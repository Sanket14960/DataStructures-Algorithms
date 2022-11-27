def fibonacciIterativeHash(n):
	sequence={}

	if n == 0 or n == 1:
		return None 

	for i in range(0, n):

		if i == 0:
			sequence.update({0:0})
		elif i == 1:
			sequence.update({1:1})
			sequence.update({2:1})
		else:
			i +=1
			add = sequence.get(i-2) + sequence.get(i-1)
			sequence.update({i:add})

	return sequence[n]

def fibonacciIterativeArray(n):
	sequence = []
	for i in range(0, n):
		if i == 0:
			sequence.append(i)
		elif i == 1:
			sequence.append(i)
			sequence.append(i)
		else:
			i+=1
			sequence.append(sequence[i-2] + sequence[i-1])

	print(sequence)
	return sequence[n]

def fibonacciIterativeRecursive(n):
	
	if n <= 1:
		return n

	a = fibonacciIterativeRecursive(n - 2)
	b = fibonacciIterativeRecursive(n - 1)

	return a + b 
