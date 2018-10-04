""""Given a list of integers, find an index of an element, where
sum of elements to the right is exactly same as that of sum of elements to the right
 e.g. input_list=[1,9,3,0,10]
       output= 2

i.e. input_list[2]= 3 and sum(all elements to left)=10 and sum(all elements to right)=10

Note: Here 'else' to the end will get executed when break in the main body will not get executed.
     i.e. There is no such element in the list which satisfies above condition

Logic:1) Start with the middle index in the list
      2) Check sum(elements to the left) and sum(elements to the right), return index if equal
      3) if sum(elements to the left) > sum(elements to the right), decrement index and repeat step(2)
      4) if sum(elements to the left) < sum(elements to the right), increment index and repeat step(2)
"""

import math

input_list=[1,1,1,1,1,1,1,0,7]
list_length=len(input_list)

index=math.ceil(list_length/2)

while 0<=index<len(input_list):
    if(sum(input_list[:index])==sum(input_list[index+1:])):
        print("The index in List at which the sum of elements to right is exactly same as that to right is: ",index)
        break
    elif(sum(input_list[:index])>sum(input_list[index:])):
        index=index-1
    else:
        index=index+1
else: print("There is no any element in List where the given condition gets satisfied")