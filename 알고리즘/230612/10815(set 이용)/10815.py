import sys
sys.stdin = open("sample.txt")

N = int(input())
# set는 중복을 허용하지 않고, 순서가 없음
# 교집합, 합집합, 차집합을 구할 때 유용함
# set를 사용하지 않을 때는 계속 시간 초과가 떴음
# https://wikidocs.net/1015 참고
my_arr = set(list(map(int, input().split())))
M = int(input())
arr = list(map(int, input().split()))

answer = []

for i in arr:
    if i in my_arr:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)