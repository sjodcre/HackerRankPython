def wrapper(f):
    def fun(l):
        k=[]
        for i in l:
            lastFive = i[-5:]
            middleFive = i[len(i)-10:len(i)-5]
            i = "+91 "+middleFive+ " " + lastFive
            k.append(i)

        return f(k)
        # complete the function
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


