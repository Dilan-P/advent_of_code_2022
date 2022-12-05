#%%
with open('inputs/day_02.txt', 'r') as f:
    lines = f.readlines()

score = 0

for line in lines:
    line = line.strip()

    opp = line.split(' ')[0]
    me = line.split(' ')[1]

    if me == 'X':
        score += 1

        if opp == 'C':
            score += 6

        if opp == 'A':
            score += 3

    elif me == 'Y':
        score += 2

        if opp == 'A':
            score += 6

        if opp == 'B':
            score += 3

    elif me == 'Z':
        score += 3

        if opp == 'B':
            score += 6

        if opp == 'C':
            score += 3

print(f"Final score: {score}")
# %%
with open('inputs/day_02.txt', 'r') as f:
    lines = f.readlines()

score = 0

for line in lines:
    line = line.strip()

    opp = line.split(' ')[0]
    result = line.split(' ')[1]

    if result == 'X':
        score += 0

        if opp == 'A':
            score += 3
        if opp == 'B':
            score += 1
        if opp == 'C':
            score += 2

    elif result == 'Y':
        score += 3

        if opp == 'A':
            score += 1
        if opp == 'B':
            score += 2
        if opp == 'C':
            score += 3

    elif result == 'Z':
        score += 6

        if opp == 'A':
            score += 2
        if opp == 'B':
            score += 3
        if opp == 'C':
            score += 1

print(f"Final score: {score}")