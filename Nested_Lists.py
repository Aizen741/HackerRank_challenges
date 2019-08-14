N = int(input())
total = []
for i in range(N):
    lst = []
    name = str(input())
    marks = float(input())
    lst.append(name)
    lst.append(marks)
    total.append(lst)

a1 = []

for i in range(len(total)):
    a1.append(total[i][1])

minimum = min(a1)

a2 = []

for i in range(len(a1)):
    if minimum != a1[i]:
        a2.append(a1[i])

a3 = min(a1)
kid = []
for i in range(len(total)):
    if a3 == total[i][1]:
        kid.append(total[i][0])
kid.sort()

for i in range(len(kid)):
    if (kid[-1]) == kid[-2]:
        print(kid[-3:])

    else:
        print(kid[-1])




