
class Arbre:
	def __init__(self, freq):
		self.freq = freq

	def estFeuille(self):
		""" return True ssi l'arbre est restreint à une feuille"""
		return (type(self) is Feuille)

	def frequence(self):
		return self.freq
	
	def setfrequence(self, freq):
		self.freq = freq
	
	def getcode(self):
		""" à réecrire avec les accesseur filsgauche, clé ..."""
		def build(self, prefix, dic):
			assert( (self.fg!=None and self.fd!=None) or (self.fg==None and self.fd==None) )
			if self.fg!=None and self.fd!=None:
				build(self.fg, prefix+'0', dic)
				build(self.fd, prefix+'1', dic)
			else:
				dic[self.symb] = prefix
		dic = dict()
		build(self,'',dic)
		return dic

	def draw(self):
		(lines,_) = self.drawing()
		for l in lines:
			print(l)

class Noeud(Arbre):
	def __init__(self, *args):
		""" le constructeur attend 2 ou 3 paramètres:
			Noeud(filsgauche, filsdroit, frequence)
			Noeud(filsgauche, filsdroit)
		"""
		if len(args)==3:
			(fg, fd, freq) = args
			Arbre.__init__(self, freq)
			self.fg, self.fd = fg, fd
		elif len(args)==2:
			(fg, fd) = args
			Arbre.__init__(self, None)
			self.fg, self.fd = fg, fd
		else:
			raise TypeError("Wrong number of arguments !")

	def __repr__(self):
		if self.freq:
			return "(%s, %s): %d" % (repr(self.fg), repr(self.fd), self.freq)
		else:
			return "(%s, %s)" % (repr(self.fg), repr(self.fd)) 
			
	def filsGauche(self):
		return self.fg
	
	def filsDroit(self):
		return self.fd
	
	def drawing(self):
		""" retourne (liste de lignes, position de la racine sur la première ligne) """
		root = "*"
		spaceBetweenTree = 3
		def assemble(fg, fd):
			linesg, cg = fg
			linesd, cd = fd
			widthg, widthd = len(linesg[0]), len(linesd[0])
			
			#print(linesg, cg, linesd, cd,spaceBetweenTree)
			c = (cg+(cd+widthg)+spaceBetweenTree)//2
			offset =  (cg+(cd+widthg)+spaceBetweenTree)% 2
			
			lines = [[" "]*(widthg+widthd+spaceBetweenTree-offset)]
			lines[0][c-1] = root
			lines[0] = "".join(lines[0])
			
			for i in range(1,c-cg):
				lines.append( [" "]*(widthg+widthd+spaceBetweenTree-offset) )
				lines[i][c-i-1] = "/"
				lines[i][c+i-1] = "\\"
				lines[i] = "".join(lines[i])
				
			for i in range(min(len(linesg),len(linesd))):
				lines.append(linesg[i]+(spaceBetweenTree-offset)*" "+linesd[i])
			if len(linesg) < len(linesd):
				for i in range( len(linesg), len(linesd)):
					lines.append(" "*widthg + " "*(spaceBetweenTree-offset) + linesd[i])
			if len(linesg) > len(linesd):
				for i in range( len(linesd), len(linesg)):
					lines.append(linesg[i]+ " "*(spaceBetweenTree-offset) +" "*widthd)
			
			return (lines,c)
		
		# Si l'arbre a un fg et un fd ...
		return assemble(self.fg.drawing(), self.fd.drawing()) 
	
	
	
class Feuille(Arbre):
	def __init__(self, *args):
		""" le constructeur attend 2 ou 3 paramètres:
			Feuille(symbole, frequence)
			Feuille(symbole)
		"""
		if len(args)==2:
			(s, freq) = args
			Arbre.__init__(self, freq)
			self.symb = s
		elif len(args)==1:
			(s, ) = args
			Arbre.__init__(self, None)
			self.symb = s
		else:
			raise TypeError("Wrong number of arguments!")
		
	def __repr__(self):
		if self.freq:
			return "<%s: %d>" % (repr(self.symb), self.freq)
		else:
			return "<%s>" % (repr(self.symb)) 

	def symbole(self):
		return self.symb

	def drawing(self):
		""" retourne (liste de lignes, position de la racine sur la première ligne) """
		return (["%s" % repr(self.symb)] , 2)


if __name__ == '__main__':
	import os
	# Determine this module's name from it's file name and import it.
	module_name = os.path.splitext(os.path.basename(__file__))[0]
	arbor = __import__(module_name)
	
	arbre1 = Noeud(Noeud(Noeud(Feuille('A'), Feuille('T')), Feuille('G')), Feuille('C'))
	print(arbre1)
	
	arbre1.draw()
	
	arbre2 = Noeud(arbre1,Noeud(arbre1,arbre1))
	arbre2.draw()
	