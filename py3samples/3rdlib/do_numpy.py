# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         do_numpy
# Description:
# Author:       Administrator
# Date:         2021/12/9
# desc: Copyright © Administrator All rights reserved.
# -------------------------------------------------------------------------------

import sys
import numpy as np

def np_arange():
    # arange(start=0,stop=x,step=1)
    print(np.arange(5))
    arr = np.arange(start=10, stop=20, step=2, dtype=float)
    print(arr)

def np_blank_matrix():
    print(np.ones(5))
    x = np.ones([3, 2], dtype=int)
    print(x)

    print(np.zeros(5))
    x = np.zeros([3, 2], dtype=int)
    print(x)

def np_random():
    #3x4 [[...]..]
    print(np.random.rand(3))
    print(np.random.rand(3, 4))  # n->[0,1)

    print('standard_normal(5):',np.random.standard_normal(5))
    print('randn(3)',np.random.randn(3))
    print('randn(3,4):\n',np.random.randn(3,4))

    print(np.random.random((3)))
    print(np.random.random((3, 4)))



    print(np.random.randint(3, 10))     # 3~10


# np_random()
np_blank_matrix()