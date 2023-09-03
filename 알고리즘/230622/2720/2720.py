import sys
sys.stdin = open("sample.txt")

T = int(input())
for i in range(T):
    answer = [0, 0, 0, 0]
    change = int(input())
    while change != 0:
        if change >= 25:
            answer[0] = change // 25
            change = change % 25
        elif 10 <= change < 25:
            answer[1] = change // 10
            change = change % 10
        elif 5 <= change < 10:
            answer[2] = change // 5
            change = change % 5
        else:
            answer[3] = change
            change = 0

    print(*answer)