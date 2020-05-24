n = int(input())
marksheet = []
score = []
for i in range(n):
    name = input()
    scored = float(input())
    marksheet += [[name,scored]]
    score += [scored]

x = sorted(set(score))[1]

for k , v in sorted(marksheet):
    if v == x:
        print((k))
