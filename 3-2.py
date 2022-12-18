data = []
with open(f"3.txt", "r") as file:
    data = file.read().splitlines()
print(data)
# data = [
#     'NFLsRDNNDNBDlgPPgBglQlzj',
# 'HJhdZpfJzlWQjjHw',
# 'ffJTppZZqTNlGnNsMG'
# ]
o = 0

for i, line in enumerate(data[::3]):
    print(data.index(line), "-", line)
    ix = data.index(line)
    for l in line:
        if l in data[ix+1] and l in data[ix+2]:
            print("match:" + l)
            if l.isupper():
                print(ord(l) - 64 + 26)
                o += ord(l) - 64 + 26
                break
            else:
                print(ord(l) - 96)
                o += ord(l) - 96
                break
        else:
            print("no match:" + l)


 

print(o)

