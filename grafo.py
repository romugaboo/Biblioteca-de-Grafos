# Algoritmo de Prim para árvore geradora mínima (MST) por meio da matriz de adjacência
import sys

class Grafo():
	# Construtor: Monta matriz de adjacência preenchida com zeros
	def __init__(self, vertices):
		self.V = vertices
		self.grafo = [[0 for coluna in range(self.V)]
					for linha in range(vertices)]
		
	# Função que faz a leitura de um grafo em txt e o insere em uma matriz de adjacência
	def lerGrafo(self, arquivo):
		with open(arquivo, 'r') as f:
			linhas = f.readlines()
		
		# Lê o número de vértices
		vertices = int(linhas[0].strip())
		
		# Cria matriz de adjacência para o grafo no txt
		matriz_adjacencia = [[0] * vertices for _ in range(vertices)]
		for linha in linhas[1:]:
			valores = linha.strip().split()
			origem, destino, peso = int(valores[0]), int(valores[1]), int(valores[2])
			matriz_adjacencia[origem - 1][destino - 1] = peso
			matriz_adjacencia[destino - 1][origem - 1] = peso
		
		# Cria um grafo com as informações de grafo.txt e executa o algoritmo de Prim
		g = Grafo(vertices)
		g.grafo = matriz_adjacencia
		
		return g

	# Função que imprime a árvore geradora mínima
	def printMST(self, pai):
		print("\nA árvore geradora mínima pelo algoritmo de Prim desse grafo é: \n")
		print("Aresta \t\tPeso")
		for i in range(1, self.V):
			print(pai[i] + 1, "-", i + 1, "\t\t", self.grafo[i][pai[i]])

	# Função que encontra o vértice não visitado de menor peso no grafo
	# O sys.maxsize é equivalente ao infinito
	def chaveMin(self, chave, mst):
		min = sys.maxsize
		for v in range(self.V):
			# Se a chave for menor que o valor mínimo e ainda não estiver na MST, atualize a chave
			if chave[v] < min and mst[v] == False:
				min = chave[v]
				indexMin = v			
		return indexMin
		
	# Função que constrói a MST
	def prim(self):
		# Array de vértices com pesos mínimos
		chave = [sys.maxsize] * self.V
		
		# Array dos pais preenchido com zeros
		pai = [None] * self.V 
		
		# O vértice 0 é escolhido como o primeiro
		chave[0] = 0
		mst = [False] * self.V
		
		# O primeiro vértice não tem pai
		pai[0] = -1

		for i in range(self.V): 
			u = self.chaveMin(chave, mst)
			
			# Insere menor vértice na lista do novo grafo
			mst[u] = True
			
			# Se o vértice for vizinho da chave, não está incluso na MST e o peso é o menor dentre todos os vizinhos
			# Atualiza o valor da chave e do pai
			for v in range(self.V): 
				if self.grafo[u][v] > 0 and mst[v] == False and chave[v] > self.grafo[u][v]:
					chave[v] = self.grafo[u][v]
					pai[v] = u
		self.printMST(pai)

	# Função que faz o BFS
	def BFS(self, começo):
		visitado = [False] * self.V
		fila = [começo - 1]
 
		# Começo já está visitado
		visitado[começo - 1] = True

		print("\nA árvore de busca pelo BFS é:")
 
		while fila:
			vis = fila[0]
 
			# Imprime nó atual
			print(vis + 1, end = ' ')
			fila.pop(0)
			 
			# Para todo vértice adjascente do vértice atual
			for i in range(self.V):
				if (self.grafo[vis][i] > 1 and (not visitado[i])):
					# Coloque-o na fila
					fila.append(i)
					visitado[i] = True
		
	def DFSRecursivo(self, começo, visitado):
		# Print current node
		print(começo + 1, end = ' ')
 
		# Set current node as visited
		visitado[começo] = True
 
		# For every node of the graph
		for i in range(self.V):			 
			# If some node is adjacent to the current node and it has not already been visited
			if (self.grafo[começo][i] > 1 and (not visitado[i])):
				self.DFSRecursivo(i, visitado)

	def DFS(self, começo):
			print("\n\nA árvore de busca pelo DFS é:")
			visitado = [False] * g.V
			self.DFSRecursivo(começo - 1, visitado)

if __name__ == '__main__':
	g = Grafo(0)
	g = g.lerGrafo('grafoSimples.txt')
	g.prim()
	g.BFS(1)
	visitado = [False] * g.V
	g.DFS(1)
	print("\n")