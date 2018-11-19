string = str(input("Enter a string: "))
if string == "racecar":
	print ("Good!")
string= string.replace(" ","")
string= string.replace(",","")
string= string.replace("!","")

string2 = string[::-1] #Read the string array backwards, -1 is the backwards step
#Alternate way: Use reverse
#string2 = reverse(string)

if string2 == string:
	print ("You entered a Palindrome")
else:
	print("You did not enter a Palindrome")