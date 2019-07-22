number_of_students = int(input())
results = {}

for i in range(number_of_students):
    a = input().split(' ')
    results[a[0]] = [float(x) for x in a[1:]]
student = input()

print("%.2f" %(sum(results[student])/len(results[student])))