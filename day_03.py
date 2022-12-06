#%%
with open('inputs/day_03.txt', 'r') as f:
    lines = f.readlines()

priority = 0

for line in lines:
    line = line.strip()

    line_0 = line[:len(line)//2]
    line_1 = line[len(line)//2:]

    line_0 = set(line_0)
    line_1 = set(line_1)

    unique_char = str(list(line_0.intersection(line_1))[0])

    if unique_char.isupper():
        priority += ord(unique_char) - 38
    else:
        priority += ord(unique_char) - 96

print(f"Priority sum: {priority}")
# %%
with open('inputs/day_03.txt', 'r') as f:
    lines = f.readlines()

priority = 0

for i in range(0, len(lines), 3):
    line_0 = lines[i].strip()
    line_1 = lines[i+1].strip()
    line_2 = lines[i+2].strip()

    line_0 = set(line_0)
    line_1 = set(line_1)
    line_2 = set(line_2)

    unique_char = str(list(line_0.intersection(line_1).intersection(line_2))[0])

    if unique_char.isupper():
        priority += ord(unique_char) - 38
    else:
        priority += ord(unique_char) - 96

print(f"Priority sum: {priority}")