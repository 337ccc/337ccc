import sys
sys.stdin = open('sample.txt')


def min_cost(possible_days):
    cost = 0
    coupon = 0
    print(possible_days)

    # 먼저 5일권 구매
    new_possible_days = list(possible_days)
    for i in new_possible_days:
        if i in possible_days and i + 1 in possible_days and i + 2 in possible_days:
            if i + 3 in possible_days and i + 4 in possible_days:
                cost += 37000
                coupon += 2
                for j in range(i, i + 5):
                    possible_days.remove(j)
                print(i, cost, coupon)
                print(possible_days)
        else:
            continue

    # 그다음 3일권 구매
    new_possible_days = list(possible_days)
    for i in new_possible_days:
        if i in possible_days and i + 1 in possible_days and i + 2 in possible_days:
            cost += 25000
            coupon += 1
            for j in range(i, i + 3):
                possible_days.remove(j)
            print(i, cost, coupon)
            print(possible_days)
        else:
            continue

    # 마지막으로 1일권 구매
    possible_days_count = len(possible_days)
    for _ in range(possible_days_count):
        if coupon >= 3:
            coupon -= 3
        else:
            cost += 10000

    return cost


n, m = map(int, input().split())
remove_days = list(map(int, input().split()))

possible_days = set(i for i in range(1, n + 1))
for i in remove_days:
    possible_days.remove(i)

answer = min_cost(possible_days)
print(answer)