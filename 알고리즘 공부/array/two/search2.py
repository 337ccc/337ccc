# 델타를 이용한 2차 배열 탐색
N = int(input())

# N * N 배열
arr = [list(range(N)) for _ in range(N)]

for i in range(0, N):
    for j in range(0, N):
        # 우하좌상
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:  # 유효한 인덱스면
                print(arr[ni][nj])  # test(arr[ni][nj])