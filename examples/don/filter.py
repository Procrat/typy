#!/bin/python3

import json
from datetime import datetime, timedelta

pc_lokalen = {}

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
    
class User:
    def __init__(self, name):
        self.name = name
        self.events = []
        self.lSpend = {}

    def addEvent(self, event):
        self.events.append(event)

    def addTimeSpent(self, lokaal, tijd):
        if lokaal not in self.lSpend:
            self.lSpend[lokaal] = timedelta()
        self.lSpend[lokaal] += tijd;

    def convert(self):
        for lokaal in self.lSpend:
            self.lSpend[lokaal] = self.lSpend[lokaal].seconds

#Laad alle namen van pc's in.
with open("data/pc.txt") as pc:
    for line in pc:
        lijst = line.split(" - ")
        pc_lokalen[lijst[0]] = lijst[1].strip()

vroegste = datetime.max

events = []

with open("data/we.log") as log:
    for line in log:
        lijst = line.strip().split(';')
        events.append(Event(lijst))
    #Stel vroegste tijd in
    log.seek(0)
    vroegste = Event(log.readline().strip().split(';')).tijd

vroegste = vroegste.replace(hour=0, minute=0, second=0)

perioden = []
pcs = {}
dag = vroegste
for event in events:
    if event.pc not in pcs:
        pcs[event.pc] = Pc()
    if event.log == "logon" and not pcs[event.pc].gebruiktDoor(event.user):
        pcs[event.pc].gebruik(event)
    elif event.log == "logoff" and pcs[event.pc].gebruiktDoor(event.user):
        perioden.append(pcs[event.pc].startevent)
        perioden.append(event)
    else:
        pcs[event.pc].__init__()
#perioden = sorted(perioden, key=lambda periode: periode.user)
users = {}
for event in perioden:
    if event.user not in users:
        users[event.user] = User(event.user)
    users[event.user].addEvent(event)

with open("users.json", "w") as file:
    file.write("[")
    for user in users:
        tijd = None;
        for event in users[user].events:
            if(event.log == "logon"):
                tijd = event.tijd
            else:
                users[user].addTimeSpent(pc_lokalen[event.pc], event.tijd - tijd)
        users[user].convert()
        file.write(json.dumps({
            "name": users[user].name,
            "time": users[user].lSpend
            }) + ",")
    file.write("]")