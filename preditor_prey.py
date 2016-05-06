#!/usr/local/bin/python
# simulate predator/prey populations over time using discretized Lotka-Voltera equations

import matplotlib.pyplot as pplot # import the graphing function
import argparse # for a flexible comandline interface
import os # to check for the next file save name to be used
from time import sleep # allow program to pause

# set up the parser to get user input. All input is optional
parser = argparse.ArgumentParser(description='Simulate the populations of a group of predators and prey over time.')
parser.add_argument('-d', '--days', type=int, default=10000, help='specify the number of days to simulate')
parser.add_argument('--pred', type=float, default=10, help='specify the starting number of predators')
parser.add_argument('--prey', type=float, default=100, help='specify the starting number of prey')
parser.add_argument('-f', '--filename', type=str, help='specify the starting number of prey', default='')

group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action='store_true', help='print detailed output as the program is running', default=0)
group.add_argument('-q', '--quiet', action='store_true', help='suppress all program output while running', default=0)

args = parser.parse_args()

pred_pop = [] # the predator population
prey_pop = [] # the prey population
days = args.days # the number of days to simulate
pred_init = args.pred # the initial number of predators
prey_init = args.prey # the initial number of prey
save_location = args.filename # user specified save location

# set the verbosity level
verbose = 1
if args.quiet: verbose -= 1
if args.verbose: verbose += 1

# constants that determine the growth and death rates 
a = 0.0008
b = 0.03
c = 0.006
d = 0.001

# add initial values to pred and prey population lists
pred_pop.append(pred_init)
prey_pop.append(prey_init)

# if verbose anounce program begining
if verbose >= 1:
   print("Running %s with \n initial predator level: %d, initial prey level: %d \n for %d days..." % (__file__, pred_init, prey_init, days))

# simulate population changes over time
for day in range(days-1):
   x = pred_pop[-1]
   y = prey_pop[-1]
   next_pred = max((x + a*x*y - b*x), 0)
   next_prey = max((y + c*y - d*x*y), 0)
   pred_pop.append(next_pred)
   prey_pop.append(next_prey)

   # if verbose is >= 2 print population levels after each step
   if verbose >=2:
      print("day: %d, \t pred pop: %d,\t prey pop: %d" % (day, next_pred, next_prey))
      sleep(.5)

pplot.plot(pred_pop, label="Predator population")
pplot.plot(prey_pop, label="Prey population")
pplot.legend()

# save the graph to a user supplied location, or to next graph[i]
path = os.path.abspath(__file__)[:-len(__file__)]+'graphs'
if save_location:
   pplot.savefig(save_location)
else:
   existing_graphs = os.listdir(path)
   i=1
   while True:
      next = 'graph'+str(i)+'.png'
      if next not in existing_graphs:
         break
      i+=1
   save_location = path+'/graph'+str(i)+'.png'
   pplot.savefig(save_location)

# if verbose print save location
if verbose >= 1:
   print("Graph saved to \n %s. \n Goodbye" % save_location)
