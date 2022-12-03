
elfs = {}
with open('1_data.txt') as f:
    sum_so_far = 0
    elf = 0
    for line in f:
        if len(line.strip()) ==0:
            elfs[elf] = sum_so_far
            elf += 1
            sum_so_far = 0
        else:
            calorie = int(line.strip())
            sum_so_far += calorie

ranked = sorted(elfs.items(), key=lambda tpl: tpl[1], reverse=True)
print(sum([x[1] for x in ranked[:3]]))
        
