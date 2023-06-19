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
		g = g.lerGrafo(arquivo)
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
				g.BFS(int(comeco), arquivoSaida)	
				print("\nBFS realizado com sucesso!")	
    	    #3 - DFS (escolha o vértice inicial)
			case "3":
				comeco = input("\nDigite o vértice de ínicio: ")	
				g.DFS(int(comeco), arquivoSaida)	
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
				distancia_minima = g.dijkstra()
				with open(arquivoSaida, 'a') as saida:
					saida.write("\nDistancia minima:\n\n ")
					saida.write(str((distancia_minima)))
				saida.close	
				print("\nCaminho mínimo, distância média e distâncias mínimas realizados com sucesso!")	
			#7 - Todas as operações acima (as operações personalizadas começarão do vértice 1)
			case "7":
				g.printDadosGrafo(arquivoSaida)	
				g.BFS(1, arquivoSaida)	
				g.DFS(1, arquivoSaida)	
				g.componentesConexos(arquivoSaida)	
				g.prim(arquivoSaida)	
				distancia_minima = g.dijkstra()
				with open(arquivoSaida, 'a') as saida:
					saida.write("\nDistancia minima:\n\n ")
					saida.write(str((distancia_minima)))
				saida.close	
				print("\nOperações realizadas com sucesso!")
			
			case "8":
				arquivoSaida, g = definirArquivo()

    	    #0 - Sair
			case _:
				sys.exit("Programa finalizado.\n")