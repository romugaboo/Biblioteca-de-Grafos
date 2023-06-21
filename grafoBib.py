# Algoritmo de Prim para árvore geradora mínima (MST) por meio da matriz de adjacência
import sys
from collections import deque
import math
import heapq

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
				mst.write('\nMST: \n')
				mst.write('Aresta/Peso \n')
				pesoTotal = 0
				for i in range(1, self.v):
					pesoTotal = pesoTotal + self.matrizAdj[i][pai[i]]
					mst.write(str(pai[i] + 1) + ' ' + str(i + 1) + ' ' + str(self.matrizAdj[i][pai[i]]) + '\n')
				mst.write('Peso total: ' + str(pesoTotal) + '\n')
			mst.close()

	def printDadosGrafo (self, arquivoSaida):
		with open(arquivoSaida, 'a') as saida:
			saida.write('\nnum de vertices: '+ str(self.v))
			saida.write('\nnum de arestas: '+  str(self.arestas))
			saida.write(f'\nGrau medio : {self.calcular_grau_medio():.2f}\n\n')
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
	def BFS(self, arquivoSaida, comeco):
		visitado = [False] * self.v
		fila = [comeco - 1]
		with open(arquivoSaida, 'a') as BFS:
				BFS.write("\nBFS:\n")
		BFS.close()
 
		# Começo já está visitado
		visitado[comeco - 1] = True 
		while fila:
			vis = fila[0]
			with open(arquivoSaida, 'a') as BFS:
				BFS.write(str(vis + 1))
				BFS.write(' ')
			BFS.close()
			fila.pop(0)
			 
			# Para todo vértice adjacente do vértice atual
			for i in range(self.v):
				if (self.matrizAdj[vis][i] != 0 and (not visitado[i])):
					# Coloque-o na fila
					fila.append(i)
					visitado[i] = True

	def DFS(self, arquivoSaida, comeco):
		visitado = [False] * self.v
		pilha = [comeco - 1]

		with open(arquivoSaida, 'a') as DFS:
			DFS.write("\n\nDFS:\n")
		DFS.close()
		
		while pilha:
			vertice = pilha.pop()
			
			if not visitado[vertice]:
				with open(arquivoSaida, 'a') as DFS:
					DFS.write(str(vertice + 1))
					DFS.write(' ')
				DFS.close()
				visitado[vertice] = True
				
				for vizinho in range(self.v - 1, -1, -1):
					if self.matrizAdj[vertice][vizinho] != 0 and not visitado[vizinho]:
						pilha.append(vizinho)

	def calcular_grau_medio(self):
		graus = []
		# Calcular o grau de cada vértice
		for i in range(self.v):
			grau = sum(self.matrizAdj[i])
			graus.append(grau)
		# Calcular o grau médio
		grauMedio = sum(graus) / self.v
		return grauMedio
	
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

	def BFScomponentesConexos(self, inicio, visitados, componente):
		fila = [inicio]
		visitados[inicio] = True
		while fila:
			vertice = fila.pop(0)
			componente.append(vertice)
			for vizinho in range(self.v):
				if self.matrizAdj[vertice][vizinho] != 0 and not visitados[vizinho]:
					fila.append(vizinho)
					visitados[vizinho] = True

	def componentesConexos(self, arquivoSaida):
		with open(arquivoSaida, 'a') as saida:
			saida.write("\n\nComponentes Conexas: ")
		saida.close
		visitados = [False] * self.v
		todasComponentes = []
		for v in range(self.v):
			if not visitados[v]:
				componente = []
				self.BFScomponentesConexos(v, visitados, componente)
				todasComponentes.append(componente)
		componentes_ordenados = sorted(todasComponentes, key=len, reverse=True)

		# Converter cada componente em uma string
		componentes_string = " "
		for i, componente in enumerate(componentes_ordenados):
			num_vertice_componente = len(componente)
			componente_str = f"Componente {i+1}, com {num_vertice_componente} vertices: "+",".join(str(v+1) for v in componente)
		componentes_string += componente_str + "\n"
		with open(arquivoSaida, 'a') as saida:
			saida.write(componentes_string)
		saida.close
	
	def dijkstra(self, arquivoSaida, chamadaUnica):
		origem = 1
		destino = 0 
		valid_input = chamadaUnica #Caso True, o input de usuário não será requirido, e o algoritmo iniciará a partir do vértice 1 para todos os outros vértices do Grafo
		while not valid_input:
			origem = int(input("Caminho mínimo\n\nDigite o vértice de origem: "))
			destino = int(input("Insira um destino. Use 0 para calcular o menor caminho para todos os vértices: "))


			if origem == destino:
				ZeroDivisionError=("Origem e destino não podem ser iguais. Por favor, forneça valores diferentes.\n\n")
				print(f"Erro: {str(ZeroDivisionError)}")
			elif origem<=0:
				ZeroDivisionError=("Origem deve ser valor maior que zero.\n\n")
				print(f"Erro: {str(ZeroDivisionError)}")
			else:
				valid_input = True
		origem -= 1
		destino = destino-1
		distancias = [sys.maxsize] * self.v
		distancias[origem] = 0
		visitados = [False] * self.v
		interromper = False
		visitados_ordem = []
		distancia_media = 0.0
		heap = [(0, origem)] ##inicializamos o heap com uma tupla <distancia, vértice>, contendo a distância e o vértice de origem no início

		while heap: #enquanto houverem tuplas:
			u_dist, u = heapq.heappop(heap) # como a tupla é formada por <distancia, vértice>, u_dist e u recebem os valores de cada um respectivamente. este elemento tbm é retirado do heap.
			if visitados[u]: #se o vértice já tinha sido visitado, vai pular a iteração sobre ele
				continue
			visitados[u] = True #se não, vai marcá-lo como visitado
			visitados_ordem.append(u) #aqui é onde recebemos a ordem de acesso dos vértices

			if u == destino: 
				interromper = True
				break
			for v in range(self.v):
				if (self.matrizAdj[u][v] > 0 and
						not visitados[v] and
						u_dist + self.matrizAdj[u][v] < distancias[v]):
					distancias[v] = u_dist + self.matrizAdj[u][v]
					heapq.heappush(heap, (distancias[v], v))
					if interromper:
						break

		distancias_str = ""
		distancia_media=0.0
		vezesSoma = 0.0
		if destino==-1:
			for i, distancia  in enumerate(distancias):
					if i !=origem:
						distancias_str += f"Distancia ate o vertice {i+1}: {distancia}\n"
						distancia_media = sum(distancias)/(self.v-1)
			distancias_str+= f"Distancia media: {distancia_media:.2f}\n\n"
		else:
			vezesSoma =0.0
			vertices_str = ""

			for v in visitados_ordem[1:destino+1]:
				vertices_str += f"vertice: {v+1} de peso {distancias[v]}\n"

			distancias_str = f"Vertices visitados do caminho minimo:\n {vertices_str}\n"
			pesoAnterior = float(distancias[visitados_ordem[0]])
			for v in visitados_ordem[1:destino+3]:
				pesoAtual = float(distancias[v])
				if pesoAtual>pesoAnterior:
					distancia_media +=pesoAtual
					vezesSoma+=1
				pesoAnterior = pesoAtual
			distancia_media= distancia_media/vezesSoma
			distancias_str+= f"Distancia media: {distancia_media:.2f}\n\n"

		print ("Dados gravados no .txt com sucesso")
		with open(arquivoSaida, 'a') as saida:
			saida.write("\nDistancia minima:\n\n")
			saida.write(str((distancias_str)))
			saida.close
	