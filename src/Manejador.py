from .Atomico import Atomico
from .Struct import Struct
from .Union import Union

class ExcepcionManejador(Exception):
	def __init__(self, mensaje):
		self.mensaje = mensaje
	
	def __str__(self):
		return self.mensaje

class Manejador():
	def __init__(self):
		self.atomicos = {}
		self.structs = {}
		self.uniones = {}

	def definirAtomico(self, nombre, representacion, alineacion):
		if nombre in self.atomicos or nombre in self.structs or nombre in self.uniones:
			raise ExcepcionManejador(f"Redeclaración del tipo '{nombre}'")
		
		self.atomicos[nombre] = Atomico(nombre, representacion, alineacion)

	def definirStruct(self, nombre, *tipo):
		if nombre in self.atomicos or nombre in self.structs or nombre in self.uniones:
			raise ExcepcionManejador(f"Redeclaración del tipo '{nombre}'")
		tipo = list(tipo)
		for i in range(len(tipo)):
			t = tipo[i]
			if t in self.atomicos:
				tipo[i] = self.atomicos[t]
			elif t in self.structs:
				tipo[i] = self.structs[t]
			elif t in self.uniones:
				tipo[i] = self.uniones[t]
			else:
				raise ExcepcionManejador(f"El tipo '{t}' no esta definido")		
			
		self.structs[nombre] = Struct(nombre, *tipo)

	def definirUnion(self, nombre, *tipo):
		if nombre in self.atomicos or nombre in self.structs or nombre in self.uniones:
			raise ExcepcionManejador(f"Redeclaración del tipo '{nombre}'")
		tipo = list(tipo)
		for i in range(len(tipo)):
			t = tipo[i]
			if t in self.atomicos:
				tipo[i] = self.atomicos[t]
			elif t in self.structs:
				tipo[i] = self.structs[t]
			elif t in self.uniones:
				tipo[i] = self.uniones[t]
			else:
				raise ExcepcionManejador(f"El tipo '{t}' no esta definido")
			
		self.uniones[nombre] = Union(nombre, *tipo)

	def getDescripcionSinEmpaquetar(self, nombre):
		if nombre in self.atomicos:
			return self.atomicos[nombre].getDescripcionSinEmpaquetar()

		elif nombre in self.structs:
			return self.structs[nombre].getDescripcionSinEmpaquetar()

		elif nombre in self.uniones:
			return self.uniones[nombre].getDescripcionSinEmpaquetar()
		
		else:
			raise ExcepcionManejador(f"El tipo '{nombre}' no esta definido")
	
	def getDescripcionEmpaquetando(self, nombre):
		if nombre in self.atomicos:
			return self.atomicos[nombre].getDescripcionEmpaquetando()

		elif nombre in self.structs:
			return self.structs[nombre].getDescripcionEmpaquetando()
		
		elif nombre in self.uniones:
			return self.uniones[nombre].getDescripcionEmpaquetando()

		else:
			raise ExcepcionManejador(f"El tipo '{nombre}' no esta definido")
		
	def getDescripcionReordenando(self, nombre):
		if nombre in self.atomicos:
			return self.atomicos[nombre].getDescripcionReordenando()
		
		elif nombre in self.structs:
			return self.structs[nombre].getDescripcionReordenando()

		elif nombre in self.uniones:
			return self.uniones[nombre].getDescripcionReordenando()

		else:
			raise ExcepcionManejador(f"El tipo '{nombre}' no esta definido")