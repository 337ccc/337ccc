import sys
sys.stdin = open("sample.txt")

A, B, C = map(int, input().split())

if A == B == C:
    print(10000 + A * 1000)
else:
    if A == B != C:
        print(1000 + A * 100)
    elif A == C != B:
        print(1000 + A * 100)
    elif B == C != A:
        print(1000 + B * 100)
    else:
        max_num = max(A, B, C)
        print(max_num * 100)