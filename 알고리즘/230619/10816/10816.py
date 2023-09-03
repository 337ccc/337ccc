import sys
sys.stdin = open("sample.txt")

from bisect import bisect_left, bisect_right

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
M = int(input())
check = list(map(int, sys.stdin.readline().split()))
answer = []
for i in check:
    num = bisect_right(arr, i) - bisect_left(arr, i)
    answer.append(num)

print(*answer)