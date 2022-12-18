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

class Tree:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.value = data[y][x]
        self.left = data[y][:x]
        self.left.reverse()
        self.right = data[y][x+1:]
        self.up = get_col(x)[:y]
        self.up.reverse()
        self.down = get_col(x)[y+1:]
    
    def __str__(self):
        return f"({self.x}, {self.y}) = {self.value}"
    
    def __repr__(self):
        return self.__str__()

    def getScenicScore(self):
        score = 1
        for direction in [self.left, self.right, self.up, self.down]:
            hitEdge = True
            for i, cell in enumerate(direction):
                if cell >= self.value:
                    score *= (i + 1)
                    hitEdge = False
                    break
            if hitEdge:
                score *= len(direction)
        
        return score
    


output = np.zeros((len(data[0]), len(data)), dtype=int)
for y, row in enumerate(data):
    for x, cell in enumerate(row):
        if x == 0 or x == len(row) - 1 or y == 0 or y == len(data) - 1:
            output[y][x] = 0
            continue
        tree = Tree(x, y, data)
        output[y][x] = tree.getScenicScore()

print(output.max())