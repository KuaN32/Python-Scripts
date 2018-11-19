a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
'''
b = []
bound = int(raw_input("Enter a number: "))
print ("Elements printed line by line: \n")
for num in a:
	if num < bound:
		b.append(num)
		print (str(num) + "\n")
print ("Elements printed in a new list: \n")
print(b)
'''
# Written in one line of python, if number is less than 5, useful shortcut!
print ([i for i in a if i<5])
