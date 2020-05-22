"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

nums=[-1,-2,-3,-6,-8]
target=-9
first_number=0
index_list=[]


for i in nums:
    first_number=i

    if (target-first_number) not in nums[nums.index(i)+1:]:
        continue
    else:
        second_number=nums.index(target-first_number,nums.index(first_number)+1)
        index_list.append(("First number index",nums.index(first_number)))
        index_list.append(("Second Number index",second_number))

    break

print("Required list of indexes: ", index_list)
