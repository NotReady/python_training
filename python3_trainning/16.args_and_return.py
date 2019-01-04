#coding: UTF-8

# ---------------------------------------
# @note 関数の引数と返り値
# 特になし
# ---------------------------------------

a = 3
b = 7

def add1(c, d):
    e = c + d
    print(e)

add1(a, b)

def add2(c, d):
    e = c + b
    return e

f = add2(a, b)
print(f)
