#coding: UTF-8

# ---------------------------------------
# @note 比較演算子
# - 文字列同士も比較演算可能
# ---------------------------------------

a = True
b = False
print(a)
print(b)

c = 5
d = c > 4
print(d)

e = c < 4
print(e)

f = c <= 5
print(f)

g = c >= 5
print(g)

h = c == 5
print(h)

i = c != 5
print(i)

# 文字列も比較演算可能
k = "Hello"
l = "Hello"
m = k == l
print(m)

n = "Hi"
o = k == n
print(o)