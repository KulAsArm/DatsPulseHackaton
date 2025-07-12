import numpy as np
test_map =  [{'q': 6, 'r': -20, 'cost': 1, 'type': 2}, {'q': 9, 'r': -23, 'cost': 1, 'type': 2}, {'q': 8, 'r': -23, 'cost': 1, 'type': 2}, {'q': 6, 'r': -19, 'cost': 1, 'type': 2}, {'q': 10, 'r': -23, 'cost': 1, 'type': 2}, {'q': 7, 'r': -19, 'cost': 1, 'type': 2}, {'q': 7, 'r': -17, 'cost': 1, 'type': 3}, {'q': 8, 'r': -16, 'cost': 1, 'type': 3}, {'q': 8, 'r': -22, 'cost': 1, 'type': 2}, {'q': 9, 'r': -18, 'cost': 1, 'type': 2}, {'q': 12, 'r': -24, 'cost': 1, 'type': 2}, {'q': 11, 'r': -16, 'cost': 1, 'type': 2}, {'q': 8, 'r': -19, 'cost': 1, 'type': 2}, {'q': 9, 'r': -17, 'cost': 1, 'type': 2}, {'q': 10, 'r': -19, 'cost': 1, 'type': 2}, {'q': 12, 'r': -23, 'cost': 1, 'type': 2}, {'q': 12, 'r': -17, 'cost': 1, 'type': 2}, {'q': 11, 'r': -23, 'cost': 1, 'type': 2}, {'q': 11, 'r': -19, 'cost': 1, 'type': 2}, {'q': 10, 'r': -20, 'cost': 1, 'type': 1}, {'q': 9, 'r': -20, 'cost': 1, 'type': 2}, {'q': 10, 'r': -18, 'cost': 1, 'type': 2}, {'q': 10, 'r': -16, 'cost': 1, 'type': 3}, {'q': 11, 'r': -17, 'cost': 1, 'type': 2}, {'q': 8, 'r': -24, 'cost': 1, 'type': 2}, {'q': 9, 'r': -22, 'cost': 1, 'type': 2}, {'q': 7, 'r': -22, 'cost': 1, 'type': 2}, {'q': 9, 'r': -16, 'cost': 1, 'type': 2}, {'q': 10, 'r': -24, 'cost': 1, 'type': 2}, {'q': 12, 'r': -18, 'cost': 1, 'type': 2}, {'q': 7, 'r': -23, 'cost': 1, 'type': 3}, {'q': 10, 'r': -22, 'cost': 1, 'type': 2}, {'q': 7, 'r': -21, 'cost': 1, 'type': 2}, {'q': 13, 'r': -22, 'cost': 1, 'type': 2}, {'q': 8, 'r': -17, 'cost': 1, 'type': 2}, {'q': 10, 'r': -21, 'cost': 1, 'type': 1}, {'q': 13, 'r': -20, 'cost': 1, 'type': 2}, {'q': 12, 'r': -20, 'cost': 1, 'type': 2}, {'q': 12, 'r': -19, 'cost': 1, 'type': 2}, {'q': 11, 'r': -24, 'cost': 1, 'type': 2}, {'q': 7, 'r': -18, 'cost': 1, 'type': 2}, {'q': 9, 'r': -21, 'cost': 1, 'type': 1}, {'q': 11, 'r': -21, 'cost': 1, 'type': 2}, {'q': 8, 'r': -18, 'cost': 1, 'type': 3}, {'q': 8, 'r': -20, 'cost': 1, 'type': 2}, {'q': 7, 'r': -20, 'cost': 1, 'type': 2}, {'q': 11, 'r': -18, 'cost': 1, 'type': 2}, {'q': 13, 'r': -18, 'cost': 1, 'type': 2}, {'q': 9, 'r': -24, 'cost': 1, 'type': 2}, {'q': 9, 'r': -19, 'cost': 1, 'type': 2}, {'q': 12, 'r': -22, 'cost': 1, 'type': 2}, {'q': 13, 'r': -21, 'cost': 1, 'type': 2}, {'q': 8, 'r': -21, 'cost': 1, 'type': 2}, {'q': 11, 'r': -22, 'cost': 1, 'type': 2}, {'q': 14, 'r': -20, 'cost': 1, 'type': 2}, {'q': 12, 'r': -21, 'cost': 1, 'type': 2}, {'q': 11, 'r': -20, 'cost': 1, 'type': 2}, {'q': 10, 'r': -17, 'cost': 1, 'type': 2}, {'q': 12, 'r': -16, 'cost': 1, 'type': 2}, {'q': 13, 'r': -19, 'cost': 1, 'type': 2}, {'q': 6, 'r': -21, 'cost': 1, 'type': 3}]
_map = sorted(test_map, key=lambda x: (x['q'], x['r']))
print(_map)
coord = []
for hex in _map:
    coord.append((hex['q'], hex['r']))
print(coord)
max_vert = max(coord, key=lambda x: x[0])[0]
min_vert = min(coord, key=lambda x: x[0])[0]
max_hor = min(coord, key=lambda x: x[1])[1]
min_hor = max(coord, key=lambda x: x[1])[1]
print(f"Максимум по вертикале {max_vert}")
print(f"Минимум по вертикале {min_vert}")
print(f"Максимум по горизонтале {max_hor}")
print(f"Минимум по горизонтале {max_vert}")
abs_max = abs(max([max_hor, min_hor, min_vert, max_vert], key=lambda x: abs(x)))
print(abs_max)
main_hex = [(9, -20), (10, -22)]
rows = ''
for i in range(-abs_max, abs_max):
    cols = ''
    for j in range(-abs_max, abs_max):
        if (i, j) in coord:
            if (i, j) in main_hex:
                cols += '\t**'
            else:
                cols += '\t^^'
            print((i, j))
        else:
            cols += "\t--"
    rows += cols + '\n'
print(rows)
# print(np.matrix(coord))
def create_map(_map):
    for hex in _map:
        ...
