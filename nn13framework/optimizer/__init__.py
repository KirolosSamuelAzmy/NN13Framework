import numpy as np

class optimizer:
    pass

class batch_gradient_descent(optimizer):

    def __init__(self,model,learning_rate,batch_size,regularization_parameter=0):
        '''
        model is and nn13framework.neural_network.model() object
        
        Uses L2 Regularization
        '''
        self.learning_rate = learning_rate
        self.regularization_parameter = regularization_parameter
        self.batch_size = batch_size
        self.model = model

    def step(self,grad_loss):
        last_dx = grad_loss.T
        for i in reversed(range(len(self.model.layers))):
            dw , dx = self.model.layers[i].backward(last_dx)
            last_dx = dx
            #Update Rule
            if self.model.layers[i].is_activation:
                continue
            self.model.layers[i].weight -= (self.learning_rate*dw/self.batch_size + self.regularization_parameter*(self.model.layers[i].weight))
            #self.model.layers[i].weight[:,:-1] -= (self.learning_rate*dw[:,:-1]/self.batch_size + self.regularization_parameter*(self.model.layers[i].weight[:,:-1]))
            #self.model.layers[i].weight[:,-1] -= self.learning_rate*dw[:,-1]/self.batch_size
        self.model.weights = [layer.weight for layer in self.model.layers if layer.weight is not None]