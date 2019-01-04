#coding: UTF-8

# ---------------------------------------
# @note for
# - foreach風
# - 式　for i in range:
# ---------------------------------------

a = [1,2,3,4,5]

for i in a:
    print(i)

# rangeオブジェクト
for i in range(1,6):
    print(i)

for i in range(1, 6):
    j = i * 2
    print(j)

b = ["Taro", 1985, 0.125, True]
print(b)

for i in b:
    print(i)