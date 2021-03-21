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


def initial_and_final(input_file:list, option:int)-> list:

	intial_and_final = input_file[0]
	intial_and_final = intial_and_final.split(' ; ')
	result = []

	if option == 'inicial':
		result = intial_and_final[0].split(', ')
		result = intial_and_final[0].split(',')

	elif option == 'final':
		result = intial_and_final[1].split(',')
		result = intial_and_final[1].split(', ')

	return result


def get_transitions(input_file:list)-> list:

	result = input_file.copy()
	result.pop(0)
	size = len(result)
	result.pop(size-1)

	return result


def get_word(input_file:list)-> str:

	last = (len(input_file)-1)
	word = input_file[last]
	word = word.split(' : ')
	result = word[1]

	return result


def main():
	
	path = 'entrada.txt'

	input_file = open_input(path)
	initials = initial_and_final(input_file, 'inicial')
	finals = initial_and_final(input_file, 'final')
	transitions = get_transitions(input_file)
	word = get_word(input_file)

if __name__ == "__main__":
    main()