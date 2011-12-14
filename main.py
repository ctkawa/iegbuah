# -*- coding: utf-8 -*-
import emparelhamento
#import Tkinter
#import tkMessageBox
#import tkFileDialog
import time
import os

class Main:
	def __init__(self):
		self.hungaro = emparelhamento.Hungaro()
		
		#self.janela = Tkinter.Tk()
		#self.janela.title("IEGBUAH")
		#self.janela.geometry("300x500+100+100")
		
		self.telaInicio()
		self.telaPrincipal()
		self.telaFinal()
		#self.janela.mainloop()
	
	def telaInicio(self):
		os.system('clear')
		
		#self.frame = Tkinter.Frame(self.janela)
		#self.frame.pack()
		
		#f = Tkinter.Frame(self.frame)
		#f.pack()
		
		#ltitulo = Tkinter.Label(f, text="IEGBUAH")
		#ltitulo.pack()
		
		print "IEGBUAH"
		
		#ldescricao = Tkinter.Label(f, text="Implementacao de\nEmparelhamento de\nGrafo Bipartido\nUtilizando o\nAlgoritmo Hungaro")
		#ldescricao.pack()
		
		print "\tImplementacao de\n\tEmparelhamento de\n\tGrafo Bipartido\n\tUtilizando o\n\tAlgoritmo Hungaro"
		
		#ltitulo = Tkinter.Label(f, text="\n\n\nThe Best of The Beatles!\n\n\n")
		#ltitulo.pack()
		
		#bnext = Tkinter.Button(f, text="Iniciar", command = self.telaPrincipal )
		#bnext.pack()
		
		time.sleep(3)
		
		return
		
	
	def telaFinal(self):
		os.system('clear')
		#self.frame.destroy()
		
		#self.frame = Tkinter.Frame(self.janela)
		#self.frame.pack()
		
		#f = Tkinter.Frame(self.frame)
		#f.pack()
		
		#ltitulo = Tkinter.Label(f, text="IEGBUAH")
		#ltitulo.pack()
		
		print "IEGBUAH"
		
		#ldescricao = Tkinter.Label(f, text="Implementacao de\nEmparelhamento de\nGrafo Bipartido\nUtilizando o\nAlgoritmo Hungaro")
		#ldescricao.pack()
		
		print "\tImplementacao de\n\tEmparelhamento de\n\tGrafo Bipartido\n\tUtilizando o\n\tAlgoritmo Hungaro"
		
		#ltitulo = Tkinter.Label(f, text="\n\n\nRun, Lola, Run!\n\n\n")
		#ltitulo.pack()
		
		#bnext = Tkinter.Button(f, text="Sair", command = self.janela.destroy )
		#bnext.pack()
		
		time.sleep(3)
		
	
	def telaPrincipal(self):
		os.system('clear')
		
		#self.frame.destroy()
		
		#self.frame = Tkinter.Frame(self.janela)
		#self.frame.pack()
		
		#f = Tkinter.Frame(self.frame)
		#f.pack()
		
		#ltitulo = Tkinter.Label(f, text="IEGBUAH")
		#ltitulo.pack()
		
		print "IEGBUAH"

		#action = 0
		#radioMtzAdj = Tkinter.Radiobutton(f, text = 'Matriz de Adcacencia', variable = action, value = 0)
		#radioMtzAdj.select()
		#radioMtzAdj.pack()
		#Tkinter.Radiobutton(f, text = 'Dot', variable = action, value = 1).pack()
		#Tkinter.Radiobutton(f, text = 'action C', variable = action, value = 2).pack()
		#bopen = Tkinter.Button(f, text="Abrir", command = self.janela.destroy )
		#bopen.pack()
		
		
		# pede o endereço da imagem
		self.emparelhar()

		## mostra o grafo
		
		#f1 = Tkinter.Frame(f)
		#f1.pack()
		
		#sb1x = Tkinter.Scrollbar(f1, orient=Tkinter.HORIZONTAL)
		#sb1y = Tkinter.Scrollbar(f1, orient=Tkinter.VERTICAL)
		
		#img1 = Tkinter.PhotoImage(file='grafo.gif')
		#lgrafoIn = Tkinter.Canvas(f1, xscrollcommand=sb1x.set, yscrollcommand=sb1y.set)
		
		#sb1x.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)
		#sb1x.config(command=lgrafoIn.xview)
		
		#sb1y.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
		#sb1y.config(command=lgrafoIn.yview)
		
		#lgrafoIn.create_image((0,0), image=img1)
		#lgrafoIn.img1 = img1
		#lgrafoIn.pack()
		
		##bAbrir = Tkinter.Button(f, text="Abrir...", command = self.abrirArquivoMatrizAdjacente() )
		##bAbrir.pack()
		
		#f2 = Tkinter.Frame(f)
		#f2.pack()
		
		#sb2x = Tkinter.Scrollbar(f2, orient=Tkinter.HORIZONTAL)
		#sb2y = Tkinter.Scrollbar(f2, orient=Tkinter.VERTICAL)
		
		#img2 = Tkinter.PhotoImage(file='grafoEmparelhado.gif')
		#lgrafoOut = Tkinter.Canvas(f2, xscrollcommand=sb2x.set, yscrollcommand=sb2y.set)
		
		#sb2x.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)
		#sb2x.config(command=lgrafoOut.xview)
		
		#sb2y.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
		#sb2y.config(command=lgrafoOut.yview)
		
		#lgrafoOut.create_image((0,0), image=img2)
		#lgrafoOut.img2 = img2
		#lgrafoOut.pack()
		
		#bnext = Tkinter.Button(f, text="Terminar", command = self.telaFinal )
		#bnext.pack()
		
		return
	
	
	def emparelhar(self):
		
		
		#filename = tkFileDialog.askopenfilename()
		
		
		tipoEscolhido = False
		while not tipoEscolhido:
			
			print "\nEscolha o tipo de arquivo: \n"
			
			print "\t[1] Matriz de Adjacência"
			print "\t[2] Descrição em Linguagem Dot"
			
			print "\n"
			
			tipo = raw_input(">> ")
			
			if tipo == '1':
				self.hungaro.lerGrafoDoArquivoMatrizAdjacente("MatrizAdjacencia.txt", "vn.txt")
				tipoEscolhido = True
			elif tipo == '2':
				self.hungaro.lerGrafoDoArquivoDot("grafo2.dot")
				tipoEscolhido = True
		
		#print "Abrindo..."
		
		#filename = tkFileDialog.askopenfilename(filetypes = [('Text Files', ('.txt', '.py'))], initialdir = "~")
		#filename = tkFileDialog.askopenfilename()
		#filename = "/home/cleber/Documents/UFSCar/TG/projeto_final/MatrizAdjacencia.txt"
		#filename = "grafo2.dot"
		#if filename != "":
			#self.hungaro.lerGrafoDoArquivoMatrizAdjacente(filename)
		#	self.hungaro.lerGrafoDoArquivoDot(filename)
		#exit()
		
		self.hungaro.geraImagemGrafoInicial()
		print("imagem do grafo inicial gerada.")
		self.hungaro.aplicaHungaro()
		self.hungaro.geraImagemGrafoEmparelhado()
		print("imagem do grafo resultante gerada.")
		self.hungaro.exportarParaMatrizAdj("matrizAdjResultado.txt")
		return


m = Main()
