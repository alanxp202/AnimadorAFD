from transition import Transition
from automaton import Automaton
from state import State
import imageio
import pydot
import glob
import json
import sys
import os


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


def save_dot_and_png(automaton:Automaton, state_walk):
	
	ini = 0
	steps = 1
	graph = pydot.Dot(label=automaton.get_name(), graph_type='digraph', bgcolor='gray')

	for i in automaton.get_states():
		if i in automaton.get_initials_list():
			graph.add_node(pydot.Node(ini, shape = 'point'))
			my_edge = pydot.Edge(ini, i.get_name())
			graph.add_edge(my_edge)
			ini += 1
	
	for s in automaton.get_states():
		if s in automaton.get_finals_list():
			my_node = pydot.Node(s.get_name(), shape='doublecircle')
			graph.add_node(my_node)
		else:
			my_node = pydot.Node(s.get_name(), shape='circle')
			graph.add_node(my_node)
	
	for t in automaton.get_transitions():
		my_edge = pydot.Edge(t.get_origin().get_name(), t.get_goal().get_name(), label = t.get_name())
		graph.add_edge(my_edge)

	graph.set_graph_defaults(rankdir='LR')
	graph.write_raw(f'assets/dot/output_{steps}.dot')
	graph.write_png(f'assets/steps/output_{steps}.png')

	
	for s in state_walk:
		if s.get_origin() in automaton.get_finals_list():
			my_node = pydot.Node(s.get_origin().get_name(), shape='doublecircle', color='blue')
			graph.add_node(my_node)
			graph.write_raw(f'assets/dot/output_{steps}.dot')
			graph.write_png(f'assets/steps/output_{steps}.png')
			steps += 1
		else:
			my_node = pydot.Node(s.get_origin().get_name(), shape='circle', color='blue')
			graph.add_node(my_node)
			graph.write_raw(f'assets/dot/output_{steps}.dot')
			graph.write_png(f'assets/steps/output_{steps}.png')
			steps += 1

		my_edge = pydot.Edge(s.get_origin().get_name(), s.get_goal().get_name(), label = s.get_name(), color='blue')
		graph.del_edge(s.get_origin().get_name(), s.get_goal().get_name())
		graph.add_edge(my_edge)

		graph.write_raw(f'assets/dot/output_{steps}.dot')
		graph.write_png(f'assets/steps/output_{steps}.png')
		steps += 1

		my_node.set_color('black')
		graph.write_raw(f'assets/dot/output_{steps}.dot')
		graph.write_png(f'assets/steps/output_{steps}.png')
		steps += 1
		
		my_edge.set_color('black')
		graph.write_raw(f'assets/dot/output_{steps}.dot')
		graph.write_png(f'assets/steps/output_{steps}.png')
		steps += 1

		if s.get_goal() in automaton.get_finals_list():
			my_node = pydot.Node(s.get_goal().get_name(), shape='doublecircle', color='blue')
			graph.add_node(my_node)
			graph.write_raw(f'assets/dot/output_{steps}.dot')
			graph.write_png(f'assets/steps/output_{steps}.png')
			steps += 1
		else:
			my_node = pydot.Node(s.get_goal().get_name(), shape='circle', color='blue')
			graph.add_node(my_node)
			graph.write_raw(f'assets/dot/output_{steps}.dot')
			graph.write_png(f'assets/steps/output_{steps}.png')
			steps += 1


def save_gif(gif:int):
	
	png_dir = 'assets/steps/'
	images = []
	dire = os.listdir(png_dir)

	dire.sort(key=lambda dir:int(dir.split('_')[1].split('.')[0]))

	print(dire)
	for file_name in dire:
		if file_name.endswith('.png'):
			file_path = os.path.join(png_dir, file_name)
			images.append(imageio.imread(file_path))
	
	imageio.mimsave(f'assets/gif/gif_automato_{gif}.gif', images, duration=0.4,loop=1)
	
	for file in os.listdir('assets/steps/'):
		try:
			os.remove(f'assets/steps/{file}')
		except FileNotFoundError:
			pass


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
	
	inicial = a.get_initials_list()

	for i in inicial:
		a.start_reach(word,i)
		word = get_word(input_file)

	print(a.get_steps())
	
	gif = 1
	for s in a.get_steps():
		save_dot_and_png(a,s)
		save_gif(gif)
		gif += 1


if __name__ == "__main__":
    main()