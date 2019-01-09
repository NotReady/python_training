# coding: UTF-8

#------------------------------
# functions
# 関数ライブラリ
#------------------------------

import numpy as np
import chainer
from chainer import Variable, Chain
import chainer.links as L
import chainer.functions as F

sample_array = np.array([[1,2,3]], dtype=np.float32)
x = Variable(sample_array)

# ベクトルの合計
y1 = F.sum(x)
print(y1.data)
# 平均値
y2 = F.average(x)
print(y2.data)
# 最大値
y3 = F.max(x)
print(y3.data)
# シグモイド関数
y4 = F.sigmoid(x)
print(y4.data)
# ランプ関数
y5 = F.relu(x)
print(y5.data)