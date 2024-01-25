# 델타를 이용한 2차 배열 탐색
N = int(input())
# 좌우상하로 각각 얼만큼 탐색할건지
# P가 3이라면 좌우상하로 각각 3번째 칸까지 탐색함
P = int(input())

# N * N 배열
arr = [list(range(N)) for _ in range(N)]

# 좌우상하
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

for i in range(0, N):
    for j in range(0, N):
        for k in range(4):
            for m in range(1, P + 1):
                ni = i + di[k] * m
                nj = j + dj[k] * m
                if 0 <= ni < N and 0 <= nj < N:
                    print(arr[ni][nj])