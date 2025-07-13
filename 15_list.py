
#* list(리스트)

numbers = [2, 3, 5, 7, 11, 13]
names = ["otter_1", "otter_2", "otter_3", "otter_4"]

print(numbers)
print(names)
# [2, 3, 5, 7, 11, 13]
# ['otter_1', 'otter_2', 'otter_3', 'otter_4']

#* 인덱싱
print(names[1])
# otter_2

num_1 = numbers[1]
num_3 = numbers[3]
print(num_1 + num_3)
# 10

print(numbers[-1])
# 13

#* 리스트 슬라이싱
print(numbers[0:4])
# [2, 3, 5, 7]
print(numbers[2:])
# [5, 7, 11, 13]
print(numbers[:3])
# [2, 3, 5]
new_list = numbers[:3]
print(new_list[2])
# 5

#* 지정연산자
numbers[0] = 100
print(numbers)
# [100, 3, 5, 7, 11, 13]
numbers[0] = numbers[0] + numbers[1]
print(numbers)
# [103, 3, 5, 7, 11, 13]


#! 리스트 함수
numbers = []

#* len()함수: 길이를 반환
print(len(numbers))
# 0

#* append()함수: 리스트에 내용 추가
