#List are like a compund data type , used to group together to other
#Example of the list type is 
square = [1,4,9,16,25]
#print(square)

#List are built in sequence type thus that can be sliced and indexed 
print(square[0])
#here the sequncening is from 0-1-2-3 from right and from left it will be -0--1
print(square[-0])
#-0  and 0 both are same to understand about it 
print(square[-1])
#Indexing part  
print(square[1:])
#Initials are always included and ending part is not 
print(square[-3:])
#We can concantane the list
Squares = square + [36, 49, 64, 81, 100]
print(Squares)
square.append(36)
print(square)