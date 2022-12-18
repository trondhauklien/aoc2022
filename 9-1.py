import numpy as np
data = []
with open(f"9.txt", "r") as file:
    data = file.read().splitlines()

class Rope:
    def __init__(self, x, y):
        self.headX = x
        self.headY = y
        self.tailX = x
        self.tailY = y
        self.tailHistory = []

    def moveTailOneStep(self):
        if abs(self.tailX - self.headX) > 1:
            if self.tailX > self.headX:
                self.tailX -= 1
            else:
                self.tailX += 1
            self.tailY = self.headY
        if abs(self.tailY - self.headY) > 1:
            if self.tailY > self.headY:
                self.tailY -= 1
            else:
                self.tailY += 1
            self.tailX = self.headX
        self.tailHistory.append((self.tailX, self.tailY))

    def moveHeadOneStep(self, direction):
        if direction == "U":
            self.headY -= 1
        elif direction == "D":
            self.headY += 1
        elif direction == "L":
            self.headX -= 1
        elif direction == "R":
            self.headX += 1
        else:
            raise ValueError("Invalid direction")
        self.moveTailOneStep()

    def move(self, direction, steps):
        for i in range(steps):
            self.moveHeadOneStep(direction)

    def __repr__(self):
        return self.tailHistory()

rope = Rope(0, 0)
for row in data:
    instruction = []
    instruction = row.split()
    instruction[1] = int(instruction[1])
    rope.move(instruction[0], instruction[1])

print(len(set(rope.tailHistory)))