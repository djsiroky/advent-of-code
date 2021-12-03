gamma = ""
epsilon = ""
lineCounts = []

def binary_to_decimal(binary_string):
	multiplier = 1
	value = 0
	for digit in reversed(binary_string):
		if digit == "1":
			value += multiplier
		multiplier *= 2
	return value

with open('input.txt') as f:
	lines = f.readlines()
	line_length = len(lines[0].replace('\n', '').strip())
	lineCounts = [0 for i in range(line_length)]
	for line in lines:
		for idx, char in enumerate(line):
			if char == "1":
				lineCounts[idx] += 1
	
	print(lineCounts)
	gamma = [ int(float(x) / len(lines) > 0.50) for x in lineCounts]
	epsilon = [ int(not x) for x in gamma ]
	gamma = [ str(x) for x in gamma]
	epsilon = [ str(x) for x in epsilon]
	g_dec = binary_to_decimal(gamma)
	e_dec = binary_to_decimal(epsilon)
	print(''.join(gamma))
	print(''.join(epsilon))
	print(g_dec, e_dec, g_dec * e_dec)
		
		