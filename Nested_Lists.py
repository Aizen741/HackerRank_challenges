from typing import Dict, Any

Number_of_students = int(input())
d = {}
def Students():
    global Name
    global Marks
    for i in range(Number_of_students):
        Name = str(input())
        Marks = (input())
        d[Name] = float(Marks)
    dictionary: dict[Name, Marks] = (d)

    value = sorted(dictionary , key=dictionary.__getitem__)
    for i in value:
        if value.key[1] == value.key[2]:
            return value[1]

        else:
            return i in value[1] , value[2]





    return sortedvalue

print(Students())






