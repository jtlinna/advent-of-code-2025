def parse_id_range(id_range):
    start, end = id_range.split('-')
    return (int(start), int(end))

def get_ids_with_digit_sequence_repeating_twice(start, end):
    result = []
    for id in range(start, end + 1):
        id_str =  str(id)
        id_len = len(id_str)
        if id_len % 2 != 0: continue
        half_len = id_len // 2
        first_half = id_str[:half_len]
        second_half = id_str[half_len:]
        if first_half == second_half:
            result.append(id)
    return result

def get_ids_with_digit_or_digit_sequence_repeating_twice_or_more(start, end):
    result = []
    for id in range(start, end + 1):
        id_str = str(id)
        id_len = len(id_str)
        if id_len < 2: continue
        if all(digit == id_str[0] for digit in id_str):
            result.append(id)
            continue

        digit_sequence = id_str[0]
        for digit in id_str[1:]:
            digit_sequence += digit
            if len(digit_sequence) > id_len // 2:
                break

            if id_str.count(digit_sequence) >= 2 and len(id_str.replace(digit_sequence, '')) == 0:
                result.append(id)
                break
    return result

def get_invalid_ids(id_ranges, invalid_func):
    invalid_ids = []
    for id_range in id_ranges:
        start, end = id_range
        repeating_ids = invalid_func(start, end)
        invalid_ids += repeating_ids
    return invalid_ids

input = []
with open('input.txt', 'r') as file:
    input = [parse_id_range(id_range) for id_range in file.readline().split(',')]
              
print('Part 1:', sum(get_invalid_ids(input, get_ids_with_digit_sequence_repeating_twice)))
print('Part 2:', sum(get_invalid_ids(input, get_ids_with_digit_or_digit_sequence_repeating_twice_or_more)))
