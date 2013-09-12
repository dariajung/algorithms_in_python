def mult_three_five():
	sum = 0
	for x in range(1000):
		if x % 3 == 0 or x % 5 == 0:
			sum += x
	return sum

answer = mult_three_five();

print answer
