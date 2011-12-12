# -*- coding: utf-8 -*-
import pydot

class Hungaro:
	def texto(self):
		return "Algoritmo Hungaro"
	
	def lerGrafoDoArquivoMatrizAdjacente(self, caminho):
		#arquivo = open(caminho, 'r')
		#self.grafo = graph()
		#MAX_NO = 100
		
		#loop de 1 ate MAX_NO inclusive
		#for i in range(1, MAX_NO+1):
			#linha = arquivo.readline()
			#if linha!='':
				#lista = linha.split('\t')
				#if i==1:
					#lista_no = []
					#contagem = 1
					#for no in range(linha.count('\t')):
						#lista_no.insert(0, str(contagem))
						#print 'insert: '+str(contagem)
						#contagem+=1
					#self.grafo.add_nodes(lista_no)
				#j = 1
				#for cell in lista:
					##	e = (''+str(j), ''+str(i))
					#if cell == '1' and j>i:
						#self.grafo.add_edge((''+str(j), ''+str(i)))
						##self.grafo.set_edge_weight(e, 1)
						#print 'add Edge: ' + str(j) + ' - ' + str(i)
					##elif cell == '2' and j>i:
					##	grafo.add_edge(e)
					##	grafo.set_edge_weight(e, 2)
					##	print 'add Edge Emparelhado: ' + str(j) + ' - ' + str(i)
					#j+=1
			#else:
				#break
		
		self.grafo = pydot.Dot('Grafo', graph_type='graph' )
		self.subgrafox = pydot.Subgraph('X', rank='same' )
		self.subgrafoy = pydot.Subgraph('Y', rank='same' )
		self.grafo.add_subgraph( self.subgrafox )
		self.grafo.add_subgraph( self.subgrafoy )
		
		self.subgrafox.add_node(  pydot.Node("A") )
		self.subgrafox.add_node(  pydot.Node("B") )
		self.subgrafox.add_node(  pydot.Node("C") )
		
		self.subgrafoy.add_node(  pydot.Node("D") )
		self.subgrafoy.add_node(  pydot.Node("E") )
		self.subgrafoy.add_node(  pydot.Node("F") )
		self.subgrafoy.add_node(  pydot.Node("G") )
		self.subgrafoy.add_node(  pydot.Node("H") )
		
		self.grafo.add_edge( pydot.Edge("A", "E") )
		self.grafo.add_edge( pydot.Edge("A", "F") )
		self.grafo.add_edge( pydot.Edge("A", "G") )
		self.grafo.add_edge( pydot.Edge("B", "E") )
		self.grafo.add_edge( pydot.Edge("B", "F") )
		self.grafo.add_edge( pydot.Edge("B", "H") )
		self.grafo.add_edge( pydot.Edge("C", "F") )
		self.grafo.add_edge( pydot.Edge("C", "G") )
		self.grafo.add_edge( pydot.Edge("C", "H") )
		
		
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
		
		# ...
		
		return
		
	def geraImagemGrafoEmparelhado(self):
		
		self.grafoEmp.write_gif('grafoEmparelhado.gif')
		
		return
	