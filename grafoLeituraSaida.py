import grafo 

# Função que faz a leitura de um grafo em txt
def lerGrafo(g, arquivo):
	with open(arquivo, 'r') as f:
		linhas = f.readlines()
	# Lê o número de vértices
	vertices = int(linhas[0].strip())
	# Cria matriz de adjacência para o grafo no txt
	matrizAdj = [[0] * vertices for _ in range(vertices)]
	for linha in linhas[1:]:
		valores = linha.strip().split()
		origem, destino, peso = int(valores[0]), int(valores[1]), float(valores[2])
		matrizAdj[origem - 1][destino - 1] = peso
		matrizAdj[destino - 1][origem - 1] = peso
		
	# Cria um grafo com as informações de grafo.txt
	g.v = vertices
	g.matrizAdj = matrizAdj
	g.arestas = (len(linhas)-1)
	return g

def printMST(g, arquivoSaida, pai):
		with open(arquivoSaida, 'a') as mst:
			mst.write('\n\nMST: \n')
			mst.write('Aresta/Peso \n')
			pesoTotal = 0
			for i in range(1, g.v):
				pesoTotal = pesoTotal + g.matrizAdj[i][pai[i]]
				mst.write(str(pai[i] + 1))
				mst.write(' ')
				mst.write(str(i + 1))
				mst.write(' ')
				mst.write(str(g.matrizAdj[i][pai[i]]))
				mst.write('\n')
			mst.write('Peso total: ')
			mst.write(str(pesoTotal))
			mst.write('\n')
		mst.close()

def printDadosGrafo (g, arquivoSaida):
	with open(arquivoSaida, 'a') as saida:
		saida.write('\nnum de vertices: '+ str(g.v))
		saida.write('\nnum de arestas: '+  str(g.arestas))
		saida.write('\nGrau medio: '+  str(g.calcular_grau_medio())+'\n\n')
		saida.write("Distribuicao Empirica:\n")
		distribuicao_empirica = g.calcular_distribuicao_empirica()
		saida.write(distribuicao_empirica)
	saida.close()

def printBFS(g, arquivoSaida, vis):
	with open(arquivoSaida, 'a') as BFS:
		BFS.write(str(vis + 1))
		BFS.write(' ')
	BFS.close()

def printDFS(g, arquivoSaida, vertice):
	with open(arquivoSaida, 'a') as DFS:
		DFS.write(str(vertice + 1))
		DFS.write(' ')
	DFS.close()