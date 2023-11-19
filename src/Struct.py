from .Tipo import Tipo
class Struct(Tipo):
	def __init__(self, nombre, *tipo):
		self.nombre = nombre
		self.tipo = list(tipo)

	def __str__(self):
		return f"{self.nombre}: {{{', '.join([str(t) for t in self.tipo])}}}"
	
	def getDescripcionSinEmpaquetar(self):
		alineacion = 0
		desperdicio = 0

		for t in self.tipo:
			descripcion = t.getDescripcionSinEmpaquetar()
			if alineacion % descripcion["alineacion"] != 0:
				desperdicio += descripcion["alineacion"] - (alineacion % descripcion["alineacion"])
				desperdicio += descripcion["desperdicio"]
				alineacion += descripcion["alineacion"] - (alineacion % descripcion["alineacion"])
			alineacion += descripcion["representacion"]

		# Se han ocupado la cantidad de bytes representados por alineacion hasta el momento
		representacion = alineacion

		# Alineacion es la potencia de 2 mayor o igual donde entra representacion
		alineacion = 2 if representacion < 2 else 2 ** (representacion - 1).bit_length()

		return {
			"tipo": "struct",
			"representacion": representacion,
			"alineacion": alineacion,
			"desperdicio": desperdicio
		}
	
	def getDescripcionEmpaquetando(self):
		representacion = sum([t.getDescripcionEmpaquetando()["representacion"] for t in self.tipo])
		alineacion = 2 if representacion < 2 else 2 ** (representacion - 1).bit_length()
		desperdicio = sum([t.getDescripcionEmpaquetando()["desperdicio"] for t in self.tipo])

		return {
			"tipo": "struct",
			"representacion": representacion,
			"alineacion": alineacion,
			"desperdicio": desperdicio
		}
	
	def getDescripcionReordenando(self):
		key = lambda t: t.getDescripcionReordenando()["alineacion"]
		
		# Se ordenan los tipos de mayor a menor alineacion
		tiposOrdenados = sorted(self.tipo, key=key, reverse=True)

		alineacion = 0
		desperdicio = 0

		for t in tiposOrdenados:
			descripcion = t.getDescripcionReordenando()
			if alineacion % descripcion["alineacion"] != 0:
				desperdicio += descripcion["alineacion"] - (alineacion % descripcion["alineacion"])
				desperdicio += descripcion["desperdicio"]
				alineacion += descripcion["alineacion"] - (alineacion % descripcion["alineacion"])
			alineacion += descripcion["representacion"]

		# Se han ocupado la cantidad de bytes representados por alineacion hasta el momento
		representacion = alineacion

		# Alineacion es la potencia de 2 mayor o igual donde entra representacion
		alineacion = 2 if representacion < 2 else 2 ** (representacion - 1).bit_length()

		return {
			"tipo": "struct",
			"representacion": representacion,
			"alineacion": alineacion,
			"desperdicio": desperdicio
		}