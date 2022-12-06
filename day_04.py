#%%
with open('inputs/day_04.txt', 'r') as f:
    lines = f.readlines()

overlaps = 0

for line in lines:
    line = line.strip()

    range_0 = line.split(',')[0]
    range_1 = line.split(',')[1]

    range_0_min = int(range_0.split('-')[0])
    range_0_max = int(range_0.split('-')[1])

    range_1_min = int(range_1.split('-')[0])
    range_1_max = int(range_1.split('-')[1])

    if (range_0_min <= range_1_min) and (range_0_max >= range_1_max):
        overlaps += 1
    
    elif (range_1_min <= range_0_min) and (range_1_max >= range_0_max):
        overlaps += 1

print(f"Num. overlapping ranges: {overlaps}")
# %%
with open('inputs/day_04.txt', 'r') as f:
    lines = f.readlines()

overlaps = 0

for line in lines:
    line = line.strip()

    range_0 = line.split(',')[0]
    range_1 = line.split(',')[1]

    range_0_min = int(range_0.split('-')[0])
    range_0_max = int(range_0.split('-')[1])

    range_1_min = int(range_1.split('-')[0])
    range_1_max = int(range_1.split('-')[1])

    range_0 = set(range(range_0_min, range_0_max+1))
    range_1 = set(range(range_1_min, range_1_max+1))

    if len(range_0.intersection(range_1)):
        overlaps += 1

print(f"Num. overlapping ranges: {overlaps}")