def swap_case(s):

    if len(s)>=0 or len(s)<=100:
        return s.swapcase()
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

