# coding: UTF-8

import numpy as np

a = np.arange(42).reshape(6,7)
# 行列モデルを取得
print(np.shape(a))
# 要素数を取得
print(np.size(a))

(row, col) = np.shape(a)
print(row)
print(col)

# 要素が全て0の配列を作成する
b = np.zeros(10)
print("np.zeros:" + str(b))

# 要素が全て1の配列を作成する
c = np.ones(10)
print("np.ones:" + str(c))

# 乱数
d = np.random.rand(10)
print("np.random.rand:" + str(d))

# レンジをシャッフルした配列を作成する
e = np.random.permutation(range(10))
print("np.random.permutation" + str(e))