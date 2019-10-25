# -*- coding: utf-8 -*-

nota1 = int (input("Digite a primeira nota: "))
nota2 = int (input("Digite a segunda nota: "))

soma = nota1 + nota2

if soma >= 6:
	print("Aprovado")
elif soma < 6:
	print("Reprovado")
else:
	print("Nota invalida")
