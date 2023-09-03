import sys
sys.stdin = open("sample.txt")

# 3장의 색종이의 총 면적을 구하는 문제
# 겹치는 부분도 있기에 어떻게 풀어야 하나 많이 고민함
# 색종이가 존재하는 부분은 1, 색종이가 존재하지 않는 부분은 0
N = int(input())

arr = [[0] * 101 for _ in range(101)]

for n in range(N):
    col, row = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[col + i][row + j] = 1

count = 0
for c in range(101):
    for r in range(101):
        if arr[c][r] == 1:
            count += 1

print(count)