import sys
sys.stdin = open("sample.txt")

N = int(input())

# 일의 자리가 짝수이면 소수점 첫째 자리가 0.5라도 round 사용해도 내림 처리가 됨
# round(4.5) == 4
if round(N * 0.15) == N * 0.15 - 0.5:
    exclude = round(N * 0.15) + 1
else:
    exclude = round(N * 0.15)

lines = list(map(int, sys.stdin.readlines()))
lines.sort()

if N == 0:
    answer = 0
elif 0 < N <= 3:
    # 일의 자리가 짝수이면 소수점 첫째 자리가 0.5라도 round 사용해도 내림 처리가 됨
    # round(12.5) == 12
    if round(sum(lines) / len(lines)) == sum(lines) / len(lines) - 0.5:
        answer = round(sum(lines) / len(lines)) + 1
    else:
        answer = round(sum(lines) / len(lines))
else:
    # 제외하는 숫자의 개수로 for문을 돌렸더니 시간초과가 났음
    # 그래서 오름차순 정렬을 하고 슬라이싱을 통해 난이도 배열을 만듦
    lines = lines[exclude : N-exclude]
    if round(sum(lines) / len(lines)) == sum(lines) / len(lines) - 0.5:
        answer = round(sum(lines) / len(lines)) + 1
    else:
        answer = round(sum(lines) / len(lines))

print(answer)