import sys
sys.stdin = open("sample.txt")

arr = list(input())
total = 0
for i in arr:
    if i == 'A' or i == 'B' or i == 'C':
        total += 3
    elif i == 'D' or i == 'E' or i == 'F':
        total += 4
    elif i == 'G' or i == 'H' or i == 'I':
        total += 5
    elif i == 'J' or i == 'K' or i == 'L':
        total += 6
    elif i == 'M' or i == 'N' or i == 'O':
        total += 7
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        total += 8
    elif i == 'T' or i == 'U' or i == 'V':
        total += 9
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        total += 10

print(total)