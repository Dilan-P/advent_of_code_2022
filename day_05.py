#%%
with open('inputs/day_05.txt', 'r') as f:
    lines = f.readlines()

columns = [
    ['b', 'l', 'd', 't', 'w', 'c', 'f', 'm'],
    ['n', 'b', 'l'],
    ['j', 'c', 'h', 't', 'l', 'v'],
    ['s', 'p', 'j', 'w'],
    ['z', 's', 'c', 'f', 't', 'l', 'r'],
    ['w', 'd', 'g', 'b', 'h', 'n', 'z'],
    ['f', 'm', 's', 'p', 'v', 'g', 'c', 'n'],
    ['w', 'q', 'r', 'j', 'f', 'v', 'c', 'z'], 
    ['r', 'p', 'm', 'l', 'h']
]

for line in lines[10:]:
    line = line.strip()

    num_moves = [int(x) for x in line.split(' ') if x.isdigit()][0]
    column_from = [int(x) for x in line.split(' ') if x.isdigit()][1]
    column_to = [int(x) for x in line.split(' ') if x.isdigit()][2]

    for i in range(num_moves):
        columns[column_to-1].append(columns[column_from-1].pop())

message = [column[-1] for column in columns]
print(f"Final message: {''.join(message)}")
# %%
with open('inputs/day_05.txt', 'r') as f:
    lines = f.readlines()

columns = [
    ['b', 'l', 'd', 't', 'w', 'c', 'f', 'm'],
    ['n', 'b', 'l'],
    ['j', 'c', 'h', 't', 'l', 'v'],
    ['s', 'p', 'j', 'w'],
    ['z', 's', 'c', 'f', 't', 'l', 'r'],
    ['w', 'd', 'g', 'b', 'h', 'n', 'z'],
    ['f', 'm', 's', 'p', 'v', 'g', 'c', 'n'],
    ['w', 'q', 'r', 'j', 'f', 'v', 'c', 'z'], 
    ['r', 'p', 'm', 'l', 'h']
]

for line in lines[10:]:
    line = line.strip()

    num_moves = [int(x) for x in line.split(' ') if x.isdigit()][0]
    column_from = [int(x) for x in line.split(' ') if x.isdigit()][1]
    column_to = [int(x) for x in line.split(' ') if x.isdigit()][2]

    for i in [x for x in columns[column_from-1][-num_moves:]]:
        columns[column_to-1].append(i)
    columns[column_from-1] = columns[column_from-1][:-num_moves]


message = [column[-1] for column in columns]
print(f"Final message: {''.join(message)}")