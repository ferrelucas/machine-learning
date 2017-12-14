from dados import loadAccess

X,Y = loadAccess()

treino_dados = X[:90]
treino_marcacoes = Y[:90]

teste_dados = X[-9:]
teste_marcacoes = Y[-9:]
from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

result = modelo.predict(teste_dados)

diferencas = result - teste_marcacoes
acertos = [d for d in diferencas if d == 0]
totalAcertos = len(acertos)
totalElementos = len(teste_dados)

txAcerto = 100.0* totalAcertos/totalElementos

print txAcerto
print len(X)