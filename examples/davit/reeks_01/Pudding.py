'''
Created on Feb 12, 2015

@author: david
'''
amount = int(input())
price = float(input())
required = int(input())
miles = int(input())

cost = amount * price
coupons = amount // required
revenue = coupons * miles

print("Phillips spendeerde $%s voor %i frequent flyer mijlen." %(cost,revenue))