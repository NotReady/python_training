#coding: UTF-8

# ---------------------------------------
# @note 繰り返しと条件分岐の組み合わせ
# ---------------------------------------

# range=>listに変換list(range)
a = range(0, 10)
print(list(a))

b = []
for i in a:
    if i % 2 == 0:
        b.append(i)

print(b)