import io
import unittest
from unittest.mock import patch
from src.repl import main

class TestExpresionesAritmeticas(unittest.TestCase):

	def testExit(self):
		with patch('builtins.input', side_effect=['SALIR']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[1], 'Bienvenido al manejador de tipos de datos')

	def testAtomico(self):
		with patch('builtins.input', side_effect=['ATOMICO INT 4 4', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				# Significa que no hubo output
				self.assertEqual(output[-1], "-------------------------------------------------------------------------------------------------------")

	def testStruct(self):
		with patch('builtins.input', side_effect=['ATOMICO INT 4 4', 'STRUCT PUNTO INT INT', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				# Significa que no hubo output
				self.assertEqual(output[-1], "-------------------------------------------------------------------------------------------------------")

	def testUnion(self):
		with patch('builtins.input', side_effect=['ATOMICO INT 4 4', 'ATOMICO CHAR 1 2', 'UNION VALOR INT CHAR', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				# Significa que no hubo output
				self.assertEqual(output[-1], "-------------------------------------------------------------------------------------------------------")

	def testDescribe(self):
		with patch('builtins.input', side_effect=[
			'atomico bool 1 2',
			'atomico int 4 4',
			'atomico char 1 1',
			'atomico double 8 8',
			'struct meta int char char double bool',
			'describir meta',
			'salir'
		]):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-17:], [
					"Sin empaquetar:",
					"Tipo: struct",
					"Representacion: 17",
					"Alineacion: 32",
					"Desperdicio: 2",
					"",
					"Empaquetando:",
					"Tipo: struct",
					"Representacion: 15",
					"Alineacion: 16",
					"Desperdicio: 0",
					"",
					"Reordenando:",
					"Tipo: struct",
					"Representacion: 15",
					"Alineacion: 16",
					"Desperdicio: 0",
				])

	def testRedeclare(self):
		with patch('builtins.input', side_effect=[
			'atomico bool 1 2',
			'atomico int 4 4',
			'atomico char 1 1',
			'atomico double 8 8',
			'atomico double 8 8',
			'struct meta int char char double bool',
			'struct meta int char char double bool',
			'union bar int meta bool',
			'union bar int char bool',
			'salir'
		]):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-3:], [
					"ERROR: Redeclaración del tipo 'DOUBLE'",
					"ERROR: Redeclaración del tipo 'META'",
					"ERROR: Redeclaración del tipo 'BAR'"
				])

	def testUndefined(self):
		with patch('builtins.input', side_effect=[
			'atomico bool 1 2',
			'describir meta',
			'struct meta int char char double bool',
			'salir'
		]):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-2:], [
					"ERROR: El tipo 'META' no esta definido",
					"ERROR: El tipo 'INT' no esta definido"
				])

if __name__ == '__main__':
	unittest.main()