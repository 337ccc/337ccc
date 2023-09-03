import sys
sys.stdin = open("sample.txt")

N = int(input())

# 메모리 초과를 해결하기 위해 0이 10,001개인 list 만듦
# 그리고 그 수에 해당하는 인덱스에 1을 더하는 방식으로 저장
arr = [0] * 10001
for i in range(N):
    num = int(sys.stdin.readline().strip())
    arr[num] += 1

# print(arr)
# [0, 2, 2, 2, 1, 2, 0, 1, 0, 0, 0, ... , 0] - num의 개수
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ..., 10,000] - num
for j in range(10001):
    if arr[j] != 0:
        for _ in range(arr[j]):
            print(j)