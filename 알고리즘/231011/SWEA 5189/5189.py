import sys
sys.stdin = open('sample.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)