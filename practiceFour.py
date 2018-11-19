number = int(input("Enter a number: "))
'''
x = range(1,number+1) #List of numbers from 1 to the input
y = []
for element in x:
	if number % element == 0:
		y.append(element)
print (y)
'''
#Lines 2-7 all in one Line
print ([y for y in range(1,number+1) if number % y == 0])