year = 2019
month = 10
day = 29
print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")
# 오늘은 2019년 10월 29일입니다.

print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))
# 오늘은 2019년 10월 29일입니다.

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))
# 오늘은 2019년 10월 29일입니다.

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year + 1, month + 1, day + 1))
# 오늘은 2020년 11월 30일입니다.

print("-------------")

print("저는 {}, {}, {}를 좋아합니다.".format("마케팅", "코딩", "운동"))
# 저는 마케팅, 코딩, 운동를 좋아합니다.

print("저는 {1}, {0}, {2}를 좋아합니다.".format("마케팅", "코딩", "운동"))
# 저는 코딩, 마케팅, 운동를 좋아합니다.

print("-------------")

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2}입나다".format(num_1, num_2, num_1 / num_2))
# 1 나누기 3은 0.3333333333333333입나다

print("{0} 나누기 {1}은 {2:.2f}입나다".format(num_1, num_2, num_1 / num_2))
# 1 나누기 3은 0.33입나다

print("{0} 나누기 {1}은 {2:.0f}입나다".format(num_1, num_2, num_1 / num_2))
# 1 나누기 3은 0입나다


# 최근 많이 사용하는 문법
name = "otter"
age = "27"
print(f"제 이름은{name}이고 {age}살입니다.")
# 제 이름은otter이고 27살입니다.