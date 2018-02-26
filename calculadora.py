#!/usr/bin/python3

import sys

def suma(num1, num2):
	return num1 + num2
def resta(num1, num2):
	return num1 - num2
def multiplicacion(num, num2):
	return num1 * num2
def division(num1, num2):
	return num1 / num2
funciones = {
	'suma': suma,
	'resta': resta,
	'multiplicacion': multiplicacion,
	'division': division
}


if __name__ == "__main__":
	if len(sys.argv) != 4:
		print('el numero de argumentos no es correcto')
		print('	Utiliza el formato: ./calculadora.py <operador> <numero1> <numero2>')
		sys.exit(1)
	try:
		num1 = float(sys.argv[2])
		num2 = float(sys.argv[3])
	except ValueError:
		print('¡Los numero no son validos')
		sys.exit(1)
	try:
		result = argv[1](num1, num2)
		print(result)
	except ZeroDivisionError:s
		print('No se puede dividir entre 0')
sys.exit(0)
