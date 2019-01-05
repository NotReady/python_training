# coding: UTF-8

# ---------------------------------------
# @note numpyの配列基礎
# 型はndarray
# numpy.array(list)          list型からndarrayを作成する
# numpy.arange(iRange)       整数値のステップ値でndarrayを作成する
# ndarray.reshape(row, column, z) 多次元配列に再構成する
# ---------------------------------------

import numpy as np

# listから構成する
a = np.array(list(range(0, 10)))
print(a)

# 整数のステップ値で構成する
b = np.arange(10)
print(b)

c = np.array([[0,1,2], [3,4,5]])
print(c)

# 2行3列モデルに再構成する
d = np.arange(6).reshape(2,3)
print(d)

# 3行2列モデルに再構成する
e = np.arange(6).reshape(3,2)
print(e)

# 2行3列2段モデルに再構成する
f = np.arange(12).reshape(2,3,2)
print(f)