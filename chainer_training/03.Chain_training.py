# coding: UTF-8

#------------------------------
# Chain
# ニューラルネットワークモデル
#------------------------------

import chainer
import numpy as np
from chainer import Variable, Chain
import chainer.links as L

# links
l1 = L.Linear(4,3)
l2 = L.Linear(3,2)

#  Chainを使わず関数でスクラッチ実装
def my_forward(x):
    h = l1(x)
    return l2(h)

# 検証
x = Variable(np.array([[1,2,3,4]], dtype=np.float32))
y = my_forward(x)
print(y.data)

# 自前クラスで実装
class MyClass():
    def __init__(self):
        self.l1 = L.Linear(4,3)
        self.l2 = L.Linear(3,2)

    def forward(self, x):
        h = self.l1(x)
        return self.l2(h)

# 検証
myClass = MyClass()
x = Variable(np.array([[1,2,3,4]], dtype=np.float32))
y = myClass.forward(x)
print(y.data)

# Chainで実装
# スーパークラスにChainを指定する
class MyChain(Chain):
    def __init__(self):
        # 引数でオブジェクトを作成
        super().__init__(
            l1 = L.Linear(4,3),
            l2 = L.Linear(3,2),
        )

    def __call__(self, x):
        h = self.l1(x)
        return self.l2(h)

myChain = MyChain()
x = Variable(np.array([[1,2,3,4]], dtype=np.float32))
y = myChain(x)
print(y.data)
