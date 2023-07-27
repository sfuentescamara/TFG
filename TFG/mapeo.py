# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:03:24 2019

@author: sergi
"""

def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

rl_x = map(0, 90, 120, 0, 1080)

print(rl_x)