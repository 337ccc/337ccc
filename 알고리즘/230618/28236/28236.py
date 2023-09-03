import sys
sys.stdin = open("sample.txt")

# n = 층 수, m = 교실의 수, k = 참가하는 반의 수
n, m, k = map(int, input().split())

min_time = (n - 1) + m
answer = 0
for i in range(k):
    floor, room = map(int, sys.stdin.readline().split())
    time = (floor - 1) + (m - room + 1)
    if min_time > time:
        min_time = time
        answer = i + 1
    elif min_time == time:
        if answer == 0:
            answer = i + 1

print(answer)