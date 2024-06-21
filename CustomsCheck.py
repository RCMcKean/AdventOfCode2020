import re

group = []
groups = [group]
group_total = []
group_match = []

with open("Customs.txt") as f:
    lines = f.readlines()
f.close()

for i in range(0, len(lines)):
    if lines[i] == "\n":
        group = []
        groups.append(group)
    else:
        a = re.search(r'\w+', lines[i])
        a = str(a.group(0))
        group.append(a)

for i in range(0, len(groups)):
    full = list(groups[i][0])
    full.sort()
    for j in range(0, len(groups[i])-1):
        part = list(groups[i][j+1])
        # print("input full: ", full)
        # print("input part: ", part)
        for item in part:
            if item not in full:
                full.append(item)
        full.sort()
        # print("output full: ", full, "\n")
    group_total.append(len(full))
print("The sum of all the groups individual answers is: ", sum(group_total))

for i in range(0, len(groups)):
    final = []
    rem = []
    if i == 22:
        print("error")
    part1 = list(groups[i][0])
    part1.sort()
    if len(groups[i]) == 1:
        final = part1
    for j in range(0, len(groups[i])-1):
        part2 = list(groups[i][j+1])
        part2.sort()
        for letter in part1:
            if letter in part2:
                if letter not in final:
                    final.append(letter)
            else:
                if letter in final:
                    if letter not in rem:
                        rem.append(letter)
                    # final.remove(letter)  # note index and remove that instead
        for a in rem:
            if a in final:
                final.remove(a)
        part1 = final
    final.sort()
    # print(final)

    group_match.append(len(final))
print(group_match)
print("The sum of all the groups matching answers is: ", sum(group_match))
# Not 3490 - too high
# Not 3320, 3328, 3378
# test 1 or 2 matches
