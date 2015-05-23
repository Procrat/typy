import math

class Eiwit:
	def __init__(self, begintoestand, config=[]):
		if math.sqrt(len(begintoestand))%1==0:
			self.lengte=int(math.sqrt(len(begintoestand)))
			self.begin=[[0 for x in range(self.lengte)] for x in range(self.lengte)]
			if (len(config)):
				opvouwen(self,config)	
			for i in range(0,self.lengte):
				for j in range(0,self.lengte):
					self.begin[i][j]=begintoestand[j+i*self.lengte]
		else:
			raise AssertionError("Ongeldige begintoestand")

	def opvouwen(self, config=[]):
		self.configuratie=[]
		bool=1
		for element in config:
			if not((element[0]==element[2] and element[1]+1==element[3]) or (element[0]+1==element[2] and element[1]==element[3])):
				raise AssertionError("Ongeldige configuratie!")
					
		self.configuratie=config

								
	def bindingsenergie(self):
		energie=0
		for el in self.configuratie:
			nieuw=self.begin[el[0]][el[1]]*self.begin[el[2]][el[3]]
			energie=energie+nieuw
		return energie
	
	def __str__(self):
		output=[]
		output.append("+----"*(self.lengte)+"+")
		for i in range(0,self.lengte):
			string="|"
			for j in range(0, self.lengte):
				string+='{0:^4}'.format(str(self.begin[i][j]))
				if not j==self.lengte-1:
					string+=" "
			output.append(string+"|")
			if not i==self.lengte-1:
				output.append("+    "*(self.lengte)+"+")
			else:
				output.append("+----"*(self.lengte)+"+")
		return "\n".join(output)


eiwit = Eiwit([-2, 5, -4, 2, 4, -1, 2, 1, 3, 2, -5, 2, 5, -3, 6, 1])
eiwit.opvouwen([(1, 1, 1, 2), (2, 1, 2, 2), (3, 0, 3, 1), (1, 0, 2, 0), (0, 1, 1, 1), (1, 1, 2, 1), (0, 2, 1, 2), (2, 2, 3, 2), (1, 3, 2, 3)])
print((eiwit.bindingsenergie())) 
print(eiwit)
