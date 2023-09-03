import sys
sys.stdin = open("sample.txt")

answer = 1
while answer != 0:
    A, B = map(int, sys.stdin.readline().split())
    answer = A + B
    if answer != 0:
        print(answer)