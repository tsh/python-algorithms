import string
from itertools import chain

chars = dict(zip(chain(string.ascii_lowercase, string.ascii_uppercase), range(1, 53)))


sum = 0
with open('3_data.txt') as f:
    triplets = []
    for line in f:
        triplets.append(line.strip())

        if len(triplets) == 3:
            common = set(triplets[0]) & set(triplets[1]) & set(triplets[2])
            num = chars[list(common)[0]]
            sum += num
            triplets = []
print(sum)
