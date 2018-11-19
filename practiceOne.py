import datetime
name = input("Enter your name: ")
age = int(input ("Enter your age: "))
now = datetime.datetime.now()
thisyear = now.year
yeartohundred = thisyear+ (100-age)

message = "You will be 100 years old in "+ str(yeartohundred) + "."
print (message)

repeat = int(input("Enter an integer: "))

print (repeat * message)
print ("\nMessage repeated on new lines\n")
print (repeat * (message + "\n"))