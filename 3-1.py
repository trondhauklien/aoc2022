data = []
with open(f"3.txt", "r") as file:
    data = file.read().splitlines()
print(data)
output = []

for line in data:
    print(len(line))
    a  = line[:len(line)//2]
    b = line[len(line)//2:]
    output.append([a,b])

print(output)

o = 0
for s in output:
    print(s)
    
    for l in s[0]:
        if l in s[1]:
            if l.isupper():
                print(ord(l) - 64 + 26)
                o += ord(l) - 64 + 26
                break
            else:
                print(ord(l) - 96)
                o += ord(l) - 96
                break

 

print(o)

