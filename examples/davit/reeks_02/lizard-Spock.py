'''
Created on Feb 12, 2015

@author: david
'''
play1 = input()
play2 = input()

if play1 == play2:
    print("gelijkspel" )
elif play1 == "blad" and ( play2 == "steen" or play2 == "Spock"):
    print("speler1 wint")
elif play1 == "steen" and ( play2 == "schaar" or play2 == "hagedis"):
    print("speler1 wint")
elif play1 == "hagedis" and (play2 == "Spock" or play2 == "blad"):
    print("speler1 wint")
elif play1 == "Spock" and (play2 == "steen" or play2 == "schaar"):
    print("speler1 wint")
elif play1 == "schaar" and (play2 == "blad" or play2 == "hagedis"):
    print("speler1 wint")
else:
    print("speler2 wint")