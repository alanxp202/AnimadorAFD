from automaton import Automaton
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


def initial_and_final(input_file:list)-> list:
	
	result = []
	intial_or_final = input_file[0]
	intial_or_final = intial_or_final.split(' ; ')
	
	initial = intial_or_final[0].split(' ')
	final = intial_or_final[1].split(' ')

	result.append(initial)
	result.append(final)

	return result


def get_transitions(input_file:list)-> list:

	result = input_file.copy()
	result.pop(0)
	size = len(result)
	result.pop(size-1)

	return result


def get_states(transitions:list, intial_or_final:list)-> list:

	dict_states = {}
	states = []
	
	for info in transitions:
		estados = info.split(' ')
		origin = estados[0]
		goal = estados[3]
		if origin not in states:
			states.append(origin)
		if goal not in states:
			states.append(goal)

	for info in states:
		dict_states[info] = {
			'is_initial': False,
			'is_final' : False
		}
		if info in intial_or_final [0]:
			dict_states[info]['is_initial'] = True
		elif info in intial_or_final [1]:
			dict_states[info]['is_final'] = True
		
	return dict_states

def get_word(input_file:list)-> str:

	last = (len(input_file)-1)
	word = input_file[last]
	word = word.split(' : ')
	result = word[1]

	return result


def main():

	path = 'entrada.txt'

	input_file = open_input(path)
	transitions = get_transitions(input_file)
	intial_or_final = initial_and_final(input_file)
	states = get_states(transitions, intial_or_final)
	word = get_word(input_file)

	automaton = Automaton(word, transitions, intial_or_final[0], intial_or_final[1])
	
	print(automaton.to_string())
	automaton.start_trasitinos()

	#get_states(input_file)
	# intial_or_final = initial_and_final(input_file)
	# print(intial_or_final)

	# transitions = get_transitions(input_file)
	# print(transitions)

	# word = get_word(input_file)
	# print(word)

if __name__ == "__main__":
    main()