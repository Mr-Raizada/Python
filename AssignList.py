letters = ['a', 'b', 'c','d','e','f','g']
print(letters)
print(len(letters))
#Replaceing some values 
letters[2:5] = ['C', 'D', 'E']
print(letters)
print(len(letters))
#now removing them
letters[2:5] = []
print(letters)
print(len(letters))
#clearing the list by replacing all the elements with empty list 
letters[:] =[]
print(letters)
print(len(letters))