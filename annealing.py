import time
import sys
import itertools
import math
import random
import copy

s = '''{0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0},

{0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0}, 

{1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1}, 

{1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1}, 

{1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1}, 

{0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0}, 

{1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0}, 

{1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0}, 

{1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0}, 

{0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0}, 

{1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0}, 

{1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1}, 

{0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1}, 

{0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1}, 

{0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1}, 

{0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1}, 

{1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1}, 

{1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1}, 

{0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1}, 

{1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1}'''


l = s.splitlines()
l = [x for x in l if x.strip()]
l = map(lambda x:[c for c in x if c in '01'], l)

representation_1 = l

l = []

for thing in representation_1:
 l.append(set())
 for i, item in enumerate(thing):
  if item is '1':
   l[-1].add(i)

representation_2 = l

representation_3 = map(lambda x: set(range(20)) - x, representation_2)

def neighbor(selection, max_distance = 1):
 # distance : flipping pairs of bits
 new_selection = copy.deepcopy(selection)
 if max_distance > 100:
  max_distance = 100
 if max_distance < 0:
  return new_selection
 so_far = 0
 so_far_small = set()
 while so_far < max_distance:
  patient_num = random.randint(0,19)
  patient_record = new_selection[patient_num]
  not_patient_record = representation_2[patient_num] - patient_record
  one_index = random.sample(patient_record, 1)[0]
  zero_index = random.sample(not_patient_record, 1)[0]
  if (patient_num, one_index) not in so_far_small and (patient_num, zero_index) not in so_far_small:
   so_far_small.add((patient_num, one_index))
   so_far_small.add((patient_num, zero_index))
   so_far += 1
   new_selection[patient_num].add(zero_index)
   new_selection[patient_num].remove(one_index)
 return new_selection

def selection_solution(selection):
 solution = []
 for patient in selection:
  solution.append([0]*21)
  for medicine in patient:
   solution[-1][medicine] = 1
 return solution

def solution_selection(solution):
 selection = []
 for k in range(20):
  selection.append(set())
  for j in range(21):
   if solution[k][j]:
    selection[-1].add(j)
 return selection

def solution_distance(solution_1, solution_2):
 return sum([sum([a!=b for a,b in zip(x,y)]) for x,y in zip(solution_1, solution_2)])

distance_solution = solution_distance

def selection_distance(selection_1, selection_2):
 return solution_distance(selection_solution(selection_1), selection_solution(selection_2))

distance_selection = selection_distance

def score_selection(selection):
 all_pairs = set()
 for item in selection:
  for pair in itertools.combinations(item, 2):
   s = map(str, sorted(list(pair)))
   all_pairs.add(','.join(s))
 return len(all_pairs)

def score_solution(solution):
 selection = solution_selection(solution)
 return score_selection(selection)

energy = score_selection

def random_selection():
 selection = []
 for level_number in range(20):
  selection.append(set(random.sample(representation_2[level_number], 5)))
 return selection

def random_solution():
 return selection_solution(random_selection())

def temperature_exp(alpha = 0.999, start = 300):
 # T = (alpha ^ k) * start
 def temp(k):
  return (alpha ** k) * (float(start))
 return temp

def temperature_lin(m = -0.01, start = 300):
 # T = start + m*k
 def temp(k):
  return start + m * k
 return temp

def distance_f(temperature):
 # returns a distance for neighbor, based on temperature
 return 1

def probability_f(energy_s, energy_n, T):
 # probability that we switch
 if energy_n >= energy_s:
  return 1
 if T <= 0.00000001:
  return T
 return math.exp((energy_s - energy_n)/T)

def anneal(max_k = 1000, temperature = temperature_exp(), probability = probability_f, distance = distance_f, selection = None):
 last_time = 0
 if selection is None:
  selection = random_selection()
 max_energy = energy(selection)
 current_energy = max_energy
 best_selection = selection
 for k in range(max_k):
  T = temperature(k)
  N = neighbor(selection, distance(T))
  neighbor_energy = energy(N)
  if time.time() > last_time + 0.25:
   last_time = time.time()
   sys.stdout.flush()
   sys.stdout.write('Now: E={0},T={1} | Neighbor: E={2},D={3} | Best: E={4},D={5} | k={6}/{7}\r'.format(
    str(current_energy).center(3, ' '), str(T)[:5].center(5, ' '), str(neighbor_energy).center(3, ' '),
    str(distance_selection(N, selection)).center(3, ' '), str(max_energy).center(3, ' '), 
    str(distance_selection(best_selection, selection)).center(3, ' '), str(k+1).center(len(str(max_k)), ' '), max_k))
  if neighbor_energy > max_energy:
   max_energy = neighbor_energy
   best_selection = N
  if probability(current_energy, neighbor_energy, T) >= random.random():
   selection = N
   current_energy = neighbor_energy
 print '\b'
 return best_selection

