# Algoritmo de Prim para árvore geradora mínima (MST) por meio da matriz de adjacência
import sys
from collections import deque
import math

class Grafo():
	# Construtor: Monta matriz de adjacência preenchida com zeros
	def __init__(self, vertices):
		self.v = vertices
		self.matrizAdj = [[0 for coluna in range(self.v)]
					for linha in range(vertices)]
		self.arestas=0
	
	def lerGrafo(self, arquivo):
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
		self.v = vertices
		self.matrizAdj = matrizAdj
		self.arestas = (len(linhas)-1)
		return self

	def printMST(self, arquivoSaida, pai):
			with open(arquivoSaida, 'a') as mst:
				mst.write('\n\nMST: \n')
				mst.write('Aresta/Peso \n')
				pesoTotal = 0
				for i in range(1, self.v):
					pesoTotal = pesoTotal + self.matrizAdj[i][pai[i]]
					mst.write(str(pai[i] + 1))
					mst.write(' ')
					mst.write(str(i + 1))
					mst.write(' ')
					mst.write(str(self.matrizAdj[i][pai[i]]))
					mst.write('\n')
				mst.write('Peso total: ')
				mst.write(str(pesoTotal))
				mst.write('\n')
			mst.close()

	def printDadosGrafo (self, arquivoSaida):
		with open(arquivoSaida, 'a') as saida:
			saida.write('\nnum de vertices: '+ str(self.v))
			saida.write('\nnum de arestas: '+  str(self.arestas))
			saida.write('\nGrau medio: '+  str(self.calcular_grau_medio())+'\n\n')
			saida.write("Distribuicao Empirica:\n")
			distribuicao_empirica = self.calcular_distribuicao_empirica(arquivoSaida)
			saida.write(distribuicao_empirica)
		saida.close()
	
	# Função que encontra o vértice não visitado de menor peso no grafo
	# O sys.maxsize é equivalente ao infinito
	def chaveMin(self, chave, mst):
		min = sys.maxsize
		for v in range(self.v):
			# Se a chave for menor que o valor mínimo e ainda não estiver na MST, atualize a chave
			if chave[v] < min and mst[v] == False:
				min = chave[v]
				indexMin = v			
		return indexMin
		
	# Função que constrói a MST
	def prim(self, arquivoSaida):
		# Array de vértices com pesos mínimos
		chave = [sys.maxsize] * self.v
		
		# Array dos pais preenchido com zeros
		pai = [None] * self.v 
		
		# O vértice 0 é escolhido como o primeiro
		chave[0] = 0
		mst = [False] * self.v
		
		# O primeiro vértice não tem pai
		pai[0] = -1

		for i in range(self.v): 
			u = self.chaveMin(chave, mst)
			
			# Insere menor vértice na lista do novo grafo
			mst[u] = True
			
			# Se o vértice for vizinho da chave, não está incluso na MST e o peso é o menor dentre todos os vizinhos
			# Atualiza o valor da chave e do pai
			for v in range(self.v): 
				if self.matrizAdj[u][v] > 0 and mst[v] == False and chave[v] > self.matrizAdj[u][v]:
					chave[v] = self.matrizAdj[u][v]
					pai[v] = u
		self.printMST(arquivoSaida, pai)

	# Função que faz o BFS
	def BFS(self, começo, arquivoSaida):
		visitado = [False] * self.v
		fila = [começo - 1]
 
		# Começo já está visitado
		visitado[começo - 1] = True 
		while fila:
			vis = fila[0]
			with open(arquivoSaida, 'a') as BFS:
				BFS.write(str(vis + 1))
				BFS.write(' ')
			BFS.close()
			fila.pop(0)
			 
			# Para todo vértice adjacente do vértice atual
			for i in range(self.v):
				if (self.matrizAdj[vis][i] > 1 and (not visitado[i])):
					# Coloque-o na fila
					fila.append(i)
					visitado[i] = True

	def DFS(self, inicio, arquivoSaida):
		visitado = [False] * self.v
		pilha = [inicio - 1]
		
		while pilha:
			vertice = pilha.pop()
			
			if not visitado[vertice]:
				with open(arquivoSaida, 'a') as DFS:
					DFS.write(str(vertice + 1))
					DFS.write(' ')
				DFS.close()
				visitado[vertice] = True
				
				for vizinho in range(self.v - 1, -1, -1):
					if self.matrizAdj[vertice][vizinho] > 1 and not visitado[vizinho]:
						pilha.append(vizinho)

	def calcular_grau_medio(self):
		grau_medio = self.arestas/self.v
		return grau_medio
	
	def calcular_distribuicao_empirica(self, arquivoSaida):
		distDistribuicao = {}
		total_vertices = self.v
		distribuicao_empirica = "" 
		for v in range(self.v):
				grau = sum(1 for peso in self.matrizAdj[v] if peso > 0)
				if grau in distDistribuicao:
					distDistribuicao[grau] += 1
				else:
					distDistribuicao[grau] = 1
		distribuicao_ordenada = sorted(distDistribuicao.items(), key=lambda x: x[0])  # Ordena a distribuição
		with open(arquivoSaida, 'a') as saida:
				for grau, frequencia in distribuicao_ordenada:
					distr = frequencia / total_vertices
					distribuicao_empirica += "Grau {} ---> Distribuicao Empirica = {}\n".format(str(grau), str(distr))
				return distribuicao_empirica
	
	def distanciaMedia(self):
		#ESTÁ INCORRETO, A DISTANCIA MÉDIA DEPENDE DO ALGORITMO DE DIJKSTRA (EU ACHO)
		pesoTotal = 0
		for i in range(self.v):
				for j in range(self.v):
					pesoTotal = pesoTotal + self.matrizAdj[i][j]
		pesoTotal = pesoTotal / 2
		distanciaMedia = pesoTotal / (math.comb(self.arestas, 2))
		return distanciaMedia

