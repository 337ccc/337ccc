import sys
sys.stdin = open("sample.txt")

T = int(input())
for _ in range(T):
    arr = list(map(int, sys.stdin.readline().split()))
    N = arr[0]
    scores = arr[1 : N + 2]
    average = sum(scores) / N
    count = 0
    for i in scores:
        if i > average:
            count += 1
    answer = (count / N) * 100
    print('{:.3f}%'.format(answer))