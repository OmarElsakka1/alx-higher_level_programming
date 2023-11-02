#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    sumation = 0
    count = len(argv) - 1
    for i in range(count):
        sumation += int(argv[i + 1])
    print("{}".format(sumation))
