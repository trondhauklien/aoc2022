data = []
with open(f"6.txt", "r") as file:
    data = file.read().splitlines()

i = 0
seq = ""
for c in data[0]:
    i += 1
    if (len(seq) >= 4):
        seq = seq[1:]
    seq = seq + c
    print(seq)
    if (len(seq) == 4):
        if (len(set(seq)) == 4):
            break
    
print(seq)
print(i)