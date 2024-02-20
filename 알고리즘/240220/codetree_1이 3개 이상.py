import sys
sys.stdin = open('sample.txt')  # 답 : 4

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dir_y = [-1, 1, 0, 0]
dir_x = [0, 0, -1, 1]

count = 0
for i in range(n):
    for j in range(n):
        near = 0
        for m in range(4):
            find_y = i + dir_y[m]
            find_x = j + dir_x[m]
            if 0 <= find_y <= n - 1 and 0 <= find_x <= n - 1:
                if arr[find_y][find_x] == 1:
                    near += 1
        if near >= 3:
            count += 1

print(count)