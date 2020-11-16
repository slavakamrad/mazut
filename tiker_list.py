tiker_list = []

with open('tikers.txt') as In:
    for line in In:
        tiker_list.append(line.rstrip('\n'))
