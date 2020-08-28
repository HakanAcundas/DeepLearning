"Hakan Acundaş"
import numpy as np


class Traveler():
    def __init__(self, Column=8, Row=8, movement_capacity=15,
                 possible_moves=["UP", "RIGHT", "LEFT"], x_Start=0, y_Start=0, x_target=7, y_target=7):

        self.x = x_Start
        self.y = y_Start
        self.x_target = x_target
        self.y_target = y_target
        self.movement_capacity = movement_capacity
        self.possible_moves = possible_moves
        self.all_History = []
        self.all_X_history = []
        self.all_Y_history = []
        self.go = {"UP": self.up, "RIGHT": self.right, "LEFT": self.left}

        self.Column = Column
        self.Row = Row
        self.map = []
        self.create_map()
        self.think_move()
        self.move()

    def up(self):
        self.change_index(self.y, self.x)
        if self.y == self.Column - 1:
            self.y = self.y
        else:
            self.y = self.y + 1
        self.change_index(self.y, self.x)

    def right(self):
        self.change_index(self.y, self.x)
        if self.x == self.Row:
            self.x = self.x
        else:
            self.x = self.x + 1
        self.change_index(self.y, self.x)

    def left(self):
        self.change_index(self.y, self.x)
        if self.x == 0:
            self.x = self.x
        else:
            self.x = self.x - 1
        self.change_index(self.y, self.x)

    def set_gene(self, new_gene):
        self.all_History = new_gene

    def think_move(self):
        self.all_History = np.random.choice(self.possible_moves, self.movement_capacity)

    def move(self):
        for step in self.all_History:
            self.go[step]()
            self.all_X_history.append(self.x)
            self.all_Y_history.append(self.y)

    def error(self):
        error_X = (self.x_target - self.all_X_history[-1])
        error_Y = (self.y_target - self.all_Y_history[-1])
        return 1 / (1 + np.sqrt(error_X ** 2 + error_Y ** 2))

    def create_map(self):

        for i in range(self.Column):
            mini_list = np.zeros(self.Row)
            self.map.append(mini_list)
        self.map[0][0] = 1
        self.map[self.x_target][self.y_target] = 2

    def show_map(self):
        for j in range(self.Column):
            print(self.map[j])
        print(self.all_History)

    def Column(self):
        return self.Column

    def Line(self):
        return self.Row

    def change_index(self, x, y):
        if x <= self.x_target and y <= self.y_target:
            self.map[x][y] = 1


class evolution():
    def __init__(self, max_popu=10):
        self.max_popu = max_popu

        self.population = [Traveler() for i in range(max_popu)]

        self.error_values = [self.population[i].error() for i in range(max_popu)]

        sum_error = sum(self.error_values)

        self.selecting_prob = [i / sum_error for i in self.error_values]

        self.best_travaler = self.population[np.argmax(self.error_values)]

    def selection(self):
        parents = np.random.choice(self.max_popu, 2, self.selecting_prob)
        return parents

    def crossover(self, p0, p1):
        cutpoint = np.random.randint(len(p1.all_History))
        child = np.concatenate((p0.all_History[:cutpoint], p1.all_History[cutpoint:]))
        return child

    def create_new_child(self):
        parents = self.selection()
        p0, p1 = self.population[parents[0]], self.population[parents[1]]
        child_traveler = Traveler()
        child_traveler_past = self.crossover(p0, p1)
        child_traveler.set_gene(child_traveler_past)
        return child_traveler

    def create_new_population(self):
        new_population = [self.create_new_child() for i in range(self.max_popu - 1)] + [self.best_travaler]
        self.population = new_population
        self.error_values = [self.population[i].error() for i in range(self.max_popu)]
        sum_error = sum(self.error_values)
        self.selecting_prob = [i / sum_error for i in self.error_values]
        self.best_travaler = self.population[np.argmax(self.error_values)]

    def evolve(self, n_times=30):
        for i in range(n_times):
            self.create_new_population()
        return self.best_travaler


c = evolution()
c.best_travaler.show_map()

c.evolve()
c.best_travaler.show_map()

c.evolve()
c.best_travaler.show_map()

c.evolve()
c.best_travaler.show_map()

c.evolve()
c.best_travaler.show_map()

c.evolve()
c.best_travaler.show_map()