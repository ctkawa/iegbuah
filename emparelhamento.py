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
		self.exportarParaMatrizAdj(self.grafo, "matrizAdjDoOriginal")
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
		
		arvore = networkx.Graph()
		sgMx = networkx.from_pydot(sgM)
		sgXx = networkx.from_pydot(sgX)
		
		S = []
		T = []
		
		# segue os passo do algoritmo
		passo = 1
		
		while passo != 0:
			#
			# PASSO O1
			#
			if passo == 1:
				print "\tPasso 1"
				
				if sgMx.edges().__len__() == 0 :
					print "O conjunto M está vazio"
					e = self.grafoEmp.get_edges()[0]
					sgMx.add_edge( e.get_source(), e.get_destination() )
					print "A aresta " + self.imprimeVertice(e) + " foi adicionada a M"
					
				
				self.imprimeEstado(sgX, sgY, sgMx, arvore )
				raw_input("1")
				
				passo = 2
				
			#
			# PASSO O2
			#
			elif passo == 2:
				print "\tPasso 2"
				
				# existe algum vértice não saturado?
				
				i = 0
				encontrouNaoSaturado = False
				S = []
				T = []
				while not encontrouNaoSaturado and i < sgX.get_nodes().__len__():
					print "loop"
					v = sgX.get_nodes()[i]
					if not sgMx.has_node( v.get_name() ):
						print "Vértice não-saturado encontrado em X: "+ v.get_name()
						encontrouNaoSaturado = True
						S.append(v.get_name())
					i +=1
				
				if not encontrouNaoSaturado:
					print "Todos os vértices de X já estão saturados"
					passo = 0
				else:
					arvore = networkx.Graph()
					arvore.add_node( v.get_name() )
					passo = 3
					
				self.imprimeEstado(sgX, sgY, sgMx, arvore )
				raw_input("2")
				
			#
			# PASSO O3
			#
			elif passo == 3:
				print "\tPasso 3"
				
				# verifica se a vizinhança tem o mesmo tamanho de T
				
				T = arvore.nodes()
				
				sgXx = networkx.from_pydot(sgX)
				#print "arvore noses: "
				#print arvore.nodes()
				#print "T:"
				#print T.__len__()
				#print T
				i = T.__len__() - 1;
				while i >= 0:
					#print "i"
					print "T[i] Vale: "
					print T[i]
					#print "avaliando " + T[i]
					if sgXx.has_node( T[i] ):
						#print "removeu" + T[i]
						T.remove(T[i])
					i -= 1
				
				T.sort()
				print "T = " + T.__str__()
				
				#S = arvore.nodes()
				#for n in T:
					#if not sgXx.has_node( n ):
						#S.remove(n)
				
				S.sort()
				print "S = " + S.__str__()
				
				NS = []
				grafoEmpx = networkx.from_pydot(self.grafoEmp)
				grafoEmpx = grafoEmpx.to_undirected()
				
				for n in S:
					lista = grafoEmpx.neighbors(n)
					for n2 in lista:
						if n2 not in NS:
							NS.append(n2)
							
				NS.sort()
				print "NS = " + NS.__str__()
				
				if NS == T:
					print "PROBLEMA: O algoritmo não satisfaz o Teorema do Casamento"
					passo = 0
				else:
					
					# busca um y em NS que não está em T
					candidatos = []
					for n in NS:
						if n not in T:
							candidatos.append(n)
					
					y = candidatos[0];
					print "Escolheu "+ y +" entre NS - T: "+ candidatos.__str__()
					
					passo = 4
				
				self.imprimeEstado(sgX, sgY, sgMx, arvore )
				raw_input("3")
				
			#
			# PASSO O4
			#
			elif passo == 4:
				print "\tPasso 4"
				
				# verifica se y é M-saturado
				
				if sgMx.has_node( y ):
					print y + " é M-saturado"
					
					# adiciona novas arestas a arvore
					
					# busca um no na arvore que seja vizinho a y
					lista = arvore.nodes()
					i = 0
					encontrou = False
					while not encontrou and i < lista.__len__():
						if grafoEmpx.has_edge(y, lista[i]):
							arvore.add_edge( y, lista[i] )
						i +=1
					
					
					
					vizin = sgMx.neighbors( y )
					for n in sgMx.predecessors( y ):
						if not vizin.__contains__(n):
							vizin.append(n)
					z = vizin[0]
						
					arvore.add_edge( y, z )
					
					T.append(y)
					S.append(z)
					
					passo = 3
					
				else:
					print y + " é M-não-saturado"
					
					atual = y
					vizin = grafoEmpx.neighbors( atual )
					
					encontrado = False
					i = 0
					while not encontrado and i < vizin.__len__():
						if vizin[i] in arvore.nodes():
							encontrado = True
							prox = vizin[i]
						
					
					
					if sgMx.has_edge( y, prox ):
						sgMx.remove_edge( y, prox)
					else:
						sgMx.add_edge( y, prox)
					
					anterior = y
					atual = prox
					
					while atual != v.get_name():
						vizin = arvore.neighbors( atual )
						
						if vizin[0] != anterior:
							prox = vizin[0]
						else:
							prox = vizin[1]
						
						if sgMx.has_edge( atual, prox ):
							sgMx.remove_edge( atual, prox)
						else:
							sgMx.add_edge( atual, prox)
						
						anterior = atual
						atual = prox
					
					passo = 2
					
				print "Emparelhamento:"
				print sgMx.nodes()
				print sgMx.edges()
				
				print "Arvore:"
				print arvore.nodes()
				print arvore.edges()
				
				self.imprimeEstado(sgX, sgY, sgMx, arvore )
				raw_input("4")
				
		
		# adiciona arestas de sgXx em XgX
		lista = sgMx.edges()
		for e in lista:
			sgM.add_edge( pydot.Edge(e[0], e[1]) )
		
		print sgMx.edges()
		print sgM.get_edge_list()
		
		return
		
	def imprimeVertice(self, e):
		return "("+e.get_source()+", "+e.get_destination()+")"
	
	def imprimeEstado(self, sgX, sgY, sgMx, arvore ):
		sgXx = networkx.from_pydot(sgX)
		print "X: "
		print sgXx.nodes()
		
		sgYx = networkx.from_pydot(sgY)
		print "Y: "
		print sgYx.nodes()
		
		print "M: "
		print sgMx.nodes()
		print sgMx.edges()
		
		print "Arvore: "
		print arvore.nodes()
		print arvore.edges()
		
		return
	
	def geraImagemGrafoEmparelhado(self):
		
		print "cabou"
		
		lista = self.grafoEmp.get_subgraph_list()
		for s in lista:
			print s.get_name()
			for v in s.get_node_list():
				print "vertice: " + v.get_name()
			for a in s.get_edge_list():
				print "aresta: (" + a.get_source() + ", " + a.get_destination() + ") "
		
		print "cabou 2"
		
		lista = self.grafoEmp.get_subgraph_list()
		for s in lista:
			print s.get_name()
			for v in s.get_node_list():
				print "vertice: " + v.get_name()
				for a in s.get_edge_list():
					print "aresta: (" + a.get_source() + ", " + a.get_destination() + ") "
		
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






