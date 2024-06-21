# pale purple bags contain 4 muted yellow bags, 2 mirrored chartreuse bags, 5 mirrored purple bags, 2 mirrored red bags.
# How many bag colors can eventually contain at least one shiny gold bag?

# adj colour "bags contain" number adj colour "bags" [, or .]+
import re


class Bag:
    def __init__(self):
        self.colour = None
        self.contents = None
        self.count = 0
        self.gold = False

    def __str__(self):
        return 'colour:' + str(self.colour) + '\tcontents:' + str(self.contents) + '\tcount:' + str(self.count) +\
               '\tgold:' + str(self.gold)


bags = []

with open("trainingset.txt") as f:
    lines = [x.split() for x in f.read().split("\n")]


for i in range(0, len(lines)):
    bags.append(Bag())
    bags[i].colour = " ".join(lines[i][0:2])
    bags[i].contents = " ".join(lines[i][4:]).split(",")
    if "no other bags." in bags[i].contents:
        bags[i].count = 0
    else:
        bags[i].count = len(bags[i].contents)
    if r'shiny gold bag' in bags[i].contents:  # Test for gold bag
        bags[i].gold = True

    # print(Bag.colour)
    # print(Bag.contents)

    print(str(bags[i]))

