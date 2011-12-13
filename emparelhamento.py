# -*- coding: utf-8 -*-
import networkx
import pydot


class Hungaro:
	def texto(self):
		return "Algoritmo Hungaro"
	
	def lerGrafoDoArquivoMatrizAdjacente(self, caminho):
		print "Lendo matriz adjacente: "+caminho
		arquivo = open(caminho, 'r')
		self.grafo = pydot.Dot('Grafo', graph_type='graph' )
		#obter numero de no em primeira linha
		lista = arquivo.readline().split('\t')
		no_count = 0
		for coluna in range(0,len(lista)):
			self.grafo.add_node(pydot.Node(str(coluna)))
			if lista[coluna]=="1":
				self.grafo.add_edge(pydot.Edge(str(coluna), "1"))
				print ' add edge:'+str(coluna)+" - 1"
				no_count+=1
		print "numero no: "+str(no_count)
		#loop de toda linha, 2 ate no_count inclusive
		for i in range(2, no_count+1):
			linha = arquivo.readline()
			if linha != "":
				lista = linha.split('\t')
				j = 1
				for cell in lista:
					if cell == '1' and j>i:
						self.grafo.add_edge( pydot.Edge(str(j+i), str(i)) )
						print 'add Edge: ' + str(j+i) + ' - ' + str(i)
					j+=1
			else:
				print "Erro de leitura na Matriz de adjacencia"
				break
		return
	
	def lerGrafoDoArquivoDot(self, caminho):
		#self.grafo = networkx.read_dot(caminho) # network não lê subgrafos
		self.grafo = pydot.graph_from_dot_file(caminho)
		return
	
	def geraImagemGrafoInicial(self):
		self.grafo.write_gif("grafo.gif")
		self.exportarParaMatrizAdj(self grafo, "matrizAdjDoOriginal")
		return
	
	def aplicaHungaro(self): # grafo, X, emparelhamento
		
		self.grafoEmp = self.grafo
		
		# busca subgrafos
		lista = self.grafoEmp.get_subgraph_list()
		for i in lista:
			if i.get_name() == "X":
				sgX = i
			elif i.get_name() == "Y":
				sgY = i
			elif i.get_name() == "M":
				sgM = i
		
		# segue os passo do algoritmo
		passo = 1
		
		while passo != 0:
			#
			# PASSO O1
			#
			if passo == 1:
				print "\tPasso 1"
				
				if sgM.get_edges().__len__() == 0 :
					print "O conjunto M está vazio"
					e = self.grafoEmp.get_edges()[0]
					sgM.add_edge( e )
					print "O vértice " + self.imprimeVertice(e) + " foi adicionado a M"
					
				
				passo = 2
				
			#
			# PASSO O2
			#
			elif passo == 2:
				print "\tPasso 2"
				
				# existe algum vértice não saturado?
				
				i = 0
				encontrouNaoSaturado = False
				sgMx = networkx.from_pydot(sgM)
				
				while not encontrouNaoSaturado and i < sgX.get_nodes().__len__():
					v = sgX.get_nodes()[i]
					if not sgMx.has_node( v.get_name() ):
						print "Vértice não-saturado encontrado em X: "+ v.get_name()
						encontrouNaoSaturado = True
				
				if not encontrouNaoSaturado:
					print "Todos os vértices de X já estão saturados"
					passo = 0
				else:
					arvore = networkx.Graph()
					arvore.add_node( v.get_name() )
					passo = 3
				
			#
			# PASSO O3
			#
			elif passo == 3:
				print "\tPasso 3"
				
				# verifica se a vizinhança tem o mesmo tamanho de T
				
				T = arvore.nodes()
				sgXx = networkx.from_pydot(sgX)
				for n in T:
					if sgXx.has_node( n ):
						T.remove(n)
				
				T.sort()
				print "T = " + T.__str__()
				
				S = arvore.nodes()
				sgXx = networkx.from_pydot(sgX)
				for n in T:
					if not sgXx.has_node( n ):
						S.remove(n)
				
				S.sort()
				print "S = " + S.__str__()
				
				NS = []
				grafoEmpx = networkx.from_pydot(self.grafoEmp)
				for n in S:
					lvizin = grafoEmpx.neighbors( n )
					for vizin in lvizin:
						if not NS.__contains__( vizin ):
							NS.append( vizin )
							
				NS.sort()
				print "NS = " + NS.__str__()
				
				if NS == T:
					print "PROBLEMA: O algoritmo não satisfaz o Teorema do Casamento"
					passo = 0
				else:
					
					# busca um y em NS que não está em T
					candidatos = NS
					for n in candidatos:
						if T.__contains__ ( n ):
							NS.remove(n)
					
					y = NS[0];
					print "Escolheu "+ y +" entre NS - T: "+ candidatos.__str__()
					
					passo = 4
				
				
			#
			# PASSO O4
			#
			elif passo == 4:
				print "\tPasso 4"
				
				
				passo = 0
				
		
		
		### Passo 2 busca vertice de X nao saturado por arestas de M
		#partxM = networkx.from_pydot(partM)
		#partxY = networkx.from_pydot(partY)
		#grafox = networkx.from_pydot(self.grafo)
		
		#i = 0
		#fereTC = False
		#achouMSaturado = False
				
				
					
					#NS = grafox.neighbors( v.get_name() )
					#NS.sort()
					#if NS == T:
						#print "Este grafo não é emprelhável segundo o Teorema do Casamento"
						#fereTC = True
					#else:
						## escolhe em NS elementos que não estão em T
						#for i in NS:
							#if T.__contains__( i.get_name() ):
								#NS.remove( i.get_name() )
						
						#y = NS[0]
						
						### Passo 4
						### se y eh saturado, S+= vertice de ligada a y, e T+=y , GOTO Passo 3
						### senao transferencia de no ate y , GOTO Passo 2
						
						## se y é m-saturado add yz a arvore
						#if partxM.has_node( y.get_name() ):
							## um vizinho de y na arvore
							#yvizin = grafox.neighbors( y.get_name() )
							#j = 0
							##while partxM.neighbors( yvizin )
							
							## o único vizinho de y em M
							#z = partxM.neighbors( y.get_name() )[0]
							##S.append(z)
							##T.append(y)
						#else:
							## fazer manipulação do caminho M-aumentado
							
							
							#achouMSaturado = True
			#i+= 1
		
		
		return
		
	def imprimeVertice(self, e):
		return "("+e.get_source()+", "+e.get_destination()+")"
		
	def geraImagemGrafoEmparelhado(self):
		
		self.grafoEmp.write_gif('grafoEmparelhado.gif')
		
		return
		
	#recebe listas de no e aresta
	def lerGrafoBipartidoDaLista(self, particaoX, particaoY, arestas):
		self.grafo = pydot.Dot(graph_type='graph')
		subX = pydot.subgraph('X')
		subY = pydot.subgraph('Y')
		for no in particaoX:
			subX.add_node(str(no))
		for no in particaoY:
			subY.add_node(str(no))
		self.grafo.add_subgraph(subX)
		self.grafo.add_subgraph(subY)
		for aresta in arestas:
			self.grafo.add_edge(str(aresta))
		return self.grafo
		
	
	def exportarParaMatrizAdj(self, grafoDot, nome):
		print('criando arquivo com matriz de adjacencia: '+nome+'.txt')
		arquivo = open(str(nome)+'.txt', 'w')
		grafox = networkx.from_pydot(grafoDot)
		listaNo = grafox.nodes()
		for i in range(0, len(listaNo)):
			vizinhos = grafox.neighbors(listaNo[i])
			linha = ""
			for j in range(0, len(listaNo)):
				if listaNo[j] in vizinhos:
					linha+="1\t"
					print listaNo[i]+"("+str(i)+") -- " + listaNo[j]+"("+str(j)+")"
				else:
					linha+="0\t"
			linha = linha[0:-1]+"\n"
			arquivo.write(linha)






