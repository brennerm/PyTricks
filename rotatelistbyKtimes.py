'''We can use slice operator to rotate the list by any number of times clockwise(right rotation)
   and anti-clockwise(left rotation) both''' 

li=[1,2,3,4,5]
#k is number of times a list to be rotated
k=2
#for left rotation- anti-clockwise
li=li[k:]+li[:k]
print(li) #output: [3, 4, 5, 1, 2]

#for right rotation- clockwise
li=li[-k:]+li[:-k]
print(li) #output: [1, 2, 3, 4, 5]