from typing import *
from collections import *
from datetime import *
from functools import *
import copy
import heapq
import bisect
import math
import sys 

# states_odd是可能存在没有点亮位置的码
states_odd = ['0000011',
'1001011',
'0000001',
'0100001',
'0101011',
'0110110',
'1111111',
'0010110',
'0101001',
'0010110',
'1011100',
'0100110',
'1010000',
'0010011',
'0001111',
'0101101',
'0110101',
'1101010',
]

# states_nml是标准码
states_nml = [
    '1111110',
    '0110000',
    '1101101',
    '1111001',
    '0110011',
    '1011011',
    '1011111',
    '1110000',
    '1111111',
    '1111011'
]


def cnt(state: str) -> int:
    # 统计一个状态可能可以点亮成多少个状态

    res = 1 if state in states_nml else 0
    pos = [p for p in range(7) if state[p] == '0'] # 尝试点亮这些位置
    
    def dfs(p, state):
        nonlocal res
        if p >= len(pos):
            return 
        sub = pos[p]
        new_state = state[:sub] + '1' + state[sub+1:]
        if new_state in states_nml:
            print(new_state)
            res += 1
        # 点亮sub, 或者不点亮sub
        dfs(p + 1, state)
        dfs(p + 1, new_state)      
    dfs(0, state)

    return res 

ans = 1
for state in states_odd:
    print(state, cnt(state))
    ans *= cnt(state)

print(ans)
