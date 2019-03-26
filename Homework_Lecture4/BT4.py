#Cho đoạn bài hát sau
#Ngư60ời 'theo hư@ơng' hoa 100mây mù [giăng lối]
#Làn 25 sương khó30i phôi phai 90 đưa bư$ớc ai xa rồi 35
#100Đơn c#ôi m99ình ta {vấn vương} hồi ức tro^ng ... men say (chiều mưa) buồ80n 
#Ng~ăn "giọt lệ" ngừng k2hiến khoé mi sầu bi.1 
#làm rõ lời bài hát bằng cách loại bỏ toàn bộ các số và kí tự puntuation :)
#puntuation là gì?


import string

lyric = '''
Ngư60ời 'theo hư@ơng' hoa 100mây mù [giăng lối]
Làn 25 sương khó30i phôi phai 90 đưa bư$ớc ai xa rồi 35
100Đơn c#ôi m99ình ta {vấn vương} hồi ức tro^ng ... men say (chiều mưa) buồ80n 
Ng~ăn "giọt lệ" ngừng k2hiến khoé mi sầu bi.1 
'''


lines = lyric.split('\n')

for line in lines:
	new_lyric = []
	for char in line:
		if char not in string.punctuation and not char.isdigit():
			new_lyric.append(char)
	new_lyric = ''.join(new_lyric)
	print(new_lyric)
