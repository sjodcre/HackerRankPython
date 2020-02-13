if __name__ == '__main__':
    totalEntries = int(input())
    list = []
    for _ in range(totalEntries):
        # name = input()
        # score = float(input())
        list.append([str(input()), float(input())])
    secondLowestScore = sorted(set(x[1] for x in list))[1]
    studentsSecondLowest = sorted(x[0] for x in list if x[1]==secondLowestScore)

    print('\n'.join(studentsSecondLowest))


