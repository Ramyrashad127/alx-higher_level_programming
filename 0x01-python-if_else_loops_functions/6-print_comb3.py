#!/usr/bin/python3
for i in range(0, 10):
    for h in range(i, 10):
        if i == 8 and h == 9:
            print("{}{}".format(i, h))
            break
        if i == h:
            continue
        print("{}{},".format(i, h), end=' ')
