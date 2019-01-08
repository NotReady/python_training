# coding: UTF-8

#------------------------------
# links
# 重み、バイアス
#------------------------------

import chainer
import numpy as np
from chainer import Variable
import chainer.links as L

# 入力に係数をかけたものと、バイアスを全て足し合わせたオブジェクトl
# 3つの入力(x)と2の出力(y)のリンクモデルを作成する
l = L.Linear(3, 2)
print(l.W.data)
print(l.b.data)

# オブジェクトlでyを計算する
# 入力が3つなので、3要素の入力配列を用意する
# input_array = np.array([[1, 2, 3]], dtype=np.float32)
input_array = np.array([[1,2,3],[4,5,6]], dtype=np.float32)
x = Variable(input_array)

# y.data[0][0] =
# x[0] * l.W.data[0][0] +
# x[1] * l.W.data[0][1] +
# x[2] * l.W.data[0][2] +
# l.d.data[0][0]
# y.data[0][1] =
# x[0] * l.W.data[1][0] +
# x[1] * l.W.data[1][1] +
# x[2] * l.W.data[1][2] +
# l.d.data[1][0]
y = l(x)
print(y.data)

#-----------
# 微分の計算
#-----------

# lの勾配を0クリアする
l.cleargrads()

# y->lと遡って微分値を計算
# y.grad = np.ones((1,2), dtype=np.float32)
# np.ones((row,col)) => 1初期化したrow行、col列の配列
y.grad = np.ones((2,2), dtype=np.float32)
y.backward()
print(l.W.grad) # 係数の微分値
print(l.b.grad) # バイアスの微分値



