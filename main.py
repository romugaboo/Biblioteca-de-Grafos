import sys
from grafoBib import Grafo

if __name__ == '__main__':
	print ("\nOlá, professor Glauco! Bem-vindo à nossa biblioteca de grafos.")
	print("Todas as respostas estarão armazenada em um txt chamado: nome do arquivo + respostas \n")
	
	def definirArquivo():
		arquivo = input("Insira o nome do arquivo que contém o grafo a ser lido: ")
		arquivoSaida = arquivo
		arquivoSaida = arquivoSaida.replace('.txt', '_respostas.txt')
		g = Grafo(0)
		try:
			g = g.lerGrafo(arquivo)
		except FileNotFoundError:
			print("\nO arquivo não existe ou não foi encontrado.\n")
			definirArquivo()
		print("\nArquivo lido com sucesso!\n")
		return arquivoSaida, g
	g = Grafo(0)
	arquivoSaida, g = definirArquivo()

	while True:
		print ("\nMenu:")
		print ("1 - Dados do Grafo e Distribuição Empírica")
		print ("2 - BFS (escolha o vértice inicial)")
		print ("3 - DFS (escolha o vértice inicial)")
		print ("4 - Componentes Conexas")
		print ("5 - MST por Prim")
		print ("6 - Caminho mínimo, distância média e distâncias mínimas")
		print ("7 - Todas as operações acima (as operações personalizadas começarão do vértice 1)")
		print ("8 - Mudar o arquivo de entrada")
		print ("0 - Sair")
		
		option = input("\nDigite a operação que você deseja realizar: ")
		
		match option:
			#1 - Dados do Grafo e Distribuição Empírica
			case "1":
				g.printDadosGrafo(arquivoSaida)

				print("\nDados do grafo e distribuição empírica realizados com sucesso!")

    	    #2 - BFS (escolha o vértice inicial)
			case "2":
				comeco = input("\nDigite o vértice de ínicio: ")	
				g.BFS(arquivoSaida, int(comeco))	
				print("\nBFS realizado com sucesso!")	

    	    #3 - DFS (escolha o vértice inicial)
			case "3":
				comeco = input("\nDigite o vértice de ínicio: ")	
				g.DFS(arquivoSaida, int(comeco))	
				print("\nDFS realizado com sucesso!")

			#4 - Componentes Conexas
			case "4":
				g.componentesConexos(arquivoSaida)	
				print("\nComponentes conexas realizados com sucesso!")	

    	    #5 - MST por Prim
			case "5":
				g.prim(arquivoSaida)	
				print("\nMST por Prim realizada com sucesso!")

			#6 - Caminho mínimo, distância média e  distâncias mínimas	
			case "6":
				g.dijkstra(arquivoSaida, False)
				print("\nCaminho mínimo, distância média e distâncias mínimas realizados com sucesso!")	

			#7 - Todas as operações acima (as operações personalizadas começarão do vértice 1)
			case "7":
				g.printDadosGrafo(arquivoSaida)	
				g.BFS(arquivoSaida, 1)	
				g.DFS(arquivoSaida, 1)	
				g.componentesConexos(arquivoSaida)	
				g.prim(arquivoSaida)	
				g.dijkstra(arquivoSaida, True)

				print("\nOperações realizadas com sucesso!")
			
			#8 - Mudar o arquivo de entrada
			case "8":
				arquivoSaida, g = definirArquivo()

    	    #0 - Sair
			case _:
				sys.exit("Programa finalizado.\n")