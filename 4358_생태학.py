import sys

trees = {}

count = 0
while True:
    Name = sys.stdin.readline().rstrip()
    if Name == "":
        break
    trees[Name] = trees.get(Name, 0) + 1
    count += 1

for tree in sorted(trees.keys()):
    print("%s %.4f" %(tree, (trees[tree]/count)*100))