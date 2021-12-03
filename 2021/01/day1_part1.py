num_increased = 0

with open("input.txt") as f:
    prev = None
    for line in f:
        if prev == None:
            print("{} (N/A - No previous measurement)".format(line))
            prev = int(line)
            continue
        if int(line) > prev:
            num_increased += 1
            print("{} (increased)".format(line.strip()))
        else:
            print("{} (decreased)".format(line.strip()))
        prev = int(line)

print("Number of increases: {}".format(num_increased))
