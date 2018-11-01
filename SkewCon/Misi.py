
from scipy.stats import skewnorm
import numpy as np


class misi:

    def __init__(self, matrix_x, matrix_y):
        
        self._X = matrix_x
        self._Y = matrix_y
        self._Concat = np.concatenate((self._X, self._Y),axis = 0)  

    def fit_matrices(self):

        # fit matrices with a skew normal distribution
        skewnorm.fit(self._X)
