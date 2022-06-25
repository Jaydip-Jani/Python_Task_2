# initializing lists
list1 = [1, 2, 4]
list2 = [1, 3, 4]

# printing original lists
print("The original list 1 is : " + str(list1))
print("The original list 2 is : " + str(list2))

# using sorted()
# to combine two sorted lists
res = sorted(list1 + list2)

# printing result
print("The combined sorted list is : " + str(res))
