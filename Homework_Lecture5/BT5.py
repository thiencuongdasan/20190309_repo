#Với 2 list:
#L1 = [1, 2, 3, 4, 5, 6]
#L2 = [3, 4, 5, 6, 7, 8, 9, 10]
#Lấy các phần tử:

L1 = [1, 2, 3, 4, 5, 6]
L2 = [3, 4, 5, 6, 7, 8, 9, 10]


#Có trong cả A, B
A = set(L1)
B = set(L2)

C = A.union(B)
print(C)

#Chỉ có trong A
D = A.difference(B)
print(D)

#Chỉ có trong B
E = B.difference(A)

print(E)

#Không có trong cả A và B
F = A.symmetric_difference(B)
print(F)

