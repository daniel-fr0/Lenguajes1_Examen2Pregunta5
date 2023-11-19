from .Tipo import Tipo

class Atomico(Tipo):
	def __init__(self, nombre, representacion, alineacion):
		self.nombre = nombre
		self.representacion = int(representacion)
		self.alineacion = int(alineacion)

	def __str__(self):
		return self.nombre
	
	def getDescripcionSinEmpaquetar(self):
		return {
			"tipo": "atomico",
			"representacion": self.representacion,
			"alineacion": self.alineacion,
			"desperdicio": 0
		}
	
	def getDescripcionEmpaquetando(self):
		return {
			"tipo": "atomico",
			"representacion": self.representacion,
			"alineacion": self.alineacion,
			"desperdicio": 0
		}
	
	def getDescripcionReordenando(self):
		return {
			"tipo": "atomico",
			"representacion": self.representacion,
			"alineacion": self.alineacion,
			"desperdicio": 0
		}