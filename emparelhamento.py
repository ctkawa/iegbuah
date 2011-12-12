# -*- coding: utf-8 -*-
import pydot

class Hungaro:
	def texto(self):
		return "Algoritmo Hungaro"
	
	def lerGrafoDoArquivoMatrizAdjacente(self, caminho):
		print "Lendo: "+caminho
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
		
		#self.grafo = pydot.Dot('Grafo', graph_type='graph' )
		#self.subgrafox = pydot.Subgraph('X', rank='same' )
		#self.subgrafoy = pydot.Subgraph('Y', rank='same' )
		#self.grafo.add_subgraph( self.subgrafox )
		#self.grafo.add_subgraph( self.subgrafoy )
		
		#self.subgrafox.add_node(  pydot.Node("A") )
		#self.subgrafox.add_node(  pydot.Node("B") )
		#self.subgrafox.add_node(  pydot.Node("C") )
		
		#self.subgrafoy.add_node(  pydot.Node("D") )
		#self.subgrafoy.add_node(  pydot.Node("E") )
		#self.subgrafoy.add_node(  pydot.Node("F") )
		#self.subgrafoy.add_node(  pydot.Node("G") )
		#self.subgrafoy.add_node(  pydot.Node("H") )
		
		#self.grafo.add_edge( pydot.Edge("A", "E") )
		#self.grafo.add_edge( pydot.Edge("A", "F") )
		#self.grafo.add_edge( pydot.Edge("A", "G") )
		#self.grafo.add_edge( pydot.Edge("B", "E") )
		#self.grafo.add_edge( pydot.Edge("B", "F") )
		#self.grafo.add_edge( pydot.Edge("B", "H") )
		#self.grafo.add_edge( pydot.Edge("C", "F") )
		#self.grafo.add_edge( pydot.Edge("C", "G") )
		#self.grafo.add_edge( pydot.Edge("C", "H") )
		
		
		self.identificaBiparticao()
		self.geraImagemGrafoInicial()
		self.aplicaHungaro()
		self.geraImagemGrafoEmparelhado()
		
	def identificaBiparticao(self):
		
		# ...
		
		return
	
	def geraImagemGrafoInicial(self):
		self.grafo.write_gif('grafo.gif')
		#print dot
		
		#img = gv.readstring(dot)
		#gv.layout(img, 'dot')
		#gv.render(img, 'png', 'grafo.png')
		
		#novodot = "graph graphname {splines=true;A;B;C;D;E;F;A -- D;A -- E;B -- E;B -- F;C -- D;}"
		#dot = "graph graphname {{ rank=same; 1 2 3 4 5 6 7 8 9 10 11 12 13 14 }{ rank=same; 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31} 24;25;26;27;20;21;22;23;28;29;1;3;2;5;4;7;6;9;8;11;10;13;12;15;14;17;16;19;18;31;30;6 -- 20;25 -- 9;2 -- 17;1 -- 20;24 -- 8;15 -- 3;16 -- 8;30 -- 9;5 -- 23;22 -- 6;17 -- 9;26 -- 9;20 -- 5;7 -- 29;8 -- 15;19 -- 7;9 -- 27;18 -- 8;8 -- 29;17 -- 8;2 -- 15;3 -- 18;9 -- 28;8 -- 26;9 -- 31;29 -- 11;6 -- 15;12 -- 26;27 -- 8;10 -- 30;13 -- 26;3 -- 20;8 -- 23;6 -- 17;12 -- 28;10 -- 28;29 -- 12;1 -- 19;4 -- 19;25 -- 10;21 -- 8;7 -- 28;15 -- 4;24 -- 7;12 -- 25;29 -- 14;9 -- 22;18 -- 1;20 -- 8;13 -- 28;23 -- 7;12 -- 30;16 -- 5;28 -- 11;8 -- 22;18 -- 6;15 -- 9;31 -- 11;16 -- 6;27 -- 13;17 -- 3;18 -- 7;28 -- 14;23 -- 1;8 -- 25;7 -- 17;5 -- 21;16 -- 7;21 -- 6;27 -- 12;30 -- 8;27 -- 7;18 -- 4;24 -- 9;7 -- 21;17 -- 1;10 -- 27;29 -- 13;18 -- 5;16 -- 1;6 -- 28;26 -- 14;16 -- 2;5 -- 17;1 -- 22;16 -- 3;26 -- 10;5 -- 19;15 -- 5;12 -- 24;27 -- 14;17 -- 4;3 -- 19;29 -- 10;1 -- 15;9 -- 23;}"
		#img = gv.readstring(novodot)
		#gv.layout(img, 'dot')
		#gv.render(img, 'png', 'grafo.png')
		
		#img = dot_parser.parse_dot_data(dot)
		#img.write_gif('grafo.gif')
		
		return
	
	def aplicaHungaro(self):
		
		self.grafoEmp = self.grafo
		
		partX = self.grafoEmp.get_subgraph('X')
		partY = self.grafoEmp.get_subgraph('Y')
		
		# Passo 1 inicializa emparelhamento M
		
		# Passo 2 busca vertice de X nao saturado por arestas de M
		
		for no in partX.get_node_list():
			is_saturada = False
			for aresta in self.grafoEmp.get_edge_list:
				if 'dotted' == aresta.get_style() and (no.get_name == aresta.get_destination() or no.get_name == aresta.get_source()):
					is_saturada = True
			if !is_saturada:
				S = [no]
				T = []
				# Passo 3 N (S ) == T -> STOP
				#y de N (S ) que nao esteja em T
				
				# Passo 4
				# se y eh saturado, S+= vertice de ligada a y, e T+=y , GOTO Passo 3
				# senao transferencia de no ate y , GOTO Passo 2
				
		
			
		
		
		
		
		
		
		return
		
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
	