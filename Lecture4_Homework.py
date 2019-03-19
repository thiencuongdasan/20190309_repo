
###########################BT1:

#Vi?t code ki?m tra 1 string c� ph?i l� palindrome hay ko? (string d?i x?ng, vi?t xu�i hay vi?t ngu?c d?u nhu nhau, ko k? vi?t hoa hay vi?t thu?ng)

#=> Answer:

str = 'abcdefghgfedcba'

for i in range(len(str)):
        if str[i] == str[-(i + 1)]:
            i = i + 1
            if i == len(str):
                print('this is a palindrome string')
        else:
            i = i + 1
            if i == len(str):
                print('this is NOT a palindrome string')
				
				
################################BT2:

#C�c bi?n li?t k� b�n du?i n?m trong do?n t? 1 d?n 9, h?i c� bn b? gi� tr? th?a m�n di?u ki?n sau:
#a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 = 66


#=> Answer:

result = []

for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for d in range(1, 10):
                    for e in range(1, 10):
                        for f in range(1, 10):
                            for g in range(1, 10):
                                for h in range(1, 10):
                                    for i in range(1, 10):
                                        if a * c * i + 13 * b * i + d * c * i + 12 * e * c * i - f * c * i - 11 * c * i + g * h * c - 10 * c * i == 66 * c * i:
                                            result.append([a, b, c, d, e, f, g, h, i])
											
print(result)


##################################BT3:

#Nh?p 1 s? nguy�n trong do?n t? 1 d?n 12, th?c hi?n tr? v? tuple bao g?m s? ng�y v� t�n ti?ng anh tuong ?ng
#input: 1
#output: (31, "January")
#n?u nh?p ngo�i kho?ng d� th� th�ng b�o nh?p l?i, d?n khi n�o d�ng th� th�i.

#=> Answer:


while True:
        month = input('Please input a month: ')
        if month == '1':
            print('31, January')
            back = input('Go to other month? (y/n) ')
            if back == 'y':
                continue
            else:
                break
        elif month == '2':
            print('28, February')
            back = input('Go to other month? (y/n) ')
            if back == 'y':
                continue
            else:
                break
        elif month == '3':
            print('31, March')
            back = input('Go to other month? (y/n) ')
            if back == 'y':
                continue
            else:
                break
        elif month == '4':
            print('30, April')
            back = input('Go to other month? (y/n) ')
            if back == 'y':
                continue
            else:
                break
        elif month == '5':
            print('31, May')
            back = input('Go to other month? (y/n) ')
            if back == 'y':
                continue
            else:
                break
        elif month == '6':
            print('30, June')
            back = input('Go to other month? (y/n) ')
            if back == 'y':
                continue
            else:
                break
        elif month == '7':
            print('31, July')
            back = input('Go to other month? (y/n) ')
            if back == 'y':
                continue
            else:
                break
        elif month == '8':
            print('31, August')
            back = input('Go to other month? (y/n) ')
            if back == 'y':
                continue
            else:
                break
        elif month == '9':
            print('30, September')
            back = input('Go to other month? (y/n) ')
            if back == 'y':
                continue
            else:
                break
        elif month == '10':
            print('31, October')
            back = input('Go to other month? (y/n) ')
            if back == 'y':
                continue
            else:
                break
        elif month == '11':
            print('30, November')
            back = input('Go to other month? (y/n) ')
            if back == 'y':
                continue
            else:
                break
        elif month == '12':
            print('31, December')
            back = input('Go to other month? (y/n) ')
            if back == 'y':
                continue
            else:
                break
        else:
            print('\nInvalid month!\n')
            continue
			

###############################################BT4:
#Cho do?n b�i h�t sau
#Ngu60?i 'theo hu@ong' hoa 100m�y m� [giang l?i]
#L�n 25 suong kh�30i ph�i phai 90 dua bu$?c ai xa r?i 35
#100�on c#�i m99�nh ta {v?n vuong} h?i ?c tro^ng ... men say (chi?u mua) bu?80n 
#Ng~an "gi?t l?" ng?ng k2hi?n kho� mi s?u bi.1 
#l�m r� l?i b�i h�t b?ng c�ch lo?i b? to�n b? c�c s? v� k� t? puntuation :)
#puntuation l� g�?

#=> Answer:

import string

lyric = '\n- Ngu60?i \'theo hu@ong\' hoa 100m�y m� [giang l?i]\nL�n 25 suong kh�30i ph�i phai 90 dua bu$?c ai xa r?i 35\n100�on c#�i m99�nh ta {v?n vuong} h?i ?c tro^ng ... men say (chi?u mua) bu?80n \nNg~an "gi?t l?" ng?ng k2hi?n kho� mi s?u bi.1 \n'

lines = lyric.split('\n')

new_lyric = []

for line in lines:
        new_line = []
        for char in line:
            if char not in string.punctuation:
                new_line.append(char)
        new_line = ''.join(new_line)
        result = []
        for char in new_line:
            if char not in string.digits:
                result.append(char)
        result = ''.join(result)
        new_lyric.append(result.strip())
		
print('\n'.join(new_lyric))



############################################BT5:




