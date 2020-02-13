n = int(input())
s = set(map(int, input().split()))
noCom = int(input())

for i in range(noCom):
    text = input().split(' ')
    command = text[0]
    value = text[1:]
    execute = 's.' + command + "(" +  ",".join(value) + ")"
    eval(execute)
print(sum(s))
