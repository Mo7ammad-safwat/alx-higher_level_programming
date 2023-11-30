#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = 0

    if len(argv) == 1:
        print(count)
    else:
        for arg in argv[1:]:
            count += int(arg)

        print(count)
