data = []
with open(f"7.txt", "r") as file:
    data = file.read().splitlines()

class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_path(self):
        path = []
        node = self
        while node != None:
            path.append(node.name)
            node = node.parent
        return path

    def tree(self):
        print(self.name)
        for child in self.children:
            if isinstance(child, Folder):
                child.tree()
            else:
                print("  " + child.name)

    def get_size(self):
        size = 0
        for child in self.children:
            if isinstance(child, Folder):
                size += child.get_size()
            else:
                size += child.size
        return size

    # Get sum of all folders smaller than 100000
    def get_small_folders(self):
        size = 0
        for child in self.children:
            if isinstance(child, Folder):
                if child.get_size() < 100000:
                    size += child.get_size()
                size += child.get_small_folders()
        return size
    
    # Get smalles folder with size > 8748071
    def get_small_folder(self):
        small = None
        for child in self.children:
            if isinstance(child, Folder):
                if child.get_size() > 8748071:
                    if small == None:
                        small = child
                    elif child.get_size() < small.get_size():
                        small = child
                small_child = child.get_small_folder()
                if small_child != None:
                    if small == None:
                        small = small_child
                    elif small_child.get_size() < small.get_size():
                        small = small_child
        return small

    def __repr__(self):
        return f"{self.name}"

class File:
    def __init__(self, name, size):
        self.name = name
        self.parent = None
        self.size = size

    def add_parent(self, parent):
        self.parent = parent

    def get_path(self):
        path = []
        node = self
        while node != None:
            path.append(node.name)
            node = node.parent
        return path

    def __repr__(self):
        return f"{self.name}"

root = Folder("root")
current = root

ls = False
for line in data:
    print(line)
    if line.startswith("$ ls"):
        ls = True
        continue
    if ls == True and line.startswith("dir "):
        name = line.split(" ")[1]
        folder = Folder(name)
        current.add_child(folder)
        continue
    if ls == True and not line.startswith("$"):
        name = line.split(" ")[1]
        size = int(line.split(" ")[0])
        file = File(name, size)
        current.add_child(file)
        continue
    if ls == True and line.startswith("$"):
        ls = False
    if line.startswith("$ cd"):
        name = line.split(" ")[2]
        if name == "..":
            current = current.parent
        else:
            for child in current.children:
                if child.name == name:
                    current = child
                    break
        continue
    
print(root.get_small_folder().get_size())