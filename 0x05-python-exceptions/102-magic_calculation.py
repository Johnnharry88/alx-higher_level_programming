#!/usr/bin/python3
def maigic_calculation(a, b):
	res = 0
	for x in range(1, 3):
		try:
			if x > a:
				raise Exception("Too far")
			else:
				res = res + (a ** b) / x
		except Exception:
			res = a + b
			break
	return (res)
