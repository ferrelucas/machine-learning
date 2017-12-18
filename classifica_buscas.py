import pandas as pd
df = pd.read_csv('buscas.csv')
dfX = df[['home', 'logado', 'busca']]
dfY = df['comprou']
X = pd.get_dummies(dfX).values
Y = dfY.values

trainRation = 0.9

trainSize = int(trainRation * len(Y))
testSize = int(len(Y) - trainSize)
treino_dados = X[:trainSize]
treino_marcacoes = Y[:trainSize]

teste_dados = X[-testSize:]
teste_marcacoes = Y[-testSize:]




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


