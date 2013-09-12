def prob_even_fibonacci():
	first = 0
	second = 1
	total = 0
	while first <= 4000000:
		if first % 2 == 0:
			total += first
		temp = first
		first = second
		second += temp
	return total

total = prob_even_fibonacci();

print total

