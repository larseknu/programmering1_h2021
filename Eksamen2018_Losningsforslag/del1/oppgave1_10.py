a = "0#4!2#3!3#4"
sum = 0
deler = a.split("!")

for en_del in deler:
	tall = en_del.split("#")
	sum += int(tall[0]) * int(tall[1])

print(sum)

# Utskrift blir:
# 18

