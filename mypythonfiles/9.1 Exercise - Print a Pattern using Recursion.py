def print_pattern(n):
	if n == 1:
		print("*")
	else:
		print("*" * n)
		print_pattern(n-1)