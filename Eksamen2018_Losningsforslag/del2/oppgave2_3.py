from datetime import datetime


def aktiv(start, slutt, tidspunkt):
	start = datetime.fromisoformat(start)
	slutt = datetime.fromisoformat(slutt)

	return start < tidspunkt < slutt


naa = datetime.now()

forelesningsstart = "2021-11-05T14:15:00"
forelesningsslutt = "2021-11-25T16:00:00"

if aktiv(forelesningsstart, forelesningsslutt, naa):
	print("Kom deg på forelesning!")
else:
	print("For sent :(")
