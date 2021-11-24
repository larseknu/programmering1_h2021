def test(a, b, c):
	if c:
		return a + b
	else:
		return a - b


riktig = 3 > 4 and 7 > 2
print(test(3, 4, riktig))

# Utskriften blir:
# -1