#!/bin/python3

import sys
from datetime import datetime, timedelta

pc_lokalen = {}
lokalen = {}

class Event:
    def __init__(self, lijst):
        self.lijst = lijst
        self.tijd = datetime.strptime(lijst[0].strip(), "%a %d.%m.%Y %H:%M:%S")
        self.pc = lijst[1]
        self.lokaal = pc_lokalen[lijst[1].strip()]
        self.user = lijst[2]
        self.log = lijst[3]
        self.logged = False
    
    def __str__(self):
        return ";".join(self.lijst)
    

class Pc:
    def __init__(self):
        self.inGebruik = False
        self.start = None
        self.naam = None
        
    def gebruiktDoor(self, naam):
        return self.inGebruik and naam == self.naam
    
    def gebruik(self, event):
        self.startevent = event
        self.naam = event.user
        self.start = event.tijd
        self.inGebruik = True
    
#Laad alle namen van pc's in.
with open(sys.argv[2]) as pc:
    for line in pc:
        lijst = line.split(" - ")
        pc_lokalen[lijst[0]] = lijst[1]

vroegste = datetime.max

with open(sys.argv[1]) as log:
    for line in log:
        lijst = line.strip().split(';')
        event = Event(lijst)
        if event.lokaal not in lokalen:
            lokalen[event.lokaal] = []
        lokalen[event.lokaal].append(event)
    #Stel vroegste tijd in
    log.seek(0)
    vroegste = Event(log.readline().strip().split(';')).tijd

vroegste = vroegste.replace(hour=0, minute=0, second=0)

for lokaal in lokalen:
    pcs = {}
    perioden = []
    dag = vroegste
    for event in lokalen[lokaal]:
        if event.pc not in pcs:
            pcs[event.pc] = Pc()
        if event.log == "logon" and not pcs[event.pc].gebruiktDoor(event.user):
            pcs[event.pc].gebruik(event)
        elif event.log == "logoff" and pcs[event.pc].gebruiktDoor(event.user):
            perioden.append(pcs[event.pc].startevent)
            perioden.append(event)
        else:
            pcs[event.pc].__init__()
    perioden = sorted(perioden, key=lambda periode: periode.tijd)
    gebruikers = 0
    tijdelijk = 0
    
    with open("visualisatie/lokalen/{0}.csv".format(lokaal.strip()), "w") as file:
        file.write("time,users\n")
        for event in perioden:
            while event.tijd > dag + timedelta(minutes=15):
                file.write("{0},{1}\n".format(dag.strftime("%x %H:%M"), tijdelijk))
                tijdelijk = gebruikers
                dag += timedelta(minutes = 15)
            if event.log == "logon":
                gebruikers += 1
                tijdelijk += 1
            else:
                gebruikers -= 1
