num_increased = 0

with open("test.txt") as f:
    prev = None
    window = []
    sum_of_measurements = None
    for line in f:
        num = int(line)
        if len(window) < 3:
            window.append(num)
            continue
        else:
            window.pop(0)
            window.append(num)
            sum_of_measurements = sum(window)

        if prev == None:
            print("{} (N/A - No previous measurement)".format(sum_of_measurements))
            prev = int(line)
            continue
        if sum_of_measurements > prev:
            num_increased += 1
            print("{} (increased)".format(sum_of_measurements))
        else:
            print("{} (decreased)".format(sum_of_measurements))
        prev = sum_of_measurements

print("Number of increases: {}".format(num_increased))
