# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
done = False
for _ in range(x):
    n = int(input())
    arr = list(map(int, input().split()))
    # print(len(arr))
    if (arr[0]!= max(arr) and (arr[len(arr)-1]!= max(arr))):
        print('No')
    else:
        minIdx = arr.index(min(arr))
        for i in range(minIdx):
            # print(i)
            if arr[i] < arr[i+1]:
                done = True
                print('No')
                break
        for i in range(len(arr)-1,minIdx,-1):
            
            if arr[i] < arr[i-1]:
                done = True
                print('No')
                break
        if done == False:
            print('Yes')