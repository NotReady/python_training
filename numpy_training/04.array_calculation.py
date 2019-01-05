# coding: UTF-8

# ---------------------------------------
# @note numpyの配列基礎
# 配列同士を演算できる
# a + b
# 配列要素全体に演算ができる
# ndarray + 1
# ---------------------------------------

import numpy as np

a = np.arange(6).reshape(2,3)
print(a)

# 全ての要素に対して演算

b = a + 1
print(b)

c = a * 2
print(c)

d = a ** 2
print(d)

# 全ての要素同士の演算

e = np.sum(a)
print(e)

f = np.mean(a)
print(f)

#配列同士の演算

g = np.arange(1,7).reshape(2,3)
print(g)

h = a + g
print(h)

i = a * g
print(i)