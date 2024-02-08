#
# Brain of the bird
#

import numpy as np

from utils import sigmoid

class Brain:
    def __init__(self, nb_neurons: int = 5):
        # Initialize the neural network (the learning parameters)
        # FIXME
        pass

    def predict(self, normalized_x_dist: float, normalized_y_dist: float) -> int:
        # Make the prediction function using x distance and y distance as input
        # FIXME
        return np.random.uniform(0, 1) >= 0.85
        
    def mutate(self, mutation_rate=0.1):
        '''
        Mutate the parameters you have created in the init function
        mutation_rate=0.1 means we are going to mutate only 10% of the weights and biases
        '''
        # FIXME
        pass
