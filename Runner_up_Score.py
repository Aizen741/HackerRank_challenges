#First input
participants= (input())

#Second input
array = map(int,input().split())

#Using pass for participants
for value in participants:
    pass

#second output
# The value will be represented in form of list
Array_values = [item for item in array]

#Sorting the list which have no repeated values
x=sorted(list(set(Array_values)))

#printing second laregest value
print(x[-2])