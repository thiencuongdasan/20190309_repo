f = open('C:\\Python\\BT1.txt', 'w+')

for line in range(1, 301):
	if line % 15 == 0:
		f.write('FizzBuzz\n')
	elif line % 3 == 0:
		f.write('Buzz\n')
	elif line % 5 == 0:
		f.write('Fizz\n')
	else:
		f.write(str(line) + '\n')

f.close()

