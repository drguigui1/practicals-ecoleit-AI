#
# Brain of the bird
#

import numpy as np

from utils import sigmoid

class Brain:
    def __init__(self, nb_neurons: int = 5):
        scale = np.sqrt(6. / (2 + nb_neurons))
        self.h_layer = np.random.uniform(-scale, scale, (2, nb_neurons))
        self.o_layer = np.random.uniform(-scale, scale, (nb_neurons, 1))
        
        self.h_bias = np.zeros((1, nb_neurons))
        self.o_bias = np.zeros((1, 1))

    def predict(self, normalized_x_dist: float, normalized_y_dist: float) -> int:
        inpt = np.array([[normalized_x_dist, normalized_y_dist]])
        
        # Apply hidden layer transformation with bias
        hidden = sigmoid(np.dot(inpt, self.h_layer) + self.h_bias)
        
        # Apply output layer transformation with bias
        pred = sigmoid(np.dot(hidden, self.o_layer) + self.o_bias)
        pred = pred.item()

        return 1 if pred >= 0.5 else 0

        
    def mutate(self, mutation_rate=0.1):
        '''
        Mutate the parameters of 'h_layer', 'o_layer', 'h_bias', and 'o_bias'
        mutation_rate=0.1 means we are going to mutate only 10% of the weights and biases
        '''
        # Pour chaque paramètre (poids et biais), appliquer une mutation avec la probabilité définie par mutation_rate
        for param in [self.h_layer, self.o_layer, self.h_bias, self.o_bias]:
            # Déterminer quels éléments vont muter
            mutation_mask = np.random.rand(*param.shape) < mutation_rate
            # Appliquer la mutation uniquement sur les éléments sélectionnés
            param[mutation_mask] += np.random.normal(0, 0.1, size=param.shape)[mutation_mask]
