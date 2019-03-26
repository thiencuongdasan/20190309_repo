#Tạo 1 list chứa 100 phần tử ngẫu nhiên

#Viết code sinh ra 1 list mới chứa bộ n (là 1 tuple) là n phần tử liên tiếp nhau, duyệt lần lượt, các phần tử nào còn thừa ko đủ để tạo bộ n phần tử thì ko add thêm vào list

#Ví dụ:

#numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10....]  # 100 phần tử ngẫu nhiên
# output, với n = 3 là bộ 3 phần tử
#result = [(1, 3, 5), (7, 9, 2), (4, 6, 8), ...]

import random

numbers = [random.randint(1, 100) for _ in range(1, 101)]

n = 3
result = []
sub = []

for number in numbers:
	sub.append(number)
	if len(sub) == n:
		result.append(tuple(sub))
		sub = []

print(result)