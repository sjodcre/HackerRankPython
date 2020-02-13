cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    listRet = [0]
    if n==0:
        return []
    elif n==1:
        return listRet
    else:
        listRet.append(1)
        for i in range(2,n):
            listRet.append(listRet[i-1]+listRet[i-2])
        return listRet


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))