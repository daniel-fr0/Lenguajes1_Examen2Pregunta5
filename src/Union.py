from .Tipo import Tipo
from math import gcd

class Union(Tipo):
	def __init__(self, nombre, *tipo):
		self.nombre = nombre
		self.tipo = list(tipo)

	def __str__(self):
		return f"{self.nombre}: <{' | '.join([str(t) for t in self.tipo])}>"
	
	def getDescripcionSinEmpaquetar(self):
		alineacion = _mcm([t.getDescripcionSinEmpaquetar()["alineacion"] for t in self.tipo])
		representacion = max([t.getDescripcionSinEmpaquetar()["representacion"] for t in self.tipo])
		desperdicio = sum([t.getDescripcionSinEmpaquetar()["desperdicio"] for t in self.tipo])

		return {
			"tipo": "union",
			"representacion": representacion,
			"alineacion": alineacion,
			"desperdicio": desperdicio
		}
	
	def getDescripcionEmpaquetando(self):
		alineacion = _mcm([t.getDescripcionEmpaquetando()["alineacion"] for t in self.tipo])
		representacion = max([t.getDescripcionEmpaquetando()["representacion"] for t in self.tipo])
		desperdicio = sum([t.getDescripcionEmpaquetando()["desperdicio"] for t in self.tipo])

		return {
			"tipo": "union",
			"representacion": representacion,
			"alineacion": alineacion,
			"desperdicio": desperdicio
		}
	
	def getDescripcionReordenando(self):
		alineacion = _mcm([t.getDescripcionReordenando()["alineacion"] for t in self.tipo])
		representacion = max([t.getDescripcionReordenando()["representacion"] for t in self.tipo])
		desperdicio = sum([t.getDescripcionReordenando()["desperdicio"] for t in self.tipo])

		return {
			"tipo": "union",
			"representacion": representacion,
			"alineacion": alineacion,
			"desperdicio": desperdicio
		}
		
def _mcm(numeros):
	mcm = 1
	for n in numeros:
		mcm = mcm * n // gcd(mcm, n)
	return mcm