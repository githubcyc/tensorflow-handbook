import os
os.environ['CUDA_VISIBLE_DEVICES'] = '1'
import tensorflow as tf
import numpy as np

# default for 2.0
tf.enable_eager_execution()

# 定义一个随机数（标量）0 维数组
random_float = tf.random.uniform(shape=())
print(random_float)

# 定义一个有2个元素的零向量
zero_vector = tf.zeros(shape=(2))
print(zero_vector)

np_zero = np.zeros(2)
print(zero_vector.numpy() == np_zero)

# 定义两个2×2的常量矩阵
A = tf.constant([[1., 2.], [3., 4.]])
B = tf.constant([[5., 6.], [7., 8.]])

print(A.shape)      # 输出(2, 2)，即矩阵的长和宽均为2
print(A.dtype)      # 输出<dtype: 'float32'>
np = A.numpy()
print(type(np))
