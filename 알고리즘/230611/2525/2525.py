import sys
sys.stdin = open("sample.txt")

H, M = map(int, input().split())
time = int(input())

hour = time // 60
minute = time % 60

if M + minute >= 60:
    if H + hour < 23:
        finish = [H + hour + 1, M + minute - 60]
    else:
        finish = [H + hour - 23, M + minute - 60]
else:
    if H + hour < 24:
        finish = [H + hour, M + minute]
    else:
        finish = [H + hour - 24, M + minute]

print(*finish)