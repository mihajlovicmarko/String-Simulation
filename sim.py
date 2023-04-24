import numpy as np

class String():
    def __init__(self, velocity, array):
        self.V = velocity
        self.V2 = velocity **2
        self.velArray = np.zeros(np.shape(array)[0] - 2)
        self.accArray = np.zeros(np.shape(array)[0] - 2)
        self.array = array
        
        
    def Derivative(self, array):
        d_array = array[1:] - array[:-1]
        return d_array
    
    
    def Update(self, n_iter, updates_per_second):
        
        self.arrayMatrix = np.zeros((n_iter, self.array.shape[0]))
        self.EnergyKinetic = np.zeros((n_iter))
        self.EnergyPotential = np.zeros((n_iter))
        for i in range(n_iter):
            #print(i)
            self.accArray = self.Derivative(self.Derivative(self.array)) * self.V2 / updates_per_second
            self.velArray +=  self.accArray
            self.array[1:-1] += self.velArray / updates_per_second
            self.arrayMatrix[i] = self.array
            self.EnergyPotential[i] = np.sum(np.square((self.Derivative(self.array))))
            self.EnergyKinetic[i] = np.sum(np.square(self.velArray)) / self.V ** 2
            
        return self.arrayMatrix, self.EnergyPotential, self.EnergyKinetic
