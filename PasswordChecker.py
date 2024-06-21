def first_check(entry):
    count = 0
    minval, maxval = entry[0].split("-")
    minval = int(minval)
    maxval = int(maxval)
    letter = entry[1].split(":")[0]
    password = entry[2]
    password = [char for char in password]
    for item in password:
        if item == letter:
            count += 1
    if minval <= count <= maxval:
        return True
    else:
        return False


def second_check(entry):
    pos1, pos2 = entry[0].split("-")
    pos1 = int(pos1)-1
    pos2 = int(pos2)-1
    letter = entry[1].split(":")[0]
    password = entry[2]
    # password = [char for char in password]
    if (password[pos1] == letter) ^ (password[pos2] == letter):
        return True
    else:
        return False


check1 = check2 = 0
with open("password.txt", 'r') as f:
    lines = [line.split() for line in f]
for i in lines:
    if first_check(lines[lines.index(i)]):
        check1 += 1
print("After checking the password database against the first set of rules there are:")
print(str(check1) + " correct passwords")

for i in lines:
    if second_check(lines[lines.index(i)]):
        check2 += 1
print("After checking the password database against the second set of rules there are:")
print(str(check2) + " correct passwords")

