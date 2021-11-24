from datetime import datetime, date


def aktiv(start, slutt, tidspunkt):
	start = datetime.fromisoformat(start)
	slutt = datetime.fromisoformat(slutt)

	return start < tidspunkt < slutt


def innenfor_dato(start, slutt, dato):
	start = datetime.fromisoformat(start).date()
	slutt = datetime.fromisoformat(slutt).date()

	return start == dato and slutt == dato


def formater_klokkeslett(dato_string):
	dato = datetime.fromisoformat(dato_string)

	return dato.strftime("%H:%M")


def sorter_avtaler(avtaleliste):
	return sorted(avtaleliste)


# Mine funksjoner
def get_avtale_string(avtale):
	avtaledata = avtale.split(";")
	fra = formater_klokkeslett(avtaledata[0])
	til = formater_klokkeslett(avtaledata[1])
	navn = avtaledata[2]
	lokasjon = avtaledata[3]
	status = avtaledata[4].lower()

	status = get_file_content(status.strip() + ".txt")

	return f"{status}.png - {navn} ({lokasjon}) - Fra {fra} til {til}\n"


def get_file_content(filename):
	with open(filename) as file:
		return file.read()


foreleser_navn = "Lars Emil"
filnavn = "avtaler.dat"

if __name__ == '__main__':
	print("#################################")
	print(f"####Kalender for {foreleser_navn}#######")
	print("#################################")

	date_time_string = "2018-12-03T12:30:00"
	now = datetime.fromisoformat(date_time_string)
	today = now.date()

	with open(filnavn) as avtalefil:
		avtaler = avtalefil.readlines()

	avtaler = sorter_avtaler(avtaler)

	avtale_naa = ""
	avtaler_i_dag = ""

	for avtale in avtaler:
		avtaledata = avtale.split(";")
		fra = avtaledata[0]
		til = avtaledata[1]

		if aktiv(fra, til, now):
			avtale_naa += get_avtale_string(avtale)
		elif innenfor_dato(fra, til, today):
			avtaler_i_dag += get_avtale_string(avtale)


	print("****NÅ*****")
	print(avtale_naa)

	print("****I DAG*****")
	print(avtaler_i_dag)




