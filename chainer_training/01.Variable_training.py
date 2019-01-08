# coding: UTF-8

#------------------------------
# Variable
# ニューロン
#------------------------------

import chainer
import numpy as np
from chainer import Variable

# Variableのソースとなるndarrayを作成
input_array = np.array([[1,2,3],[4,5,6]], dtype=np.float32)
print(input_array)

# ndarrayをVariableオブジェクトに変換する
x = Variable(input_array)
# データ
print(x.data)

# y層を作成する
y = x ** 2
print(y.data)

# x層の微分値を求める
# y層に領域の確保が必要
y.grad = np.ones((2,3), dtype=np.float32)
y.backward()
print(x.grad)
