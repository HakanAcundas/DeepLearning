#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


class traveler():
    
    def __init__(self, start_x = 0, start_y = 0, totalmove = 10, target_x = 5, target_y = 5, possiblemoves = ["up", "right", "left"]):
       
        self.totalmove = totalmove;
        self.x = start_x;
        self.y = start_y;
        self.target_x = target_x
        self.target_y = target_y
        self.allxmoves, self.allymoves = [start_x], [start_y];
        self.possiblemoves = possiblemoves;
        self.traveler_past = [];
        self.move = {"up": self.up, "left": self.left, "right": self.right}
        self.think_steps()
        self.move_steps()
    
    def up(self):
        self.y = self.y + 1
        
    def right(self):
        self.x = self.x + 1
    
    def left(self):
        self.x = self.x - 1
    
    def think_steps(self):
        self.traveler_past = np.random.choice(self.possiblemoves, self.totalmove)
    
    
        
    def move_steps(self):
        for step in self.traveler_past:
            self.move[step]()
            self.allxmoves.append(self.x)
            self.allymoves.append(self.y)
    
    
    def set_gene(self, new_gene):
        self.traveler_past = new_gene
    
    
    def fitness(self):
        error_x = (self.target_x - self.allxmoves[-1])
        error_y = (self.target_y - self.allymoves[-1])
        return 1/(1 + np.sqrt(error_x**2 + error_y**2))
    
    def draw(self, verbose = True):
        if verbose: print(self.traveler_past)
        plt.plot(self.target_x, self.target_y, 'g*', markersize=30)
        plt.plot(self.allxmoves[-1], self.allymoves[-1], 'r^', markersize=25)
        plt.plot(self.allxmoves, self.allymoves)
        plt.axis((-2,self.target_x+2,0,self.target_y+2))
        plt.grid()
        


# In[3]:


a=traveler()


# In[4]:


a.think_steps()
a.traveler_past


# In[5]:


a.allxmoves


# In[14]:


class evolution():
    def __init__(self, max_popu = 10):
        self.max_popu = max_popu
        
        self.population = [traveler() for travelers in range(max_popu)]
        
        self.fitness_values = [self.population[i].fitness() for i in range(max_popu)]
        
        sum_fitness = sum(self.fitness_values)
        
        self.again_select_prob = [traveler_value/sum_fitness for traveler_value in self.fitness_values]
        
        self.best_traveler = self.population[np.argmax(self.fitness_values)]
        
    def selection(self):
        parents = np.random.choice(self.max_popu, 2, self.again_select_prob)
        return parents
    
    def crossover(self, parent0, parent1):
        cutoff = np.random.randint(len(parent0.traveler_past))
        child = np.concatenate((parent0.traveler_past[:cutoff], parent1.traveler_past[cutoff:]))
        return child
    
    def create_new_child(self):
        parents = self.selection()
        p0, p1 = self.population[parents[0]], self.population[parents[1]]
        child_traveler = traveler()
        child_traveler_past = self.crossover(p0, p1)
        child_traveler.set_gene(child_traveler_past)
        
        return child_traveler
    
    def create_new_gen(self):
        new_population = [self.create_new_child() for i in range(self.max_popu - 1)] + [self.best_traveler]
        self.population = new_population
        self.fitness_values = [self.population[i].fitness() for i in range(self.max_popu)]
        total_fitness = sum(self.fitness_values)
        self.reproduction_probabiliy = [val/total_fitness for val in self.fitness_values]
        self.best_traveler = self.population[np.argmax(self.fitness_values)]
        
        
    def evolve(self, times = 10):
        for i in range(times):
            self.create_new_gen()
        return self.best_traveler
        


# In[15]:


travelers = evolution()
travelers.best_traveler.draw()


# In[16]:


travelers.evolve()
travelers.best_traveler.draw()


# In[17]:


travelers.evolve()
travelers.best_traveler.draw()


# In[ ]:




