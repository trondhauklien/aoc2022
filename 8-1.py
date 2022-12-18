import numpy as np
data = []
with open(f"8.txt", "r") as file:
    data = file.read().splitlines()

data = [[int(e) for e in row] for row in data]

# Check if cell value has higher or equal values in all directions

# Detfine function to get the column of a cell
def get_col(x):
    col = [row[x] for row in data]
    return col

output = np.zeros((len(data[0]), len(data)), dtype=int)
print(data)
for y, row in enumerate(data):
    for x, cell in enumerate(row):
        if x == 0 or x == len(row) - 1 or y == 0 or y == len(data) - 1:
            output[y][x] = 1
            continue
        col = get_col(x)
        print(f"({x}, {y})")
        print(cell)
        print(row[:x])
        print(row[x+1:])
        print(col[:y])
        print(col[y+1:])
        if cell > max(row[:x]) or cell > max(row[x+1:]) or cell > max(col[:y]) or cell > max(col[y+1:]):
            output[y][x] = 1
            continue

print(output.sum())
np.savetxt('8-2.txt', output, delimiter='', fmt='%d')