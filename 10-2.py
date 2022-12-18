import textwrap
data = []
with open(f"10.txt", "r") as file:
    data = file.read().splitlines()

clock = 0

X = 1

signals = [20, 60, 100, 140, 180, 220]

data = [e.split() for e in data]

output = 0
pixels = ""

def addToClock():
    global clock
    global output
    global X
    global pixels
    if X == clock%40 or X + 1 == clock%40 or X - 1 == clock%40:
        pixels += "#"
    else: 
        pixels += "."
    clock += 1

while True:
    if data == []:
        break
    instruction = data.pop(0)
    addToClock()
    if instruction[0] == "noop":
        continue
    if instruction[0] == "addx":
        addToClock()
        X += int(instruction[1])
        continue

pixels = textwrap.wrap(pixels, 40)
for line in pixels:
    print(line)
