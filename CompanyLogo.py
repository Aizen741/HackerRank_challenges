# Companylogo
import collections

string =  sorted(input().strip())
count_the_alphabets = collections.Counter(string).most_common()

count_the_alphabets = sorted(count_the_alphabets,key=lambda x:(-1 *x[1] , x[0]))

for x in range(3):
 print(count_the_alphabets[x][0], count_the_alphabets[x][1])
