Number_of_students = int(input())
d = {}
def Students():
    for i in range(Number_of_students):
        Name = str(input())
        Marks = (input())
        d[Name] = float(Marks)
    dictionary= (d)
    dictionary = sorted(dictionary.keys())
    return dictionary[-2]
print(Students())






