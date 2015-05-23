'''
Created on Feb 12, 2015

@author: david
'''
from datetime import date
import math
naam  = input()
jaar = int(input())
leeftijd = (math.sqrt(4*jaar+1)+1)/2
if leeftijd.is_integer():
    gevraagd = leeftijd + jaar
    if gevraagd > date.today().year:
        print("%s wordt %i in %i."%(naam,leeftijd,gevraagd))
    else:
        print("%s was %i in %i."%(naam,leeftijd,gevraagd))
else:
    print("%s is geen lid van het Verbond der Wortels."%naam) 