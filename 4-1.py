data = []
with open(f"4.txt", "r") as file:
    data = file.read().splitlines()

output = 0
for line in data:
    l = line.split(",")
    o = []
    for e in l:
        o.append(e.split("-"))
    out = [list(map(int, e)) for e in o]    

    out.sort()
    print(out)
    if out[0][0] <= out[1][0] and out[0][1] >= out[1][1]:
        print("overlap")
        output += 1
    elif out[0][0] == out[1][0] and out[0][1] <= out[1][1]:
        print("overlap")
        output += 1
print(output)
