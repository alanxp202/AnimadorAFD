import json


def open_input(file_name: str)->list:

	linhas = []
	with open(file_name, 'rb') as file:
		for line in file:
			linhas.append(str(line).split("'")[1])

	entrada = []
	for line in linhas:
		entrada.append(line.split(r'\r')[0])
		
	return entrada


def main():
	arquivo_de_entrada = 'entrada.txt'

	open_input(arquivo_de_entrada)

if __name__ == "__main__":
    main()