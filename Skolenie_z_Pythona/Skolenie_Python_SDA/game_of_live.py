import numpy as np


class GameOfLife:
    def __init__(self, world_size, count_of_stages):
        self.count_of_stages = count_of_stages
        if world_size < 10:
            self.world_size = 10
        else:
            self.world_size = world_size
        self.stage = self.create_world()
        self.another_stage = self.stage
        self.temp_world = self.update_stages(self.stage)

    def create_world(self):
        matrix = np.zeros([self.world_size, self.world_size])
        matrix[1][4] = True
        matrix[2][5] = True
        matrix[3][3] = True
        matrix[3][4] = True
        matrix[3][5] = True
        return matrix

    def update_stages(self, initial):
        temp_life = np.zeros([self.world_size, self.world_size, 8])
        for m in range(self.world_size):
            for k in range(self.world_size):
                temp_life[m][k][0] = initial[(k + self.world_size - 1) % self.world_size][
                    (m + self.world_size - 1) % self.world_size]
                temp_life[m][k][1] = initial[(k + self.world_size - 1) % self.world_size][
                    (m + self.world_size) % self.world_size]
                temp_life[m][k][2] = initial[(k + self.world_size - 1) % self.world_size][
                    (m + self.world_size + 1) % self.world_size]
                temp_life[m][k][3] = initial[(k + self.world_size) % self.world_size][
                    (m + self.world_size - 1) % self.world_size]
                temp_life[m][k][4] = initial[(k + self.world_size) % self.world_size][
                    (m + self.world_size + 1) % self.world_size]
                temp_life[m][k][5] = initial[(k + self.world_size + 1) % self.world_size][
                    (m + self.world_size - 1) % self.world_size]
                temp_life[m][k][6] = initial[(k + self.world_size + 1) % self.world_size][
                    (m + self.world_size) % self.world_size]
                temp_life[m][k][7] = initial[(k + self.world_size + 1) % self.world_size][
                    (m + self.world_size + 1) % self.world_size]
        return temp_life

    def create_stage(self, initial, temp, another):
        counter = 0
        for i in range(len(initial)):
            for j in range(len(initial)):
                for k in range(8):
                    counter += temp[i][j][k]
                if not initial[i][j] and counter == 3:
                    another[i][j] = True
                elif initial[i][j] and (counter > 3 or counter < 2):
                    another[i][j] = False
                elif initial[i][j] and counter == 2:
                    another[i][j] = initial[i][j]
                counter = 0
        self.temp_world = self.update_stages(another)
        self.draw()

    def draw(self):
        for st in self.stage:
            for val in st:
                print(' # ' if val else ' . ', end='')
            print()
        print(end='\n\n\n')

    def start_life(self):
        for i in range(self.count_of_stages):
            self.create_stage(initial=self.stage, temp=self.temp_world, another=self.another_stage)


new_game = GameOfLife(15, 10)
new_game.start_life()

