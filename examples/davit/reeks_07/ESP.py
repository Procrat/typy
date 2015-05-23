'''
Created on Mar 3, 2015

@author: david
'''
import random
def taboeLengte(lijst,minimum = None, maximum = None):
    if(minimum == None or minimum < 0):
        minimum = 0
    
    if(maximum == None or maximum > len(lijst)):
        maximum = len(lijst)
        
    return random.randint(minimum,maximum)
    
        
def taboeWoorden(lijst,minimum = None, maximum = None):
    return sorted(random.sample(lijst,taboeLengte(lijst,minimum,maximum)))

woorden = ['forest', 'meadow', 'scenery', 'hills']
print(taboeWoorden(woorden, minimum = 2))