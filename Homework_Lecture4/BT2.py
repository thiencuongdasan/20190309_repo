#Các biến liệt kê bên dưới nằm trong đoạn từ 1 đến 9, hỏi có bn bộ giá trị thỏa mãn điều kiện sau:
#a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 = 66
#Viết code thực hiện phép toán trên 1 cách nhanh nhất :)

#Answer1:

count = 0

for a in range(1, 10):
	for b in range(1, 10):
		for c in range(1, 10):
			for d in range(1, 10):
				for e in range(1, 10):
					for f in range(1, 10):
						for g in range(1, 10):
							for h in range(1, 10):
								for i in range(1, 10):
									if a * c * i + 13 * b * i + d * c * i + 12 * e * c * i + g * h * c == 66 * c * i + f * c * i + 11 * c * i + 10 * c * i:
										count = count + 1
print(count)
