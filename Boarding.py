with open("Boarding_Passes.txt") as f:
    lines = f.readlines()

row = []
col = []
newmax = 0
curmax = 0
seatid = []

for i in range(0, len(lines)):
    lines[i] = lines[i].replace("\n", "")
    raw = lines[i]
    lines[i] = lines[i].replace("F", "0")
    lines[i] = lines[i].replace("B", "1")
    lines[i] = lines[i].replace("R", "1")
    lines[i] = lines[i].replace("L", "0")
    # print(lines[i], row[i], col[i])
    row.append(int(lines[i][:7], base=2))
    col.append(int(lines[i][7:], base=2))
    # print(lines[i], row[i], col[i])
    # print(row[i])
    newmax = (row[i] * 8) + col[i]
    seatid.append((row[i] * 8) + col[i])
    # print(raw, lines[i], row[i], col[i], newmax)
    if newmax > curmax:
        curmax = newmax
print("The highest seat ID is: " + str(newmax))

seatid.sort()
myseatid = 0
for i in range(0, len(seatid)-1):
    if seatid[i+1] - seatid[i] == 2:
        myseatid = seatid[i] + 1
print("My seat ID is: ", myseatid)
