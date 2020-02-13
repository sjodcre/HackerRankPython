#!/bin/python3
import collections

class OrderedCounter(collections.Counter, collections.OrderedDict):
    pass




if __name__ == '__main__':
    # s = OrderedCounter(sorted(input()).most_common(3))
    # for x in s:
    #     print(x)
    letters = OrderedCounter(sorted(input())).most_common(3)
    [print(*letter) for letter in letters]
