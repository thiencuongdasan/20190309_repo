#Với file đã tạo ra từ bài 1, làm thế nào để có 1 list chứa 10 dòng cuối (list 10 phần tử)

f = open('C:\\Python\\BT1.txt')
f1 = tuple(f)

print(f1[-10:])

