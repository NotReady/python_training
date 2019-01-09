# coding: UTF-8

#------------------------------
# optimizer
# 最適化
#------------------------------

import numpy as np
import chainer
from chainer import Variable, Chain, optimizers
import chainer.functions as F
import chainer.links as L

# モデルをクラスで実装
class MyChain(Chain):

    def __init__(self):
        super().__init__(
            # 入力層が1, 中間層が2、出力層が3
            l1 = L.Linear(1,2),
            l2 = L.Linear(2,1),
        )

    def __call__(self, x):
        # 中間層にシグモイド関数を適応
        h = F.sigmoid(self.l1(x))
        return self.l2(h)

# optimizerの設定
model = MyChain()
# 最適化アルゴリズム
# 　確率的降下法(SGD)
# 　Adam
optimizer = optimizers.SGD()
optimizer.setup(model)

# Optimizerの実行
input_array = np.array([[1]], dtype=np.float32) # 入力
answer_array = np.array([[1]], dtype=np.float32) # 正解値
x = Variable(input_array)
t = Variable(answer_array)

# modelの勾配をリセットして、出力を求める
model.cleargrads()
y = model(x)

# 出力と正解の誤差を求める
# mean_squared_error => 二乗誤差
loss = F.mean_squared_error(y, t)
print(loss.data)
loss.backward()

print(model.l1.W.data)
optimizer.update()
print(model.l1.W.data)
