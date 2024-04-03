import sys
sys.stdin = open('sample.txt')


def min_cost(possible_days):
    cost = 0
    change_coupon = 0
    for i in range(1, 99):
        if i in possible_days:
            count = 0
            for j in range(i, i + 5):
                if j in possible_days:
                    count += 1
            if count >= 4:
                cost += 37000
                change_coupon += 2
                for j in range(i, i + 5):
                    if j in possible_days:
                        possible_days.remove(j)

            elif i in possible_days and i + 1 in possible_days and i + 2 in possible_days:
                cost += 25000
                change_coupon += 1
                for j in range(i, i + 3):
                    possible_days.remove(j)

            else:
                if change_coupon != 3:
                    cost += 10000
                possible_days.remove(i)

        else:
            if len(possible_days) == 0:
                return cost
            else:
                continue

n, m = map(int, input().split())
remove_days = list(map(int, input().split()))

possible_days = set(i for i in range(1, n + 1))
for i in remove_days:
    possible_days.remove(i)

answer = min_cost(possible_days)
print(answer)