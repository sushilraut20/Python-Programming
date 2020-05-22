"""
Given an array of temperature, find out how many days next warmer days would be

input= [73,74,71,76,72,71,70,78,70]
output= [1, 2, 1, 4, 3, 2, 1, 0, 0]

"""

a=[73,74,71,76,72,71,70,78,70]
output=[]

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[j]>a[i]:
            output.append(j-i)
            break
    else:
        output.append(0)


print(output)
