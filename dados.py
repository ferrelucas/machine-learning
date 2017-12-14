import csv

def loadAccess():
	X = []
	Y = []

	arquivo = open('acesso_pagina.csv', 'rb')
	leitor = csv.reader(arquivo)

	leitor.next()

	for home, comoFunciona, contato, comprou in leitor:
		X.append([int(home), 
			int(comoFunciona), 
			int(contato)])
		Y.append(int(comprou))

	return X, Y
