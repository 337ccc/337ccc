import sys
sys.stdin = open("sample.txt")

total_grade = 0
total = 0
arr = {"A+" : 4.5, "A0" : 4, "B+" : 3.5, "B0" : 3, "C+" : 2.5,
       "C0" : 2, "D+" : 1.5, "D0" : 1, "F" : 0}

for test_case in range(20):
    name, grade, rating = input().split()
    grade = float(grade)
    if rating == "P":
        pass
    else:
        total_grade += grade
        total += grade * arr.get(rating)

answer = total / total_grade
print("{:.6f}".format(answer))  # 3.284483