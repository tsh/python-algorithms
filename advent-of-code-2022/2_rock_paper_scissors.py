draw ={
        'A': 'X',
        'B': 'Y', 
        'C': 'Z'}

win = {'A': 'Y',
       'B': 'Z',
       'C': 'X'}

lose = {'A': 'Z',
        'B': 'X',
        'C': 'Y'}

score = {
    ('A', 'X'): 1 + 3,
    ('B', 'X'): 1 + 0,
    ('C', 'X'): 1 + 6, 
    ('A', 'Y'): 2 + 6,
    ('B', 'Y'): 2 + 3,
    ('C', 'Y'): 2 + 0,
    ('A', 'Z'): 3 + 0,
    ('B', 'Z'): 3 + 6,
    ('C', 'Z'): 3 + 3,
    }

with open('2_data.txt') as f:
    s = 0
    for line in f:
        opponent, action = tuple(line.strip().split())
        if action == 'X':
            moves = lose
        elif action == 'Y':
            moves = draw
        elif action == 'Z':
            moves = win
        my_move = moves[opponent]
        s+= score[(opponent, my_move)]
    print(s)

