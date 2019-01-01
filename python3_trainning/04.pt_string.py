#coding: UTF-8

# ---------------------------------------
# @note 文字列
# 文字列はオブジェクト
# - 乗算で繰り返し結合
# - upper(), lower()など文字列関数をサポート
# ---------------------------------------

a = "Hello"
b = "World"
c = a + b
print(c)

# 乗算で繰り返し文字列
d = a * 5
print(d)

e = a * 5 + b * 3
print(e)

f = a.upper()
print(f)

g = a.lower()
print(g)

# 減算は無い
# h = a - b
