#Viết code sinh các số nguyên tố dưới 10000, lưu giữ kq vào 1 list.
#so nguyen to: so chi chia het cho 1 va chinh no, ko co so 1, co ca so 2

number = list(range(2, 1001))

result = []

for num in number:
	for i in range(2, 501):
		if num % i != 0:
			result.append(num)
			break

print(result)


