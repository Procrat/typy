'''
Created on Feb 17, 2015

@author: david
'''
import re
aantal = int(input())
for i in range(0,aantal):
    print(re.sub(r'([AEIOUJaeiouj]+)p(?i)\1',r'\1',input()))
