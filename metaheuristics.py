#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:35:32 2019

@author: jkpvsz
"""
# Packages
import numpy as np
from population import Population 
from opteval import benchmark_func as bf
import matplotlib.pyplot as plt

#def run():
    # Problem definition
num_dimensions = 2
num_agents = 50
num_iterations = 100
#problem = bf.Sphere(num_dimensions)
problem = bf.Rosenbrock(num_dimensions)
is_constrained = True
desired_fitness = 1E-6

problem.max_search_range = problem.max_search_range/100
problem.min_search_range = problem.min_search_range/100
    
    # Call optimisation method
#RandomSearch(problem, num_dimensions, num_agents, num_iterations, 
#                 desired_fitness, is_constrained)
    
#def RandomSearch(problem, num_dimensions = 2, num_agents = 30, 
#                     num_iterations = 100, desired_fitness = 1E-6, 
#                     is_constrained = True):
    
# Create population
pop = Population(problem,desired_fitness,num_agents,is_constrained)

# Initialise population with random elements uniformly distributed in space
pop.initialise_uniformly()

# -- plot population
plt.figure(1)
plt.ion()

plt.axis([-1.1,1.1,-1.1,1.1])
plt.plot(pop.positions[:,0],pop.positions[:,1],'ro')
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.pause(0.01)
plt.draw()

# Evaluate fitness values
pop.evaluate_fitness()

# Update population, global, etc
pop.update_population("all")
pop.update_particular("all")
pop.update_global("greedy")

# TODO initialise historical data

pop.cs_probability = 0.75

pop.metropolis_temperature = 10000
pop.metropolis_rate = 1

pop.de_mutation_scheme = ("current-to-best",1)
pop.de_f = 1.0
pop.de_cr = 0.2

pop.spiral_radius = 0.8
pop.radius_span = 0.4

pop.firefly_epsilon = "uniform"
pop.firefly_gamma = 1.0
pop.firefly_beta = 1.0
pop.firefly_alpha = 0.8

pop.cf_gravity = 0.001
pop.cf_alpha = 0.001
pop.cf_beta = 1.5
pop.cf_time_interval = 1.0

# Start optimisaton procedure
for iteration in range(1, num_iterations + 1):
    # Perform a perturbation
#    pop.random_search()
#    pop.random_sample()
#    pop.rayleigh_search()
#    pop.constricted_pso()
#    pop.inertial_pso()
#    pop.levy_flight()  
#    pop.mutation_de()
#    pop.local_random_walk()
#    pop.spiral_dynamic()
#    pop.firefly()
    pop.central_force()
    
#    pop.binomial_crossover_de()
#    pop.exponential_crossover_de()
        
    # Evaluate fitness values
    pop.evaluate_fitness()    

    # Update population, global
    pop.iteration = iteration
    pop.update_population("greedy")
    pop.update_global()
    
    # -- plot population
    plt.cla()
    plt.plot(pop.positions[:,0],pop.positions[:,1],'ro')
    plt.plot(pop.global_best_position[0],pop.global_best_position[1],'bo')
    plt.xlabel('x_1')
    plt.ylabel('x_2')
    plt.title(str(pop.global_best_fitness)+" at "+str(iteration))
    plt.axis([-1.1,1.1,-1.1,1.1])
    plt.pause(0.01)
    plt.draw()
    
    # Print information per iteration
    if (iteration % 10) == 0:
        print("[",iteration,"] -> ",pop.get_state())
        
plt.ioff()
plt.show()
