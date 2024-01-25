# 0 ~ 9 사의의 숫자 카드에서 임의의 카드 6장을 뽑았을 때,
# 3장의 카드가 연속적인 번호를 갖는 경우 run이라 하고,
# 3장의 카드가 동일한 번호를 갖는 경우 triplet하고 함
# 6장의 카드가 run과 triplet으로만 구성된 경우를 baby-gin이라 함
# 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라

import sys
sys.stdin = open('sample_input.txt')

N = int(input())

for test_case in range(N):
    num = input()
    # 문자열로 입력 받은 값을 int 형식으로 다시 저장
    number = int(num)

    # 여섯 자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
    # 뒤에 0을 두 번 더 붙이는 이유는 한 번에 run과 triplet 같이 검사하기 위함
    c = [0] * 12

    for i in range(6):
        c[number % 10] += 1
        number //= 10

    # 여기까지 진행하면 baby_gin을 계산하기 위한 리스트 완성
    # ex) [0, 3, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]

    i = 0
    tri, run = 0, 0
    while i < 10:
        # triplet 조사 후, run 조사
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            run += 1
            continue
        i += 1

    answer = 0
    if tri + run == 2:
        answer += 1

    print(f'#{test_case} {answer}')
