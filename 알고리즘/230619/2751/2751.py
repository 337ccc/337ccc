import sys
sys.stdin = open("sample.txt")

N = int(input())

arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()

for j in arr:
    print(j)