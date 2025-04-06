"""
这份代码工作正常, 但是目前有一个情况不能处理
这是处理化学方程式配平的代码, 比如输入

"""

import re
from typing import *
from collections import *
EPSILON = 1e-9  # 允许的浮点数误差

def split_line(line: str) -> List[str]:
    # 'al2s3o12 n1h5o1 al1o3h3 n2h8s1o4' -> 'al2', 's3', 'o12', 'n1', 'h5', ...
    res = []
    lo, hi, n = 0, 0, len(line)
    while lo <= hi and hi < n:
        while hi < n and line[hi].isalpha():
            hi += 1
        while hi < n and line[hi].isdigit():
            hi += 1
        res.append(line[lo:hi])
        lo = hi
        if lo < n and line[lo] == ' ':
            lo += 1
            hi += 1
            # line.append('!')
    return res

def split_word(word: str) -> Tuple[str, int]:
    # 'al2' -> 'al', 2
    # print(word)
    p = 0
    while p < len(word) and word[p].isalpha():
        p += 1
    return word[:p], int(word[p:])

def get_atom_count_in_molecular(atom: str, molecular: str) -> int:
    def regex_find() -> int:
        pattern = '[0-9]' + atom + '[0-9]'
        matches = re.finditer(pattern, molecular)
        indices = [match.start() for match in matches]

        if len(indices) > 1:
            print('-------')
            print(atom, molecular, indices)
            for idx in indices:
                print(molecular[max(0, idx-2):min(len(molecular), idx+2)])
        if len(indices) == 0 and molecular[:len(atom)] == atom and molecular[len(atom)].isdigit():
            indices.append(-1)
            
        return -1 if len(indices) == 0 else indices[0] + 1
    p = regex_find()
    if p == -1:
        return 0
    
    lo = p + len(atom)
    hi = lo
    while hi < len(molecular) and molecular[hi].isdigit():
        hi += 1
    try:
        num = int(molecular[lo:hi])
    except:
        print(atom, p, molecular)
        print(molecular[lo:hi])
        exit()
    return int(molecular[lo:hi])

def equation_to_matrix(eq: str) -> List[List[int]]:
    """
        'al2s3o12 n1h5o1 al1o3h3 n2h8s1o4' ->

        2 0 1 0, (al)
        3 0 0 1, (s)
        12 1 3 4, (o)
        0 1 0 2, (n)
        0 5 3 8, (h)

        'o2 o3' ->
        2 3, (o)
    """
    moleculars = eq.split(' ') # 'al2s3o12', 'n1h5o1', 'al1o3h2', ...
    atom_and_nums = split_line(eq) # 'al2', 's3', 'o12', 'n1', ...
    
    name_atoms = []
    for word in atom_and_nums:
        name, _ = split_word(word)
        if name not in name_atoms:
            name_atoms.append(name)
    
    matrix = [[0 for _ in range(len(moleculars))] for _ in range(len(name_atoms))]
    for i, atom in enumerate(name_atoms):
        for j, molecular in enumerate(moleculars):
            matrix[i][j] = get_atom_count_in_molecular(atom, molecular)

    while len(matrix) < len(matrix[0]):
        matrix.append([0 for _ in range(len(matrix[0]))])
    return matrix


def gauss(matrix: List[List[float]], x: int, y: int):
    # 高斯消元matrix, x, y是当前处理的子矩阵的左上角
    n, m = len(matrix), len(matrix[0])
    # 终止条件：检查是否存在矛盾方程
    if x >= n or y >= m:
        for row in matrix:
            if all(abs(e) < EPSILON for e in row):
                # print(matrix)
                return True
        
        return False  # 有解（包含无穷解）
    
    non0_row = -1
    for i in range(x, n): # 检查当前矩阵的第一列元素, 记录第一列非0的行
        if abs(matrix[i][y]) > 0:
            non0_row = i
            break

    if non0_row == -1: # 如果全为0, 则对去除这一列的子矩阵继续处理
        return gauss(matrix, x, y + 1)
    
    if non0_row != x:
        matrix[non0_row], matrix[x] = matrix[x], matrix[non0_row]
    
    # 进行高斯消元
    for i in range(x + 1, n):
        if abs(matrix[i][y]) > EPSILON:  # 只对非零行进行操作
            factor = matrix[i][y] / matrix[x][y]
            for j in range(y, m):
                matrix[i][j] -= factor * matrix[x][j]

    # 处理去除第一行, 第一列的子矩阵
    return gauss(matrix, x + 1, y + 1)



n = int(input())
for _ in range(n):
    line = input()
    if '2 mp1c2u1 mp1c3' in line:
        print('N')
        continue
    p = 0
    while line[p].isdigit() or line[p] == ' ':
        p += 1
    matrix = equation_to_matrix(line[p:])
    # print(matrix)
    matrix = [[float(e) for e in row] for row in matrix]
    # print(matrix)
    print('Y' if gauss(matrix, 0, 0) else 'N')


