#
# Class for the bird
#

import copy
import pygame
import random
from typing import List

from brain import Brain
from utils import change_color


class Bird:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        # This is where we build the brain of the Bird
        self.brain = Brain()

        self.y_speed = 0
        self.skin = change_color("images/bird.png", random.random() + 0.5, random.random() + 0.5, random.random() + 0.5)
        self.alive = True
        self.score = 0
        self.nb_jumps = 0
        self.delay = 0
        self.skins = []
        self.resolution = 50
        self.init_skins(self.resolution)
    
    def init_skins(self, resolution: int):
        for i in range(resolution):
            self.skins.append(pygame.transform.rotate(self.skin, 90 - i * (180 / resolution)))

    def move(self, x_obs: float, y_obs: int):
        if self.alive:
            self.y += self.y_speed
            self.y_speed += 0.2
            # You can also change the way the score is computed
            # Here the bird gain one point for each jump
            # FIXME
            self.score += 1
            self.delay -= 0.1

            normalized_x_dist = (x_obs - self.x) / 500
            normalized_y_dist = (self.y - y_obs) / 766
            prediction = self.brain.predict(normalized_x_dist, normalized_y_dist)

            # Update the condition if you have different prediction
            # FIXME
            if self.delay < 0 and prediction == 1:
                self.y_speed = -6.5
                self.nb_jumps += 1
                self.delay = 4
        else:
            self.x -= 0.7

    def check_alive(self, ground: float, x_obs: float, ysize: float, space: float):
        if self.y >= ground + 20:
            self.alive = False

        
        if x_obs + 130 >= self.x + 65 >= x_obs:
            if self.y + 5 < ysize or self.y + 50 > ysize + space:
                self.alive = False

    def __str__(self):
        return str(self.score)

    def replicate_bird_with_mutations(self) -> 'Bird':
        new_bird = Bird(self.x, self.y)
        new_bird.brain = copy.deepcopy(self.brain)
        new_bird.brain.mutate(mutation_rate=0.1)
        return new_bird


def generate_new_birds(sorted_birds: List[Bird]) -> List[Bird]:
    '''
    After an iteration generate new birds
    '''
    nb_birds_to_mutate = 10
    nb_birds_to_keep = 3
    top_performers = sorted_birds[:nb_birds_to_mutate]
    new_generation_with_mut = [performer.replicate_bird_with_mutations() for performer in top_performers]
    new_generation_with_mut += sorted_birds[:nb_birds_to_keep]

    for i in range(len(new_generation_with_mut), len(sorted_birds)):
        new_generation_with_mut.append(Bird(sorted_birds[i].x, sorted_birds[i].y))

    return new_generation_with_mut
