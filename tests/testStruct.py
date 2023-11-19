import unittest
from src.Struct import Struct
from src.Atomico import Atomico

class TestStruct(unittest.TestCase):
	def setUp(self):
		self.primitivos = {
			"bool" : Atomico("bool", 1, 2),
			"char" : Atomico("char", 1, 2),
			"int" : Atomico("int", 4, 4),
			"double" : Atomico("double", 8, 8)
		}
		self.tipos = [
			self.primitivos["int"],
			Atomico("char[2]", 2, 2),
			self.primitivos["int"],
			self.primitivos["double"],
			self.primitivos["bool"]
		]
		self.struct = Struct("meta", *self.tipos)

	def test_init(self):
		self.assertEqual(self.struct.nombre, "meta")
		self.assertEqual(self.struct.tipo, self.tipos)

	def test_str(self):
		self.assertEqual(str(self.struct), "meta: {int, char[2], int, double, bool}")

	def test_getDescripcionSinEmpaquetar(self):
		self.assertEqual(self.struct.getDescripcionSinEmpaquetar(), {
			"tipo": "struct",
			"representacion": 25,
			"alineacion": 32,
			"desperdicio": 6
		})

	def test_getDescripcionEmpaquetando(self):
		self.assertEqual(self.struct.getDescripcionEmpaquetando(), {
			"tipo": "struct",
			"representacion": 19,
			"alineacion": 32,
			"desperdicio": 0
		})
	
	def test_getDescripcionReordenando(self):
		self.assertEqual(self.struct.getDescripcionReordenando(), {
			"tipo": "struct",
			"representacion": 19,
			"alineacion": 32,
			"desperdicio": 0
		})

	def test_string(self):
		string = Struct(
			"string", 
			Atomico("char", 1, 1),
			Atomico("char", 1, 1),
			Atomico("char", 1, 1),
			Atomico("char", 1, 1),
		)
		self.assertEqual(string.getDescripcionSinEmpaquetar(), {
			"tipo": "struct",
			"representacion": 4,
			"alineacion": 4,
			"desperdicio": 0
		})
		self.assertEqual(string.getDescripcionEmpaquetando(), {
			"tipo": "struct",
			"representacion": 4,
			"alineacion": 4,
			"desperdicio": 0
		})
		self.assertEqual(string.getDescripcionReordenando(), {
			"tipo": "struct",
			"representacion": 4,
			"alineacion": 4,
			"desperdicio": 0
		})

	def test_charStruct(self):
		char4 = Struct(
			"char4", 
			Atomico("char", 1, 2),
			Atomico("char", 1, 2),
			Atomico("char", 1, 2),
			Atomico("char", 1, 2),
		)
		self.assertEqual(char4.getDescripcionSinEmpaquetar(), {
			"tipo": "struct",
			"representacion": 7,
			"alineacion": 8,
			"desperdicio": 3
		})
		self.assertEqual(char4.getDescripcionEmpaquetando(), {
			"tipo": "struct",
			"representacion": 4,
			"alineacion": 4,
			"desperdicio": 0
		})
		self.assertEqual(char4.getDescripcionReordenando(), {
			"tipo": "struct",
			"representacion": 7,
			"alineacion": 8,
			"desperdicio": 3
		})

	def test_nested(self):
		persona = Struct(
			"persona",
			Struct(
				"nombre",
				Atomico("primerNombre", 16, 16),
				Atomico("segundoNombre", 16, 16),
				Atomico("apellidoPaterno", 16, 16),
				Atomico("apellidoMaterno", 16, 16),
			),
			Struct(
				"fechaNacimiento",
				Atomico("dia", 4, 4),
				Atomico("mes", 4, 4),
				Atomico("año", 4, 4),
			),
		)
		self.assertEqual(persona.getDescripcionSinEmpaquetar(), {
			"tipo": "struct",
			"representacion": 76,
			"alineacion": 128,
			"desperdicio": 0
		})
	

if __name__ == '__main__':
	unittest.main()