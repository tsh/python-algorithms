
def range_to_tuple(r: str) -> tuple:
    n1,n2 = r.split('-')
    return(int(n1), int(n2))

counter = 0
with open('4_data.txt') as f:
    for line in f:
        f,t = line.split(',')
        sort = sorted([range_to_tuple(f), range_to_tuple(t)], key=lambda x: x[0])
        range1, range2 = sort[0], sort[1]
        if (range2[0]>=range1[0] and range2[0] <= range1[1]) or (range2[1]<=range1[1]):
            counter += 1


print(counter)
