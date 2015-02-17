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

def neighbor(solution, max_distance = 1):
 # distance : flipping pairs of bits
 new_solution = copy.deepcopy(solution)
 if max_distance > 100:
  max_distance = 100
 if max_distance < 0:
  return new_solution
 so_far = 0
 so_far_small = set()
 while so_far < max_distance:
  patient_num = random.randint(0,19)
  one_index = random.sample(representation_2[patient_num], 1)[0]
  zero_index = random.sample(representation_3[patient_num], 1)[0]
  if (patient_num, one_index) not in so_far_small and (patient_num, zero_index) not in so_far_small:
   so_far_small.add((patient_num, one_index))
   so_far_small.add((patient_num, zero_index))
   so_far += 1
   new_solution[patient_num][zero_index] = 1
   new_solution[patient_num][one_index] = 0
 return new_solution

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
  selection.append([])
  for j in range(21):
   if solution[k][j]:
    selection[-1].append(j)
 return selection

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

energy = score_solution

def random_selection():
 selection = []
 for level_number in range(20):
  selection.append(random.sample(representation_2[level_number], 5))
 return selection

def random_solution():
 return selection_solution(random_selection())

def temperature(k, alpha = 0.8, initial_temp = 250):
 return (alpha ** k) * (float(initial_temp))

def probability(energy_s, energy_n, T):
 if energy_n < energy_s:
  return 1
 if T <= 0.00000001:
  return T
 return math.exp(0-(energy_n - energy_s)/T)

def distance(temperature, strangeness = False):
 # returns a distance for neighbor, based on temperature
 if strangeness:
  # adjust this
  return 210. * (temperature / 300.)
 else:
  return 1

def anneal(max_k = 1000, alpha = 0.99, initial_temp = 250, solution = None, strangeness = False):
 if solution is None:
  solution = random_solution()
 max_score = energy(solution)
 best_solution = solution
 for k in range(max_k):
  T = temperature(k, alpha, initial_temp)
  N = neighbor(solution, distance(T, strangeness))
  score = energy(N)
  if score > max_score:
   max_score = score
   best_solution = N
  if probability(energy(solution), energy(N), T) > random.random():
   solution = N
 return best_solution
