from .Manejador import Manejador, ExcepcionManejador


def main():
	print("-------------------------------------------------------------------------------------------------------")
	print("Bienvenido al manejador de tipos de datos")
	print("\nIMPORTANTE:\n- Los comandos son insensibles a mayúsculas y minúsculas")
	print("- Las listas de [<tipo>] deben estar separadas por espacios")
	print("- Los tipos de las listas deben ser definidos con anterioridad")
	print("- Los valores de <representacion> y <alineacion> deben ser numeros enteros positivos y ")
	print("  representan la cantidad de bytes que ocupa el tipo y la alineación del mismo respectivamente\n")
	print("Comandos disponibles:")
	print("ATOMICO <nombre> <representación> <alineación> - Define un nuevo tipo atomico")
	print("STRUCT <nombre> [<tipo>] - Define un nuevo registro")
	print("UNION <nombre> [<tipo>] - Define un nuevo tipo union")
	print("DESCRIBIR <nombre> - Muestra la descripción del tipo")
	print("SALIR - Sale del programa")
	print("-------------------------------------------------------------------------------------------------------\n")

	manejador = Manejador()
	while True:
		entrada = input(">>> ").upper().strip().split(" ")

		match entrada:
			case ["SALIR"]:
				break

			case ["ATOMICO", nombre, representacion, alineacion]:
				try:
					manejador.definirAtomico(nombre, representacion, alineacion)
				except ExcepcionManejador as e:
					print("ERROR:", e)
				except Exception as e:
					print("Uso del comando ATOMICO: ATOMICO <nombre> <representación> <alineación>")
			
			case ["STRUCT", nombre, *tipo]:
				try:
					manejador.definirStruct(nombre, *tipo)
				except ExcepcionManejador as e:
					print("ERROR:", e)
				except Exception as e:
					print("Uso del comando STRUCT: STRUCT <nombre> [<tipo>]")

			case ["UNION", nombre, *tipo]:
				try:
					manejador.definirUnion(nombre, *tipo)
				except ExcepcionManejador as e:
					print("ERROR:", e)
				except Exception as e:
					print("Uso del comando UNION: UNION <nombre> [<tipo>]")

			case ["DESCRIBIR", nombre]:
				try:
					descripcion = manejador.getDescripcionSinEmpaquetar(nombre)
					print("\nSin empaquetar:")
					print(f"Tipo: {descripcion['tipo']}")
					print(f"Representacion: {descripcion['representacion']}")
					print(f"Alineacion: {descripcion['alineacion']}")
					print(f"Desperdicio: {descripcion['desperdicio']}")

					descripcion = manejador.getDescripcionEmpaquetando(nombre)
					print("\nEmpaquetando:")
					print(f"Tipo: {descripcion['tipo']}")
					print(f"Representacion: {descripcion['representacion']}")
					print(f"Alineacion: {descripcion['alineacion']}")
					print(f"Desperdicio: {descripcion['desperdicio']}")

					descripcion = manejador.getDescripcionReordenando(nombre)
					print("\nReordenando:")
					print(f"Tipo: {descripcion['tipo']}")
					print(f"Representacion: {descripcion['representacion']}")
					print(f"Alineacion: {descripcion['alineacion']}")
					print(f"Desperdicio: {descripcion['desperdicio']}")
					print()

				except ExcepcionManejador as e:
					print("ERROR:", e)
				except Exception as e:
					print("Uso del comando DESCRIBIR: DESCRIBIR <nombre>")

			case ["ATOMICO", *_]:
				print("Uso del comando ATOMICO: ATOMICO <nombre> <representación> <alineación>")
			case ["STRUCT", *_]:
				print("Uso del comando STRUCT: STRUCT <nombre> [<tipo>]")
			case ["UNION", *_]:
				print("Uso del comando UNION: UNION <nombre> [<tipo>]")
			case ["DESCRIBIR", *_]:
				print("Uso del comando DESCRIBIR: DESCRIBIR <nombre>")

			case [""]:
				pass

			case _:
				print("Comando no reconocido")


if __name__ == "__main__":
	main()