# -*- coding: utf-8 -*-
import emparelhamento
import Tkinter
import time


class Main:
	
	def __init__(self):
		self.hungaro = emparelhamento.Hungaro()
		
		self.janela = Tkinter.Tk()
		self.janela.title("IEGBUAH")
		self.janela.geometry("300x500+100+100")
		
		self.telaInicio()
		self.janela.mainloop()
	
	def telaInicio(self):
		
		self.frame = Tkinter.Frame(self.janela)
		self.frame.pack()
		
		f = Tkinter.Frame(self.frame)
		f.pack()
		
		ltitulo = Tkinter.Label(f, text="IEGBUAH")
		ltitulo.pack()
		
		ldescricao = Tkinter.Label(f, text="Implementacao de\nEmparelhamento de\nGrafo Bipartido\nUtilizando o\nAlgoritmo Hungaro")
		ldescricao.pack()
		
		ltitulo = Tkinter.Label(f, text="\n\n\nThe Best of The Beatles!\n\n\n")
		ltitulo.pack()
		
		bnext = Tkinter.Button(f, text="Iniciar", command = self.telaPrincipal )
		bnext.pack()
		
	
	def telaFinal(self):
		
		self.frame.destroy()
		
		self.frame = Tkinter.Frame(self.janela)
		self.frame.pack()
		
		f = Tkinter.Frame(self.frame)
		f.pack()
		
		ltitulo = Tkinter.Label(f, text="IEGBUAH")
		ltitulo.pack()
		
		ldescricao = Tkinter.Label(f, text="Implementacao de\nEmparelhamento de\nGrafo Bipartido\nUtilizando o\nAlgoritmo Hungaro")
		ldescricao.pack()
		
		ltitulo = Tkinter.Label(f, text="\n\n\nRun, Lola, Run!\n\n\n")
		ltitulo.pack()
		
		bnext = Tkinter.Button(f, text="Sair", command = self.janela.destroy )
		bnext.pack()
		
	
	def telaPrincipal(self):
		self.frame.destroy()
		
		self.frame = Tkinter.Frame(self.janela)
		self.frame.pack()
		
		f = Tkinter.Frame(self.frame)
		f.pack()
		
		ltitulo = Tkinter.Label(f, text="IEGBUAH")
		ltitulo.pack()
		
		lgrafoIn = Tkinter.Label(f, text="\n\n\n\n\n<Grafo Bipartido de Entrada>\n\n\n\n\n")
		lgrafoIn.pack()
		
		lgrafoOut = Tkinter.Label(f, text="\n\n\n\n\n<Grafo Emparelhado de Saída>\n\n\n\n\n")
		lgrafoOut.pack()
		
		bnext = Tkinter.Button(f, text="Terminar", command = self.telaFinal )
		bnext.pack()
		


m = Main()
