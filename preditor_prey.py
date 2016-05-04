#simulate preditor/prey populations over time using discretized Lotka-Voltera equations

import matplotlib.pyplot as pplot # import the graphing function
import argparse # for a flexible comandline interface

pred_pop = [] # the preditor population
prey_pop = [] # the prey population
days = 10000 # the number of days to simulate
pred_init = 10 # the initial number of preditors
prey_init = 100 # the initial number of prey
save_location = 'pred_prey_graphs/' + 'graph1' + '.png'

# constants that determine the growth and death rates 
a = 0.0008
b = 0.03
c = 0.006
d = 0.001

# add initial values to pred and prey population lists
pred_pop.append(pred_init)
prey_pop.append(prey_init)

# simulate population changes over time
for day in range(days-1):
   x = pred_pop[-1]
   y = prey_pop[-1]
   next_pred = max((x + a*x*y - b*x), 0)
   next_prey = max((y + c*y - d*x*y), 0)
   pred_pop.append(next_pred)
   prey_pop.append(next_prey)

pplot.plot(pred_pop, label="Preditor population")
pplot.plot(prey_pop, label="Prey population")
pplot.legend()
pplot.savefig(save_location)
