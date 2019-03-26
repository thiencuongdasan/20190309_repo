#Chỉnh lại đoạn code sau sao cho "đúng" :)
#ss = ['python', 'patience','documents','students', 'homework', 'practice','success','english', 'university','congratulation' ]
#from string import *
#list_words = []
#for a in ss:
	#values = 0
	#for i in a:
            #value = ascii_lowercases.index(i)+1
            #values = values+value
    #list_words.append([a,values])
    
 #print( list_words )

from string import ascii_lowercase

words = ['python', 'patience','documents','students', 'homework', 'practice','success','english', 'university','congratulation' ]

list_words = []

for word in words:
	values = 0
	for char in word:
		value = ascii_lowercase.index(char) + 1
		values = values + value
	list_words.append([word, values])
    
print(list_words)