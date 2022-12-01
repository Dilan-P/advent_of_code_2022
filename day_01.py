#%% Part 1
with open('inputs/day_01.txt', 'r') as f:
    lines = f.readlines()

cals = 0
max_cals = 0

for line in lines:
    line = line.strip()

    if line == '':
        if cals > max_cals:
            max_cals = cals
        
        cals = 0

    else:
        cals += int(line)

print(f"max cals: {max_cals}")
# %% Part 2
with open('inputs/day_01.txt', 'r') as f:
    lines = f.readlines()

elf_cals = 0
cals = []

for line in lines:
    line = line.strip()

    if line == '':
        cals.append(elf_cals)
        elf_cals = 0

    else:
        elf_cals += int(line)

sorted_cals = sorted(cals)

print(f"top 3 totals: {sum(sorted_cals[-3:])},  ({sorted_cals[-3:]})")