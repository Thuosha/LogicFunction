# Способ решение (2)

# "Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w"
from itertools import *
def function(x, y, z, w):
    return (x == (w or y)) or ((w <= z) and (y <= w))

for void1, void2, void3, void4, void5, void6, void7 in product([0, 1], repeat=7):
    table = (
        (1, void1, void2, 1, 0),
        (void3, void4, void5, 1, 0),
        (1, void6, 1, void7, 0)
    )
    if len(table) == len(set(table)):
        for shuffle in permutations("xyzw", r=4):
            if all(function(**dict(zip(shuffle, line))) == line[-1] for line in table):
                print(*shuffle)

# "Определите, сколько существует различных способов расстановки переменных w, x, y, z, подходящих для данной таблицы истинности?"
from itertools import *
def function(x, y, z, w):
    return (x == (w or y)) or ((w <= z) and (y <= w))

S = set()
for void1, void2, void3, void4, void5, void6, void7 in product([0, 1], repeat=7):
    table = (
        (1, void1, void2, 1, 0),
        (void3, void4, void5, 1, 0),
        (1, void6, 1, void7, 0)
    )
    if len(table) == len(set(table)):
        for shuffle in permutations("xyzw", r=4):
            if all(function(**dict(zip(shuffle, line))) == line[-1] for line in table):
                S.add(shuffle)
print(len(S))

# Written by Vsevolod Flovitskiy.
