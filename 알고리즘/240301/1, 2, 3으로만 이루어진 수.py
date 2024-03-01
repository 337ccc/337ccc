# n은 3 이상의 정수
# 각 자리수는 1, 2, 3으로만 이루어져 있음
# 3의 개수는 2보다 크거나 같고, 2의 개수는 1의 개수보다 크거나 같음
# 조건에 해당하는 수를 차례대로 출력
import sys
sys.stdin = open('sample.txt')

n = int(input())

for answer in range(10 ** (n - 1), 10 ** n):
    one = 0
    two = 0
    three = 0
    num = answer

    for i in range(n):
        remainder = num % 10
        num //= 10
        if remainder == 1:
            one += 1
        elif remainder == 2:
            two += 1
        elif remainder == 3:
            three += 1
        else:
            break

    if one + two + three == n:
        if one <= two and two <= three:
            print(answer)