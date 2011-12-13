# -*- coding: utf-8 -*-
import networkx
import pydot


class Hungaro:
	def texto(self):
		return "Algoritmo Hungaro"
	
	def lerGrafoDoArquivoMatrizAdjacente(self, caminho):
		#print "Lendo: "+caminho
		#arquivo = open(caminho, 'r')
		#self.grafo = pydot.Dot('Grafo', graph_type='graph' )
		##obter numero de no em primeira linha
		#lista = arquivo.readline().split('\t')
		#no_count = 0
		#for coluna in range(0,len(lista)):
			#self.grafo.add_node(pydot.Node(str(coluna)))
			#if lista[coluna]=="1":
				#self.grafo.add_edge(pydot.Edge(str(coluna), "1"))
				#print ' add edge:'+str(coluna)+" - 1"
				#no_count+=1
		#print "numero no: "+str(no_count)
		##loop de toda linha, 2 ate no_count inclusive
		#for i in range(2, no_count+1):
			#linha = arquivo.readline()
			#if linha != "":
				#lista = linha.split('\t')
				#j = 1
				#for cell in lista:
					#if cell == '1' and j>i:
						#self.grafo.add_edge( pydot.Edge(str(j+i), str(i)) )
						#print 'add Edge: ' + str(j+i) + ' - ' + str(i)
					#j+=1
			#else:
				#print "Erro de leitura na Matriz de adjacencia"
				#break
		
		#self.grafo = networkx.Graph()
		#self.grafo = networkx.read_dot(caminho)
		return
	
	def lerGrafoDoArquivoDot(self, caminho):
		#self.grafo = networkx.read_dot(caminho) # network não lê subgrafos
		self.grafo = pydot.graph_from_dot_file(caminho)
		return
	
	def geraImagemGrafoInicial(self):
		self.grafo.write_gif("grafo.gif")
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
		
		
		
		#while i < partX.get_nodes().__len__() and not fereTC:
			#v = partX.get_nodes()[i]		# para cada vértice de X
			#if not partxM.has_node( v.get_name() ):   # se é não-saturado
				#arvore = networkx.Graph()
				#arvore.add_node( v.get_name() )
				##T = []
				
				
				### Passo 3 N (S ) == T -> STOP
				###y de N (S ) que nao esteja em T
				#while not fereTC and not achouMSaturado:
					#T = []
					#for n in arvore.nodes():
						#if partxY.has_node( n ):
							#T.append( n )
					#T.sort()
					
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
	