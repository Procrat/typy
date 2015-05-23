class Verkaveling:
	def __init__(self, m, n):
		self.array = []
		self.m = m
		self.n = n
		if (n > 0):
			for x in range(0, m):
				self.array.append('#')
				if (n > 1):
					for y in range(0, n-1):
						self.array[x]+='#'
	
	def __str__(self):
		if (self.n > 0):
			for x in range(0, self.m):
				print((self.array[x]))
		return ''
	def reserveer(self, een, twee, *co):
		assert ((een < self.m) & (twee < self.n)), "Je kan niet reserveren buiten het Perceel."
		drie = een
		vier = twee
		if (len(co) > 0):
			assert co[0] > een, "FOUT"
			drie = co[0]
		if (len(co) > 1):
			assert co[1] > twee, "FOUT"
			vier = co[1]
		for x in range (een, drie+1):
			for y in range (twee, vier+1):
				assert self.array[x][y] == '#', "Perceel kan niet gereserveerd worden"
		for x in range(een, drie+1):
			l = list(self.array[x])
			for y in range(twee, vier+1):
				l[y] = '-'
			self.array[x] = ''.join(l)
	
	def grootstePerceel(self):
		max = 0
		current = 0
		for x1 in range(0, self.m-1):
			for y1 in range(0, self.n-1):
				for x2 in range(x1+1, self.m+1):
					for y2 in range(y1+1, self.n+1):
						if (self.isOk(x1,y1,x2,y2)):
							current = ((x2-x1)*(y2-y1))
						if (current>max):
							max = current
		return max
	def isOk(self, x1, y1, x2, y2):
		for x in range(x1, x2):
			for y in range(y1, y2):
				if (self.array[x][y] == '-'):
					return 0
		return 1 

verkaveling = Verkaveling(6, 6) 
print (verkaveling) 
print((verkaveling.grootstePerceel())) 
verkaveling.reserveer(3,0,5,2) 
print (verkaveling) 
print((verkaveling.grootstePerceel())) 
verkaveling.reserveer(0,3,2,5) 
print (verkaveling) 
print((verkaveling.grootstePerceel())) 
verkaveling.reserveer(2,2,3,3)
