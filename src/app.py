from Automaton import Automaton
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


def treat_info(input:list, idx:int):

	intial_and_final = input[0]
	intial_and_final = intial_and_final.split(' ; ')
	initial = intial_and_final[0].split(', ')
	final = intial_and_final[1].split(', ')

	print(f'Inicial: {initial} \n Final: {final}')
	

def main():
	path = 'entrada.txt'

	input_file = open_input(path)
	initials = treat_info(input_file)

	#automato = Automaton('A1',)

if __name__ == "__main__":
    main()