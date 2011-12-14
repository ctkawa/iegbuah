# -*- coding: utf-8 -*-
import emparelhamento
import time
import os

class Main:
	def __init__(self):
		self.hungaro = emparelhamento.Hungaro()
		
		self.telaInicio()
		self.telaPrincipal()
		self.telaFinal()
		
	
	def telaInicio(self):
		os.system('clear')
		
		print "IEGBUAH"
		
		print "\tImplementacao de\n\tEmparelhamento de\n\tGrafo Bipartido\n\tUtilizando o\n\tAlgoritmo Hungaro"
		
		time.sleep(3)
		
		return
		
	
	def telaFinal(self):
		os.system('clear')
		
		print "IEGBUAH"
		
		print "\tImplementacao de\n\tEmparelhamento de\n\tGrafo Bipartido\n\tUtilizando o\n\tAlgoritmo Hungaro"
		
		time.sleep(3)
		
	
	def telaPrincipal(self):
		os.system('clear')
		
		
		print "IEGBUAH"

		self.emparelhar()

		
		return
	
	
	def emparelhar(self):
		
		
		tipoEscolhido = False
		while not tipoEscolhido:
			
			print "\nEscolha o tipo de arquivo: \n"
			
			print "\t[1] Matriz de Adjacência"
			print "\t[2] Descrição em Linguagem Dot"
			print "\t[3] Matriz de Adjacência, escolher arestas"
			print "\t[4] Descrição em Linguagem Dot, escolher arestas"
			
			print "\n"
			
			tipo = raw_input(">> ")
			
			if tipo == '1':
				nome = raw_input("digite o nome da matriz: ")
				nomeR = raw_input("digite o nome do arquivo de rotulo: ")
				self.hungaro.lerGrafoDoArquivoMatrizAdjacente(nome, nomeR)
				tipoEscolhido = True
			elif tipo == '2':
				nome = raw_input("digite o nome do arquivo dot/gv: ")
				self.hungaro.lerGrafoDoArquivoDot(nome)
				tipoEscolhido = True
			elif tipo == '3':
				nome = raw_input("digite o nome da matriz: ")
				nomeR = raw_input("digite o nome do arquivo de rotulo: ")
				self.hungaro.lerGrafoDoArquivoMatrizAdjacente(nome, nomeR)
				self.hungaro.escolherEmparelhamento()
				tipoEscolhido = True
			elif tipo == '4':
				nome = raw_input("digite o nome do arquivo dot/gv: ")
				self.hungaro.lerGrafoDoArquivoDot(nome)
				self.hungaro.escolherEmparelhamento()
				tipoEscolhido = True
		
		
		
		self.hungaro.geraImagemGrafoInicial()
		print("imagem do grafo inicial gerada.")
		self.hungaro.aplicaHungaro()
		self.hungaro.geraImagemGrafoEmparelhado()
		print("imagem do grafo resultante gerada.")
		return


m = Main()
