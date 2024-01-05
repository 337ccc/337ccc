import sys
sys.stdin = open("sample.txt")

#1 7
#2 6
#3 13

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 방의 가로 길이
    arr = list(map(int, input().split()))
    maxFall = 0  # 최고 낙차
    fall = 0  # 낙차

    for i in range(N):
        box = arr[i]
        for j in range(i, N):
            if box > arr[j]:
                fall += 1
        if fall > maxFall:
            maxFall = fall
        fall = 0

    print(f'#{test_case} {maxFall}')