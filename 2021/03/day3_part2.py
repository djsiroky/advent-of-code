def binary_to_decimal(binary_string):
    multiplier = 1
    value = 0
    for digit in reversed(binary_string):
        if digit == "1":
            value += multiplier
        multiplier *= 2
    return value


def filter_by_occurence(items, index, isO2):
    d = len(items)
    one_count = 0
    one_items = []
    zero_items = []
    for item in items:
        if item[index] == "1":
            one_count += 1
            one_items.append(item)
        else:
            zero_items.append(item)
    if (float(one_count) / float(d) >= 0.5):
        if isO2:
            return one_items
        else:
            return zero_items
    else:
        if isO2:
            return zero_items
        else:
            return one_items


with open('input.txt') as f:
    lines = f.readlines()
    line_length = len(lines[0].replace('\n', '').strip())
    o2 = list(lines)
    co2 = list(lines)
    for i in range(line_length):
        if len(o2) > 1:
            o2 = filter_by_occurence(o2, i, True)
        else:
            o2 = o2[0].replace('\n', '')
            break
    for i in range(line_length):
        if len(co2) > 1:
            co2 = filter_by_occurence(co2, i, False)
        else:
            co2 = co2[0].replace('\n', '')
            break

    if type(o2) is list:
        o2 = o2[0]
    if type(co2) is list:
        co2 = co2[0]

    o2 = binary_to_decimal(o2.replace('\n', ''))
    co2 = binary_to_decimal(co2.replace('\n', ''))

    print(o2, co2, co2 * o2)
