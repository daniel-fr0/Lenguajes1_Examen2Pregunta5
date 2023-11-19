import unittest
from src.Atomico import Atomico

class TestAtomico(unittest.TestCase):
	def setUp(self):
		self.atomico = Atomico("test", 4, 2)

	def test_init(self):
		self.assertEqual(self.atomico.nombre, "test")
		self.assertEqual(self.atomico.representacion, 4)
		self.assertEqual(self.atomico.alineacion, 2)

	def test_str(self):
		self.assertEqual(str(self.atomico), "test")

	def test_getDescripcionSinEmpaquetar(self):
		description = self.atomico.getDescripcionSinEmpaquetar()
		self.assertEqual(description["tipo"], "atomico")
		self.assertEqual(description["representacion"], 4)
		self.assertEqual(description["alineacion"], 2)
		self.assertEqual(description["desperdicio"], 0)

	def test_getDescripcionEmpaquetando(self):
		description = self.atomico.getDescripcionEmpaquetando()
		self.assertEqual(description["tipo"], "atomico")
		self.assertEqual(description["representacion"], 4)
		self.assertEqual(description["alineacion"], 2)
		self.assertEqual(description["desperdicio"], 0)

	def test_getDescripcionReordenando(self):
		description = self.atomico.getDescripcionReordenando()
		self.assertEqual(description["tipo"], "atomico")
		self.assertEqual(description["representacion"], 4)
		self.assertEqual(description["alineacion"], 2)
		self.assertEqual(description["desperdicio"], 0)

if __name__ == '__main__':
	unittest.main()