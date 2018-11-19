import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#Randomly Generate Lists
a = random.sample(range(0,30),random.randint(1,10))
b = random.sample(range(0,30),random.randint(1,10))

print ("a: " + str(a))
print ("b: " + str(b))
c = []
for elem in a:
	if elem in b and elem not in c:
		c.append(elem) 
c.sort()
print ("Elements common to list a and b: ")
print (c)

#One line of code, can't seem to remove duplicates
#print([x for x in a if x in b and x not in a[:x]])