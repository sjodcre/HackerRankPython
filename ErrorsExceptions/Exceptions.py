# Enter your code here. Read input from STDIN. Print output to STDOUT
ops = int(input())
for i in range(ops):
    try:
        x= list(map(int,input().split()))
        print (x[0]//x[1])
    except ZeroDivisionError as e:
        print ("Error Code:",e)
    except ValueError as e:
        print ("Error Code:",e)
    
