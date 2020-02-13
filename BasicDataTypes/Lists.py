if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        text = input().split(' ')
        command = text[0]
        values = text[1:]
        if command == 'print':
            print(list)
        else:
            execute = 'list.' + command + "(" +  ",".join(values) + ")"
            eval(execute)

