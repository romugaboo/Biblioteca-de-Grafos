# Algoritmo de Prim para árvore geradora mínima (MST) por meio da matriz de adjacência
import sys
from collections import deque
import grafoUtils

class Grafo():
	# Construtor: Monta matriz de adjacência preenchida com zeros
	def __init__(self, vertices):
		self.v = vertices
		self.matrizAdj = [[0 for coluna in range(self.v)]
					for linha in range(vertices)]
		self.arestas=0
	
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
	def prim(self):
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
		grafoUtils.printMST(g, arquivoSaida, pai)

	# Função que faz o BFS
	def BFS(self, começo):
		visitado = [False] * self.v
		fila = [começo - 1]
 
		# Começo já está visitado
		visitado[começo - 1] = True 
		while fila:
			vis = fila[0]

			grafoUtils.printBFS(g, arquivoSaida, vis)
			fila.pop(0)
			 
			# Para todo vértice adjacente do vértice atual
			for i in range(self.v):
				if (self.matrizAdj[vis][i] > 1 and (not visitado[i])):
					# Coloque-o na fila
					fila.append(i)
					visitado[i] = True

	def DFS(self, inicio):
		visitado = [False] * self.v
		pilha = [inicio - 1]
		
		while pilha:
			vertice = pilha.pop()
			
			if not visitado[vertice]:
				grafoUtils.printDFS(g, arquivoSaida, vertice)
				visitado[vertice] = True
				
				for vizinho in range(self.v - 1, -1, -1):
					if self.matrizAdj[vertice][vizinho] > 1 and not visitado[vizinho]:
						pilha.append(vizinho)

	def calcular_grau_medio(self):
		grau_medio = self.arestas/self.v
		return grau_medio
	
	def calcular_distribuicao_empirica(self):
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

if __name__ == '__main__':
	print ("\nOlá, professor Glauco! Bem-vindo à nossa biblioteca de grafos.")
	print("Todas as respostas estarão armazenada em um txt chamado: nome do arquivo + respostas \n")
	
	arquivo = input("Insira o nome do arquivo que contém o grafo a ser lido: ")
	arquivoSaida = arquivo
	arquivoSaida = arquivoSaida.replace('.txt', '_respostas.txt')
	g = Grafo(0)
	g = grafoUtils.lerGrafo(g, arquivo)

	while True:
		print ("\nMenu:")
		print ("1 - Dados do Grafo e Distribuição Empírica")
		print ("2 - BFS")
		print ("3 - DFS")
		print ("4 - Componentes Conexas")
		print ("5 - Distância e Caminho Mínimo em um Par de Vértices")
		print ("6 - MST por Prim")
		print ("7 - Distância Média")
		print ("8 - Todas as operações acima")
		print ("0 - Sair")

		option = input("\nDigite a operação que você deseja realizar: ")
		
		match option:	
			case "1":
				grafoUtils.printDadosGrafo(g, arquivoSaida)
				print("\nOperação realizada com sucesso!")

			case "2":
				with open(arquivoSaida, 'a') as BFS:
					BFS.write("\nBFS:\n")
				BFS.close()
				g.BFS(1)
				print("\nOperação realizada com sucesso!")

			case "3":
				with open(arquivoSaida, 'a') as DFS:
					DFS.write("\n\nDFS:\n")
				DFS.close()
				g.DFS(1)
				print("\nOperação realizada com sucesso!")

			case "6":
				g.prim()
				print("\nOperação realizada com sucesso!")

			case "8":
				grafoUtils.printDadosGrafo(g, arquivoSaida)

				with open(arquivoSaida, 'a') as BFS:
					BFS.write("\nBFS:\n")
				BFS.close()
				g.BFS(1)

				with open(arquivoSaida, 'a') as DFS:
					DFS.write("\n\nDFS:\n")
				DFS.close()
				g.DFS(1)

				g.prim()
				print("\nOperação realizada com sucesso!")

			case _:
				sys.exit("Programa finalizado.")