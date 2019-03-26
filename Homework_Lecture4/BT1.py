#Viết code kiểm tra 1 string có phải là palindrome hay ko? (string đối xứng, viết xuôi hay viết ngược đều như nhau, ko kể viết hoa hay viết thường)

data = 'AbcdeFeDCba'

palindrome = data.lower()

if palindrome == palindrome[::-1]:
	print('This is palindrome')
else:
	print('This is not palindrome')
