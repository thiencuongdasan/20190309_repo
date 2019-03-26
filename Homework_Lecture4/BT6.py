a, b = 1, 1

fibonanci = [1]

while b < 1000:
	a, b = b, a + b
	fibonanci.append(a)
print(fibonanci)
