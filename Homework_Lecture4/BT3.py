months = [(31, "January"), (28, "February"), (31, "March"),
          (30, "April"), (31, "May"), (30, "June"),
          (31, "July"), (31, "August"), (30, "September"),
          (31, "October"), (30, "November"), (31, "December")]

while True:
	month = int(input('Please input a month: '))
	if month < 1 or month > 12:
		continue
	print(months[month - 1])
	back = input('Go to other month? (y/n) ')
	if back == 'y':
		continue
	break
