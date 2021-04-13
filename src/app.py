from transition import Transition
from automaton import Automaton
from state import State
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
		if info in intial_or_final [1]:
			dict_states[info]['is_final'] = True
		
	return dict_states


def get_word(input_file:list)-> list:

	last = (len(input_file)-1)
	word = input_file[last]
	word = word.split(' : ')
	result = []

	for info in word[1]:
		result.append(info)

	return result


def salve_dot(transitions:list, inicial, final, nome:str):
	
	graph = pydot.Dot(label=nome, graph_type='digraph', bgcolor='gray')
	states = []
	num = 0

	
	graph.add_node(pydot.Node(num,shape = 'point'))
	my_edge = pydot.Edge(num, inicial)
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
			if info in final:
				graph.add_node(pydot.Node(info, shape='doublecircle'))
			else:
				graph.add_node(pydot.Node(info, shape='circle'))

		my_edge = pydot.Edge(origem, destino, label = estados[1])

		graph.add_edge(my_edge)
	
	graph.set_graph_defaults(rankdir='LR')
	graph.write_raw('assets/dot/output.dot')
	graph.write_png('assets/steps/output.png')


def reach_for(state, states):

	reach = []
	#if not not wrd:
	for info in states:
		estados = info.split(' ')
		origin = estados[0]
		word = estados[1]
		goal = estados[3]
		try:
			#print(estados)
			if state == origin:
				reach.append(goal)
				
		except IndexError as e:
			pass
	return reach
	# else:
	# 	return

	# #print(reach)

	# for info in reach:
	# 	#print(info)
	# 	try:
	# 		print(f'{wrd[0]}[{info}]')
	# 		wrd.pop(0)
	# 		reach_for(info, states, wrd)
			
	# 	except IndexError as e:
	# 		return

	# #print(wrd)


def load_states(states_dict: dict) ->list:

	dictionary_items = states_dict.items()
	states = []
	for item in dictionary_items:
		s = State(item[0], item[1]['is_initial'], item[1]['is_final'])
		states.append(s)

	return states


def load_transitions(states:list, transitions_raw:list):

	transitions = []

	for transition in transitions_raw:
		estados = transition.split(' ')
		origin = estados[0]
		word = estados[1]
		goal = estados[3]
		
		t = Transition(word,origin,goal)
		transitions.append(t)
	
	for info in transitions:
		for state in states:
			if info.get_origin() == state.get_name():
				info.set_origin(state)

			if info.get_goal() == state.get_name():
				info.set_goal(state)

		#print(f'{info.get_origin().get_name()} -{info.get_name()}-> {info.get_goal().get_name()}')

	return transitions 

def main():

	path = 'entrada.txt'

	input_file = open_input(path)
	transitions_raw = get_transitions(input_file)
	intial_or_final = initial_and_final(input_file)
	states_dict = get_states(transitions_raw, intial_or_final)
	word = get_word(input_file)

	states = load_states(states_dict)
	transitions = load_transitions(states, transitions_raw)

	a = Automaton('Automato Finito',word, transitions)
	
	inicial = a.get_initials()
	
	#print (inicial.get_name())
	
	walk = a.get_reach(inicial, word[0])
	word.pop(0)
	#print(walk)

	for w in word:
		walk = a.get_reach(walk, w)
		print(walk.get_name())

	steps = a.get_steps()

	print(steps)

	salve_dot(transitions_raw,inicial.get_name(), walk.get_name(), a.get_name())

	
	#print(states_dict)
	#a.walk()

	#for transition in transitions:

	#exit()
	#salve_dot(transitions_raw, intial_or_final)

	#reach = reach_for('s0', transitions_raw)
	#print(reach)

	
if __name__ == "__main__":
    main()