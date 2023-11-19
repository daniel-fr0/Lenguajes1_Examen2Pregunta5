import unittest
from src.Union import Union
from src.Atomico import Atomico
from src.Struct import Struct

class TestUnion(unittest.TestCase):
	def setUp(self):
		self.tipo = [
			Atomico("A", 2, 2),
			Atomico("B", 3, 3),
			Atomico("C", 4, 4),
		]
		self.union = Union("foo", *self.tipo)

	def test_init(self):
		self.assertEqual(self.union.nombre, "foo")
		self.assertEqual(self.union.tipo, self.tipo)

	def test_str(self):
		self.assertEqual(str(self.union), "foo: <A | B | C>")

	def test_getDescripcionSinEmpaquetar(self):
		self.assertEqual(self.union.getDescripcionSinEmpaquetar(), {
			"tipo": "union",
			"representacion": 4,
			"alineacion": 12,
			"desperdicio": 0
		})
	
	def test_getDescripcionEmpaquetando(self):
		self.assertEqual(self.union.getDescripcionEmpaquetando(), {
			"tipo": "union",
			"representacion": 4,
			"alineacion": 12,
			"desperdicio": 0
		})
	
	def test_getDescripcionReordenando(self):
		self.assertEqual(self.union.getDescripcionReordenando(), {
			"tipo": "union",
			"representacion": 4,
			"alineacion": 12,
			"desperdicio": 0
		})

	def test_nested(self):
		obra = Union(
			"obra",
			Union(
				"escultura",
				Atomico("marmol", 6, 6),
				Atomico("madera", 4, 4),
				Atomico("metal", 3, 3),
			),
			Union(
				"pintura",
				Atomico("oleo", 8, 8),
				Atomico("acrilico", 4, 4),
				Atomico("tempera", 2, 2),
			)
		)

		self.assertEqual(obra.getDescripcionSinEmpaquetar(), {
			"tipo": "union",
			"representacion": 8,
			"alineacion": 24,
			"desperdicio": 0
		})


	

if __name__ == '__main__':
	unittest.main()