import re


class Passport:
    def __init__(self):
        self.byr = None  # birth year
        self.iyr = None  # issue year
        self.eyr = None  # expiration year
        self.hgt = None  # height
        self.hcl = None  # hair colour
        self.ecl = None  # eye colour
        self.pid = None  # passport ID
        self.cid = None  # country ID
        self.count = 0

    def __str__(self):
        return '\tbyr:' + str(self.byr) + '\tiyr:' + str(self.iyr) + '\teyr:' + str(self.eyr) + '\thgt:' \
               + str(self.hgt) + '\thcl:' + str(self.hcl) + '\t\tecl:' + str(self.ecl) + '\t\tpid:' + str(self.pid) \
               + '\tcid:' + str(self.cid) + '   \tCount = ' + str(self.count)


passports = [Passport()]
with open("Passport_data.txt") as f:
    lines = f.readlines()
for i in range(0, len(lines)):
    if lines[i] == "\n":
        passports.append(Passport())
    else:
        Passport.byr = re.search(r'(byr):([^\s]+)', lines[i])
        if Passport.byr is not None:
            passports[-1].byr = str(Passport.byr.group(2))
            passports[-1].count += 1
        Passport.iyr = re.search(r'(iyr):([^\s]+)', lines[i])
        if Passport.iyr is not None:
            passports[-1].iyr = str(Passport.iyr.group(2))
            passports[-1].count += 1
        Passport.eyr = re.search(r'(eyr):([^\s]+)', lines[i])
        if Passport.eyr is not None:
            passports[-1].eyr = str(Passport.eyr.group(2))
            passports[-1].count += 1
        Passport.hgt = re.search(r'(hgt):([^\s]+)', lines[i])
        if Passport.hgt is not None:
            passports[-1].hgt = str(Passport.hgt.group(2))
            passports[-1].count += 1
        Passport.hcl = re.search(r'(hcl):([^\s]+)', lines[i])
        if Passport.hcl is not None:
            passports[-1].hcl = str(Passport.hcl.group(2))
            passports[-1].count += 1
        Passport.ecl = re.search(r'(ecl):([^\s]+)', lines[i])
        if Passport.ecl is not None:
            passports[-1].ecl = str(Passport.ecl.group(2))
            passports[-1].count += 1
        Passport.pid = re.search(r'(pid):([^\s]+)', lines[i])
        if Passport.pid is not None:
            passports[-1].pid = str(Passport.pid.group(2))
            passports[-1].count += 1
        Passport.cid = re.search(r'(cid):([^\s]+)', lines[i])
        if Passport.cid is not None:
            passports[-1].cid = str(Passport.cid.group(2))
            passports[-1].count += 1
valid = 0
for i in range(0, len(passports)):
    if passports[i].count > 7 or (passports[i].count == 7 and passports[i].cid is None):
        valid += 1
print("First check number of valid passports = " + str(valid))

passports1 = [Passport()]
for i in range(0, len(lines)):
    if lines[i] == "\n":
        passports1.append(Passport())
    else:
        Passport.byr = re.search(r'(byr):([^\s]+)', lines[i])
        if Passport.byr is not None and (1920 <= int(Passport.byr.group(2)) <= 2002):
            passports1[-1].byr = str(Passport.byr.group(2))
            passports1[-1].count += 1
        Passport.iyr = re.search(r'(iyr):([^\s]+)', lines[i])
        if Passport.iyr is not None and (2010 <= int(Passport.iyr.group(2)) <= 2020):
            passports1[-1].iyr = str(Passport.iyr.group(2))
            passports1[-1].count += 1
        Passport.eyr = re.search(r'(eyr):([^\s]+)', lines[i])
        if Passport.eyr is not None and (2020 <= int(Passport.eyr.group(2)) <= 2030):
            passports1[-1].eyr = str(Passport.eyr.group(2))
            passports1[-1].count += 1
        Passport.hgt = re.search(r'((hgt):([^\s]+(cm|in))+)', lines[i])
        if Passport.hgt is not None:
            if Passport.hgt.group(4) == "cm" and (150 <= int(Passport.hgt.group(3)[:-2]) <= 193):
                passports1[-1].hgt = str(Passport.hgt.group(3))
                passports1[-1].count += 1
            if Passport.hgt.group(4) == "in" and (59 <= int(Passport.hgt.group(3)[:-2]) <= 76):
                passports1[-1].hgt = str(Passport.hgt.group(3))
                passports1[-1].count += 1
        Passport.hcl = re.search(r'hcl:#([0-9a-f]{6})', lines[i])
        if Passport.hcl is not None:
            passports1[-1].hcl = str(Passport.hcl.group(1))
            passports1[-1].count += 1
        Passport.ecl = re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)', lines[i])
        if Passport.ecl is not None:
            passports1[-1].ecl = str(Passport.ecl.group(1))
            passports1[-1].count += 1
        Passport.pid = re.search(r'pid:([0-9]{9}\b)', lines[i])
        if Passport.pid is not None:
            passports1[-1].pid = str(Passport.pid.group(1))
            passports1[-1].count += 1
        Passport.cid = re.search(r'(cid):([^\s]+)', lines[i])
        if Passport.cid is not None:
            passports1[-1].cid = str(Passport.cid.group(2))
            passports1[-1].count += 1

valid = 0

for i in range(0, len(passports1)):
    if passports1[i].count == 8 or (passports1[i].count == 7 and passports1[i].cid is None):
        valid += 1
        # print("Valid " + str(i) + " " + str(passports1[i]))
print("Second check number of valid passports = " + str(valid))
