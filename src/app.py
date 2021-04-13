from automaton import Automaton
import pydot
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

def salve_dot(transitions:list, intial_or_final:list):
	
	graph = pydot.Dot('Automanto',graph_type='digraph', bgcolor='gray')
	states = []
	num = 0

	print( intial_or_final[0])

	for intial in intial_or_final[0]:
		graph.add_node(pydot.Node(num,shape = 'point'))
		my_edge = pydot.Edge(num, intial)
		graph.add_edge(my_edge)
		num+=1

	

	for info in transitions:
		estados = info.split(' ')
		origem = estados[0]
		destino = estados[3]

		if origem not in states:
			states.append(origem)
		if destino not in states:
			states.append(destino)

		for info in states:
			if info in intial_or_final[1]:
				graph.add_node(pydot.Node(info, shape='doublecircle'))
			else:
				graph.add_node(pydot.Node(info, shape='circle'))

		my_edge = pydot.Edge(origem, destino, label = estados[1])

		graph.add_edge(my_edge)
	
	graph.set_graph_defaults(rankdir='LR')
	graph.write_raw('assets/dot/output_raw.dot')
	graph.write_png('assets/steps/output.png')


def main():

	path = 'entrada.txt'

	input_file = open_input(path)
	transitions = get_transitions(input_file)
	intial_or_final = initial_and_final(input_file)
	states = get_states(transitions, intial_or_final)
	word = get_word(input_file)
	salve_dot(transitions, intial_or_final)
	#print(states)
	exit()
	automaton = Automaton(word, transitions, intial_or_final[0], intial_or_final[1])
	
	automaton.start_trasitions()
	print(automaton.to_string())

	#get_states(input_file)
	# intial_or_final = initial_and_final(input_file)
	# print(intial_or_final)

	# transitions = get_transitions(input_file)
	# print(transitions)

	# word = get_word(input_file)
	# print(word)

if __name__ == "__main__":
    main()