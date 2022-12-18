import numpy as np
import matplotlib.pyplot as plt
data = []
with open(f"9.txt", "r") as file:
    data = file.read().splitlines()

class Tail:
    def __init__(self, x, y, child=None):
        self.x = x
        self.y = y
        self.child = child
        self.history = []

    def moveOneStep(self, parentX, parentY):
        if abs(self.x - parentX) > 1 and abs(self.y - parentY) > 1:
            if self.x > parentX:
                self.x -= 1
            else:
                self.x += 1
            if self.y > parentY:
                self.y -= 1
            else:
                self.y += 1
        if abs(self.x - parentX) > 1:
            if self.x > parentX:
                self.x -= 1
            else:
                self.x += 1
            self.y = parentY
        if abs(self.y - parentY) > 1:
            if self.y > parentY:
                self.y -= 1
            else:
                self.y += 1
            self.x = parentX
        self.history.append((self.x, self.y))
        if self.child is not None:
            self.child.moveOneStep(self.x, self.y)
        return

    def __repr__(self):
        return f"({self.x}, {self.y})"
class Head:
    def __init__(self, x, y, children):
        self.headX = x
        self.headY = y
        self.child = Tail(x, y)
        for i in range(children-1):
            self.child = Tail(x, y, self.child)

    def moveHeadOneStep(self, direction):
        if direction == "U":
            self.headY += 1
        elif direction == "D":
            self.headY -= 1
        elif direction == "L":
            self.headX -= 1
        elif direction == "R":
            self.headX += 1
        else:
            raise ValueError("Invalid direction")
        self.child.moveOneStep(self.headX, self.headY)

    def move(self, direction, steps):
        for i in range(steps):
            self.moveHeadOneStep(direction)

rope = Head(0, 0, 9)
for row in data:
    instruction = []
    instruction = row.split()
    instruction[1] = int(instruction[1])
    rope.move(instruction[0], instruction[1])

history = rope.child.child.child.child.child.child.child.child.child.history
print(len(set(history)))

plt.scatter(*zip(*history))
plt.scatter(*zip(*rope.child.history), marker="*")

plt.show()