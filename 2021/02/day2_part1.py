y_val = 0
x_val = 0

with open('input.txt') as f:
	for line in f:
		directions = ['up', 'down', 'forward']
		[direction, amount] = line.replace('\n', '').split(' ')
		if direction not in direction:
			raise LookupError("Unable to find the direction in directions")
		if direction == 'up':
			y_val -= int(amount)
		elif direction == 'down':
			y_val += int(amount)
		elif direction == 'forward':
			x_val += int(amount)
	
	print(x_val, y_val, x_val * y_val)
		
		