# coding: UTF-8
# ---------------------------------------
# @note numpyの配列基礎
# 配列同士を結合できる
# numpy
# .hstack([ndarray,ndarray])      配列を横方向に結合する(列追加)
# .vstack([ndarray,ndarray])      配列を縦方向に結合する(行追加)
#
# 特定行列や要素を抽出できる
# ndarray
# [[r,r],[c,c]] 特定の行列を抽出する:指定で全行列を指定
# [e%2==0]      要素に対して条件抽出
# ---------------------------------------

import numpy as np

a = np.arange(6).reshape(2,3)
print(a)

b = np.arange(6).reshape(2,3)
print(b)

# 横に結合
c = np.hstack([a,b])
print(c)

# 縦に結合
d = np.vstack([a,b])
print(d)

e = np.arange(20).reshape(4,5)
print(e)

# 行を抜き出す
f = e[[0,2],:]
print(f)

# 列を抜き出す
g = e[:,[0,2,4]]
print(g)

e[e%2==0] = 0
print(e)

