#%%
with open('inputs/day_06.txt', 'r') as f:
    lines = f.readlines()

line = lines[0].strip()

for i in range(len(line)):
    if len(line[i:i+4]) == len(set(line[i:i+4])):
        break

print(f"First marker at char: {i+4}")
#%%
with open('inputs/day_06.txt', 'r') as f:
    lines = f.readlines()

line = lines[0].strip()

for i in range(len(line)):
    if len(line[i:i+14]) == len(set(line[i:i+14])):
        break

print(f"First marker at char: {i+14}")