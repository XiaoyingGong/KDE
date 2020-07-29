# author: 龚潇颖(Xiaoying Gong)
# date： 2020/7/29 15:25  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import numpy as np

np.random.seed(1)
def standard_normal_1d(num):
    data = np.random.randn(num)
    return data

def mixture_normal_1d(num):
    data_1 = np.random.normal(0, 1, num)
    data_2 = np.random.normal(5, 2, num)
    data = np.hstack((data_1, data_2))
    return data

def normal_2d(num):
    mus = np.array([2, 2])
    sigmas = np.array([[2, 0], [0, 2]])
    return np.random.multivariate_normal(mus, sigmas, num)


def mixture_normal_2d(num):
    mus_1 = np.array([0, 0])
    sigmas_1 = np.array([[1, 0], [0, 1]])
    mus_2 = np.array([4, 4])
    sigmas_2 = np.array([[1, 0], [0, 1]])
    data_1 = np.random.multivariate_normal(mus_1, sigmas_1, num)
    data_2 = np.random.multivariate_normal(mus_2, sigmas_2, num)
    data = np.vstack((data_1, data_2))
    return data

