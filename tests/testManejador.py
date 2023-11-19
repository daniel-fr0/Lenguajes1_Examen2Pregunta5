import unittest
from src.Manejador import Manejador, ExcepcionManejador

class testManejador(unittest.TestCase):
	def setUp(self):
		self.manejador = Manejador()
	
	def test_definirAtomico(self):
		self.manejador.definirAtomico("bool", 1, 2)
		self.assertEqual(self.manejador.atomicos["bool"].nombre, "bool")
		self.assertEqual(self.manejador.atomicos["bool"].representacion, 1)
		self.assertEqual(self.manejador.atomicos["bool"].alineacion, 2)

		with self.assertRaises(ExcepcionManejador):
			self.manejador.definirAtomico("bool", 1, 2)

	def test_definirStruct(self):
		self.manejador.definirAtomico("char", 1, 2)
		self.manejador.definirAtomico("int", 4, 4)
		self.manejador.definirStruct("foo", "char", "int")

		self.assertEqual(self.manejador.structs["foo"].nombre, "foo")
		self.assertEqual(self.manejador.structs["foo"].tipo, [self.manejador.atomicos["char"], self.manejador.atomicos["int"]])

		with self.assertRaises(ExcepcionManejador):
			self.manejador.definirStruct("foo", "char", "int")

	def test_definirUnion(self):
		self.manejador.definirAtomico("char", 1, 2)
		self.manejador.definirAtomico("int", 4, 4)
		self.manejador.definirStruct("foo", "char", "int")
		self.manejador.definirUnion("bar", "int", "foo", "int")

		self.assertEqual(self.manejador.uniones["bar"].nombre, "bar")
		self.assertEqual(self.manejador.uniones["bar"].tipo, [
			self.manejador.atomicos["int"],
			self.manejador.structs["foo"],
			self.manejador.atomicos["int"]
		])

		with self.assertRaises(ExcepcionManejador):
			self.manejador.definirUnion("foo", "char", "int")

	def test_getDescripcionSinEmpaquetar(self):
		self.manejador.definirAtomico("bool", 1, 2)
		self.manejador.definirAtomico("char", 1, 2)
		self.manejador.definirAtomico("int", 4, 4)
		self.manejador.definirStruct("foo", "char", "int")
		self.manejador.definirUnion("bar", "int", "foo", "int")

		self.assertEqual(self.manejador.getDescripcionSinEmpaquetar("bool"), {
			"tipo": "atomico",
			"representacion": 1,
			"alineacion": 2,
			"desperdicio": 0
		})

		self.assertEqual(self.manejador.getDescripcionSinEmpaquetar("char"), {
			"tipo": "atomico",
			"representacion": 1,
			"alineacion": 2,
			"desperdicio": 0
		})

		self.assertEqual(self.manejador.getDescripcionSinEmpaquetar("int"), {
			"tipo": "atomico",
			"representacion": 4,
			"alineacion": 4,
			"desperdicio": 0
		})

		self.assertEqual(self.manejador.getDescripcionSinEmpaquetar("foo"), {
			"tipo": "struct",
			"representacion": 8,
			"alineacion": 8,
			"desperdicio": 3
		})

		self.assertEqual(self.manejador.getDescripcionSinEmpaquetar("bar"), {
			"tipo": "union",
			"representacion": 8,
			"alineacion": 8,
			"desperdicio": 3
		})

		with self.assertRaises(ExcepcionManejador):
			self.manejador.getDescripcionSinEmpaquetar("baz")

	def test_getDescripcionEmpaquetando(self):
		self.manejador.definirAtomico("bool", 1, 2)
		self.manejador.definirAtomico("char", 1, 2)
		self.manejador.definirAtomico("int", 4, 4)
		self.manejador.definirStruct("foo", "char", "int")
		self.manejador.definirUnion("bar", "int", "foo", "int")

		self.assertEqual(self.manejador.getDescripcionEmpaquetando("bool"), {
			"tipo": "atomico",
			"representacion": 1,
			"alineacion": 2,
			"desperdicio": 0
		})

		self.assertEqual(self.manejador.getDescripcionEmpaquetando("char"), {
			"tipo": "atomico",
			"representacion": 1,
			"alineacion": 2,
			"desperdicio": 0
		})

		self.assertEqual(self.manejador.getDescripcionEmpaquetando("int"), {
			"tipo": "atomico",
			"representacion": 4,
			"alineacion": 4,
			"desperdicio": 0
		})

		self.assertEqual(self.manejador.getDescripcionEmpaquetando("foo"), {
			"tipo": "struct",
			"representacion": 5,
			"alineacion": 8,
			"desperdicio": 0
		})

		self.assertEqual(self.manejador.getDescripcionEmpaquetando("bar"), {
			"tipo": "union",
			"representacion": 5,
			"alineacion": 8,
			"desperdicio": 0
		})

		with self.assertRaises(ExcepcionManejador):
			self.manejador.getDescripcionEmpaquetando("baz")

	def test_getDescripcionReordenando(self):
		self.manejador.definirAtomico("bool", 1, 2)
		self.manejador.definirAtomico("char", 1, 2)
		self.manejador.definirAtomico("int", 4, 4)
		self.manejador.definirStruct("foo", "char", "int")
		self.manejador.definirUnion("bar", "int", "foo", "int")

		self.assertEqual(self.manejador.getDescripcionReordenando("bool"), {
			"tipo": "atomico",
			"representacion": 1,
			"alineacion": 2,
			"desperdicio": 0
		})

		self.assertEqual(self.manejador.getDescripcionReordenando("char"), {
			"tipo": "atomico",
			"representacion": 1,
			"alineacion": 2,
			"desperdicio": 0
		})

		self.assertEqual(self.manejador.getDescripcionReordenando("int"), {
			"tipo": "atomico",
			"representacion": 4,
			"alineacion": 4,
			"desperdicio": 0
		})

		self.assertEqual(self.manejador.getDescripcionReordenando("foo"), {
			"tipo": "struct",
			"representacion": 5,
			"alineacion": 8,
			"desperdicio": 0
		})

		self.assertEqual(self.manejador.getDescripcionReordenando("bar"), {
			"tipo": "union",
			"representacion": 5,
			"alineacion": 8,
			"desperdicio": 0
		})

		with self.assertRaises(ExcepcionManejador):
			self.manejador.getDescripcionReordenando("baz")


if __name__ == '__main__':
	unittest.main()