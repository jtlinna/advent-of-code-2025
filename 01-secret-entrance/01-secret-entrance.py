input = []

with open('input.txt', 'r') as file:
    input = [-int(line[1:]) if line[0] == 'L' else int(line[1:]) for line in file.read().splitlines()]

# For Part 1 we want to calculate how many times dial (starting from 50) hits 0 after a rotation provided in the input
def count_dial_at_zero_after_rotations(start, input):
    dial = start
    counter = 0
    for value in input:
        dial = (dial + value + 100) % 100
        if dial == 0: counter += 1
    return counter

# For Part 2 we want to calculate how many times dial (starting from 50) hits 0 during or after a rotation step provided in the input
def count_dial_at_zero_after_or_during_rotations(start, input):
    dial = start
    counter = 0
    for value in input:
        for _ in range(abs(value)):
            step = 1 if value > 0 else -1
            dial = (dial + step + 100) % 100
            if dial == 0: counter += 1
    return counter

print('Part 1:', count_dial_at_zero_after_rotations(50, input))
print('Part 2:', count_dial_at_zero_after_or_during_rotations(50, input))

