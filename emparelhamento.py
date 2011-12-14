# -*- coding: utf-8 -*-
import networkx
import pydot

#O pydot esta sendo utilizado para manipular o subgrafo representado em DOT
#O networkx esta sendo usado para manipulacao geral sobre o grafo



class Hungaro:

	def texto(self):
		return "Algoritmo Hungaro"
	
	def lerGrafoDoArquivoMatrizAdjacente(self, caminhoMatriz, caminhoLista):
		print "Lendo matriz adjacente: "+caminhoMatriz
		
		arquivoLista = open(caminhoLista, 'r')
		listaNome = []
		i=1
		while True:
			nome = arquivoLista.readline()
			if nome=='':
				break
			listaNome.append(nome.strip())
			i+=1
		print("listaNome.len: "+str(len(listaNome)))
		
		arquivoMatriz = open(caminhoMatriz, 'r')
		self.grafo = pydot.Dot('Grafo', graph_type='graph' )
		#obter numero de no em primeira linha
		lista = arquivoMatriz.readline().split('\t')
		no_count = 0
		aresta_count = 0
		for coluna in range(0,len(lista)):
			self.grafo.add_node(pydot.Node(listaNome[coluna]))
			no_count+=1
			if lista[coluna]=="1":
				self.grafo.add_edge(pydot.Edge(listaNome[coluna], listaNome[0]))
				#print ' add edge:'+listaNome[coluna]+" - "+listaNome[0]
				aresta_count+=1
		print "numero no: "+str(no_count)
		#loop de toda linha, 2 ate no_count inclusive
		for i in range(2, no_count+1):
			linha = arquivoMatriz.readline()
			if linha != "":
				lista = linha.split('\t')
				j = 1
				for cell in lista:
					if cell == '1' and j>i:
						self.grafo.add_edge( pydot.Edge(listaNome[j], listaNome[i]) )
						#print 'add Edge: ' + str(j+i) + ' - ' + str(i)
						aresta_count+=1
					j+=1
			else:
				print "Erro de leitura na Matriz de adjacencia"
				break
		print("numero aresta: "+str(aresta_count))
		
		
		subX = pydot.Subgraph('', rank='same')
		subX.set_name('X')
		subY = pydot.Subgraph('', rank='same')
		subY.set_name('Y')
		for nome in listaNome:
			if nome.isdigit():
				subY.add_node(pydot.Node(nome))
			else:
				subX.add_node(pydot.Node(nome))
		self.grafo.add_subgraph(subX)
		self.grafo.add_subgraph(subY)
		subM = pydot.Subgraph()
		subM.set_name('M')
		if len(self.grafo.get_edge_list())>0:
			subM.add_edge(self.grafo.get_edge_list()[0])
		self.grafo.add_subgraph(subM)
		
		print("Matriz lida")
		
		#print self.grafo.to_string()
		f = open('DOT_original.dot', 'w')
		f.write(self.grafo.to_string())
		f.close()

		return
	
	def lerGrafoDoArquivoDot(self, caminho):
		#self.grafo = networkx.read_dot(caminho) # network não lê subgrafos
		self.grafo = pydot.graph_from_dot_file(caminho)
		return
	
	def geraImagemGrafoInicial(self):
		self.grafo.write_gif("grafo.gif")
		self.grafo.write_svg("grafo.svg")
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
		pesos = {}
		sgMx = networkx.from_pydot(sgM)
		sgMx = sgMx.to_undirected()
		sgXx = networkx.from_pydot(sgX)
		sgXx = sgXx.to_undirected()
		grafoEmpx = networkx.from_pydot(self.grafoEmp)
		grafoEmpx = grafoEmpx.to_undirected()
		
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
					pesos[v.get_name()] = 0
					
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
				#maximo = T.__len__()
				#print maximo
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
				
				print "T:"
				print T
				
				#T.sort()
				#print "T = " + T.__str__()
				
				#S = arvore.nodes()
				#for n in T:
					#if not sgXx.has_node( n ):
						#S.remove(n)
				
				S.sort()
				print "S = " + S.__str__()
				
				NS = []
				
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
							pesos[y] = pesos[lista[i]] + 1
						i +=1
					
					#vizin = sgMx.neighbors( y )
					#for n in sgMx.predecessors( y ):
					#	if not vizin.__contains__(n):
					#		vizin.append(n)
					#z = vizin[0]
					z = sgMx.neighbors( y )[0]
						
					arvore.add_edge( y, z )
					pesos[z] = pesos[y] + 1
					
					T.append(y)
					S.append(z)
					
					passo = 3
					
				else:
					print y + " é M-não-saturado"
					
					atual = y
					print "Atual = "+atual
					vizin = grafoEmpx.neighbors( atual )
					print "Vizinhos de y"
					print vizin
					
					encontrado = False
					i = 0
					while not encontrado and i < vizin.__len__():
						if vizin[i] in arvore.nodes():
							encontrado = True
							prox = vizin[i]
						i += 1
						
					print "Proximo = " + prox
					
					
					if sgMx.has_edge( y, prox ):
						print "Removendo de M: ("+ y +", "+prox+")"
						sgMx.remove_edge( y, prox)
					else:
						print "Adicionando a M: ("+ y +", "+prox+")"
						sgMx.add_edge( y, prox)
					
					anterior = y
					atual = prox
					print "Atual = "+atual
					print "Prox = "+prox
					print "Anterior = "+anterior
					
					#networkx.to_pydot(arvore).write_gif("arvore.gif")
					
					while atual != v.get_name():
						vizin = arvore.neighbors( atual )
						print vizin
						for n in vizin:
							if pesos[n] < pesos[atual]:
								prox = n
						#if vizin[0] != anterior:
							#prox = vizin[0]
						#else:
							#prox = vizin[1]
						
						if sgMx.has_edge( atual, prox ):
							print "Removendo de M: ("+ atual +", "+prox+")"
							sgMx.remove_edge( atual, prox)
						else:
							print "Adicionando a M: ("+ atual +", "+prox+")"
							sgMx.add_edge( atual, prox)
						
						anterior = atual
						atual = prox
						print "Atual = "+atual
						print "Prox = "+prox
						print "Anterior = "+anterior
						#networkx.to_pydot(arvore).write_gif("arvore.gif")
					
					passo = 2
					
				print "Emparelhamento:"
				print sgMx.nodes()
				print sgMx.edges()
				
				print "Arvore:"
				print arvore.nodes()
				print arvore.edges()
				
				self.imprimeEstado(sgX, sgY, sgMx, arvore )
				raw_input("4")
				
		
		# formata arestas de sgXx em grafoEmp
		
		lista = self.grafoEmp.get_edges()
		for e in lista:
			if sgMx.has_edge( e.get_source(), e.get_destination() ):
				e.set_style("dotted")
		
		#sgM = novoM
		
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
		
		
		
		self.grafoEmp.write_gif('grafoEmparelhado.gif')
		
		return
		
	#recebe listas de no e aresta
	#def lerGrafoBipartidoDaLista(self, particaoX, particaoY, arestas):
		#self.grafo = pydot.Dot(graph_type='graph')
		#subX = pydot.subgraph('X')
		#subY = pydot.subgraph('Y')
		#for no in particaoX:
			#subX.add_node(str(no))
		#for no in particaoY:
			#subY.add_node(str(no))
		#self.grafo.add_subgraph(subX)
		#self.grafo.add_subgraph(subY)
		#for aresta in arestas:
			#self.grafo.add_edge(str(aresta))
		#return self.grafo
		
	
	def exportarParaMatrizAdj(self, nome):
		print('criando arquivo com matriz de adjacencia: '+nome+'.txt')
		arquivo = open(str(nome)+'.txt', 'w')
		grafox = networkx.from_pydot(self.grafo)
		grafox = grafox.to_undirected()
		listaNo = grafox.nodes()
		for i in range(0, len(listaNo)):
			vizinhos = grafox.neighbors(listaNo[i])
			linha = ""
			for j in range(0, len(listaNo)):
				if listaNo[j] in vizinhos:
					linha+="1\t"
					#print listaNo[i]+"("+str(i)+") -- " + listaNo[j]+"("+str(j)+")"
				else:
					linha+="0\t"
			linha = linha[0:-1]+"\n"
			arquivo.write(linha)

	#def criarParticao(self):
		#listaSubg = self.grafo.get_subgraph_list()
		#temM=False
		#for subg in listaSubg:
			#if subg.get_name=='X' or subg.get_name=='Y':
				#return
			#if subg.get_name=='M':
				#temM = True
		#grafox = networkx.from_pydot(self.grafo)
		#listaNo = grafox.nodes()
		#X=[listaNo[0]]
		#Y=[]
		#for i in range(0,len(listaNo)):
			#vizinhos = grafox.neighbors(listaNo[i])
			#for j in vizinhos:
				#if i in X and i not in Y:
					#Y.append(j)
				#elif i not in X:
					#X.append(j)
		#subX = pydot.subgraph(graph_name='X', directed=False)
		#for no in X:
			#subX.add_node(no)
		#subY = pydot.subgraph(graph_name='Y', directed=False)
		#for no in Y:
			#subY.add_node(no)
		#self.grafo.add_subgraph(subX)
		#self.grafo.add_subgraph(subY)
		
		#subM = pydot.Subgraph(graph_name='M', directed=False)
		#if len(self.grafo.get_edge_list())>0:
			#subM.add_edge(self.grafo.get_edge_list()[0])



	def escolherEmparelhamento(self):
		grafox = networkx.from_pydot(self.grafo)
		temM=False
		
		novoGrafo = pydot.Dot(graph_type='graph')
		for vertice in self.grafo.get_node_list():
			novoGrafo.add_node(vertice)
		for subg in self.grafo.get_subgraph_list():
			if subg.get_name()!='M':
				subg.set_rank('same')
				novoGrafo.add_subgraph(subg)
				subg.set_rank('same')
		subM = pydot.Subgraph('')
		subM.set_name('M')
		novoGrafo.add_subgraph(subM)
		
		
					
		verticeVizinho = []
		fim=False
		while not fim:
			print "digite o nome do no fonte, nada para listar arestas, ou fim para terminar"
			fonte = raw_input(">> ")
			if fonte=='':
				for aresta in self.grafo.get_edge_list():
					print " aresta:("+str(aresta.get_source())+", "+str(aresta.get_destination())+")"
				for aresta in subM.get_edge_list():
					print " M:("+str(aresta.get_source())+", "+str(aresta.get_destination())+")"
			elif fonte == 'fim':
				fim = True
			else:
				print "digite o no alvo"
				alvo = raw_input(">> ")
				if (fonte,alvo) in grafox.edges():
					if fonte not in verticeVizinho and alvo not in verticeVizinho:
						#self.grafo.del_edge(pydot.Edge(fonte, alvo))
						subM.add_edge(pydot.Edge(fonte, alvo))
						verticeVizinho.append(fonte)
						verticeVizinho.append(alvo)
						print " inserido:("+str(fonte)+", "+str(alvo)+") em M"
					else:
						print "aresta invalido, M deve conter arestas com vertice em comum"
				else:
					print "nao existe tal aresta"
			print ""
			
		subMx = networkx.from_pydot(subM)
		for aresta in grafox.edges():
			if aresta not in subMx.edges():
				novoGrafo.add_edge(pydot.Edge(aresta[0], aresta[1]))
		self.grafo = novoGrafo
		print self.grafo.to_string()
		return





















