#Tính tiền điện dùng trong 1 tháng: với ít hơn 50 số điện, tính giá 15000vnd/1 số, từ số điện thứ 51 đến 200, tính giá 16500vnd/1 số, dùng lớn hơn 200 số điện thì tính giá 20000vnd/ 1 số

#Lần lượt tính tiền điện ứng với các số điện đã dùng sau: 48, 100, 150, 199, 250, 1000


price = []
numbers = [48, 100, 150, 199,250, 1000]

for i in numbers:
	if i < 50:
		expense = i * 15000
		price.append(expense)
	if i >= 50 and i <= 200:
		expense = i * 16500
		price.append(expense)
	if i > 200:
		expense = i *20000
		price.append(expense)

print(price)
