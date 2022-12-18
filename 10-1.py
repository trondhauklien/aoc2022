data = []
with open(f"10.txt", "r") as file:
    data = file.read().splitlines()

clock = 0

X = 1

signals = [20, 60, 100, 140, 180, 220]

data = [e.split() for e in data]

output = 0

def addToClock():
    global clock
    global output
    global X
    clock += 1
    if clock in signals:
        output += X * clock
        print(f"{X} * {clock} = {X*clock}")

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
print(output)
