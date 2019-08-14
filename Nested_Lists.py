N = int(input("number of students: "))


def students():
    for i in range(1,N+1):
        name = str(input("Name: "))
        marks = input("Marks: ")
    return[[name , marks]]
print(students())
