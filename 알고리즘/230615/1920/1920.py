import sys
sys.stdin = open("sample.txt")

N = int(input())
# 시간초과가 계속 발생해 list 형식이 아니라 set 형식으로 만듦
arr = set(map(int, sys.stdin.readline().split()))
M = int(input())
answer = list(map(int, sys.stdin.readline().split()))

for i in answer:
    if i in arr:
        print(1)
    else:
        print(0)