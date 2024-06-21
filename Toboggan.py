def route(down, across):
    level = 0
    tile = 0
    trees = 0

    for x in range(0, len(lines)-1):
        level += down
        tile += across
        if tile > 30:
            tile = tile - 31
        if level > len(lines)-1:
            break
        if lines[level][tile] == "#":
            trees += 1
    print("Sledging down", down, "levels and across", across, "tiles you will hit:", trees, "tree's")
    return trees


with open("map.txt", 'r') as f:
    lines = [line.split() for line in f]
    lines = [str(line) for line in lines]

for i in range(0, len(lines)):
    lines[i] = (lines[i].replace('[', ''))
    lines[i] = (lines[i].replace(']', ''))
    lines[i] = (lines[i].replace("'", ''))

path1 = route(1, 1)
path2 = route(1, 3)
path3 = route(1, 5)
path4 = route(1, 7)
path5 = route(2, 1)

total = (path1 * path2 * path3 * path4 * path5)
print("Total number of tree's hit on all paths is", total)

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
