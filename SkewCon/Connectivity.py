

from Misi import misi

class Connectivity:
 
    def __init__(self, matrix_x, matrix_y):
     
     self._X = matrix_x
     self._Y = matrix_y
    
    # def calculate_wsmi(self):

    #     matrix_x = self._X
    #     matrix_y = self._Y

    def calculate_multiple_information_sharing_index(self):

        matrix_x = self._X
        matrix_y = self._Y

        # Calculate rank for both matrices - check independency

        # Create misi object

        connectivity_obj = misi(matrix_x, matrix_y)

        connectivity_obj.fit_matrices()



