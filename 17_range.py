
#* range(start, stop)
#? start ~ stop-1

for i in range(3, 11):
    print(i)
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

print("------------")

#* range(stop)
#? 0 ~ stop-1

for i in range(10):
    print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

print("-------------")

#* range(start, stop, step)
#? start ~ stop-1, 간격: step

for i in range(3, 17, 3):
    print(i)
# 3
# 6
# 9
# 12
# 15

