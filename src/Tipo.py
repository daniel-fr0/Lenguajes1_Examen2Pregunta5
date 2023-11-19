class Tipo():
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.nombre == other.nombre
		return self.nombre == other
	
	def __ne__(self, other):
		return not(self == other)
	
	def __hash__(self):
		return hash(self.nombre)
	
	def __repr__(self):
		return self.__str__()
	
	def getDescripcionSinEmpaquetar(self):
		raise NotImplementedError
	
	def getDescripcionEmpaquetando(self):
		raise NotImplementedError
	
	def getDescripcionReordenando(self):
		raise NotImplementedError