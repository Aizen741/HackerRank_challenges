def mutate_string(s,i,c):
    string = s
    lst = list(string)
    lst[i] = c
    string = ''.join(lst)
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
