# 델타를 이용한 2차 배열 탐색
N = int(input())

# N * N 배열
arr = [list(range(N)) for _ in range(N)]

# 좌우상하
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

for i in range(0, N):
    for j in range(0, N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:  # 유효한 인덱스면
                print(arr[ni][nj])  # test(arr[ni][nj])