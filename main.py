import sys
from grafoBib import Grafo

if __name__ == '__main__':
	print ("\nOlá, professor Glauco! Bem-vindo à nossa biblioteca de grafos.")
	print("Todas as respostas estarão armazenada em um txt chamado: nome do arquivo + respostas \n")
	
	arquivo = input("Insira o nome do arquivo que contém o grafo a ser lido: ")
	arquivoSaida = arquivo
	arquivoSaida = arquivoSaida.replace('.txt', '_respostas.txt')
	g = Grafo(0)
	g = g.lerGrafo(arquivo)

	while True:
		print ("\nMenu:")
		print ("1 - Dados do Grafo e Distribuição Empírica")
		print ("2 - BFS (escolha o vértice inicial)")
		print ("3 - DFS (escolha o vértice inicial)")
		print ("4 - Componentes Conexas")
		print ("5 - Distância e Caminho Mínimo em um Par de Vértices")
		print ("6 - MST por Prim")
		print ("7 - Distância Média")
		print ("8 - Todas as operações acima (as operações personalizadas começarão do vértice 1)")
		print ("0 - Sair")

		option = input("\nDigite a operação que você deseja realizar: ")
		
		match option:
			#1 - Dados do Grafo e Distribuição Empírica
			case "1":
				g.printDadosGrafo(arquivoSaida)
				print("\nOperação realizada com sucesso!")

            #2 - BFS (escolha o vértice inicial)
			case "2":
				comeco = input("\nDigite o vértice de ínicio: ")
				with open(arquivoSaida, 'a') as BFS:
					BFS.write("\nBFS:\n")
				BFS.close()
				g.BFS(int(comeco), arquivoSaida)
				print("\nOperação realizada com sucesso!")

            #3 - DFS (escolha o vértice inicial)
			case "3":
				comeco = input("\nDigite o vértice de ínicio: ")
				with open(arquivoSaida, 'a') as DFS:
					DFS.write("\n\nDFS:\n")
				DFS.close()
				g.DFS(int(comeco), arquivoSaida)
				print("\nOperação realizada com sucesso!")

            #6 - MST por Prim
			case "6":
				g.prim(arquivoSaida)
				print("\nOperação realizada com sucesso!")

            #7 - Distância Média
			case "7":
				with open(arquivoSaida, 'a') as saida:
					saida.write("\nDistancia media: ")
					saida.write(str(g.distanciaMedia()))
				saida.close

            #8 - Todas as operações acima (as operações personalizadas começarão do vértice 1)
			case "8":
				g.printDadosGrafo(arquivoSaida)

				with open(arquivoSaida, 'a') as BFS:
					BFS.write("\nBFS:\n")
				BFS.close()
				g.BFS(1, arquivoSaida)

				with open(arquivoSaida, 'a') as DFS:
					DFS.write("\n\nDFS:\n")
				DFS.close()
				g.DFS(1, arquivoSaida)

				g.prim(arquivoSaida)
				print("\nOperação realizada com sucesso!")

				with open(arquivoSaida, 'a') as saida:
					saida.write("\nDistancia media: ")
					saida.write(str(g.distanciaMedia()))
				saida.close

            #0 - Sair
			case _:
				sys.exit("Programa finalizado.\n")