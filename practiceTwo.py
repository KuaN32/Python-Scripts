print ("Part One\n")
number = int(input("Enter a number: "))
if number % 2 == 0:
	print ("Even")
	if number % 4 == 0:
		print ("Divisible by 4") 
else:
	print ("Odd\n\n") 
print ("Part Two\n")

num = int(input("Enter Number to be divided: "))
check = int(input("Enter Number to be divided by: "))

if num%check == 0:
		print (str(num) + " is divisible by " + str(check))
else:
		print (str(num) + " is NOT divisible by " + str(check))