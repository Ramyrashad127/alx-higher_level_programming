#!/usr/bin/python3
for i in range(97, 123):
    if i == 113 or i == 101:
        continue
    if i == 122:
        print(f"{i:c}")
        break
    else:
        print(f"{i:c}",end = '')
