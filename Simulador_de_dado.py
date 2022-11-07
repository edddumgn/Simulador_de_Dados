
import random
import PySimpleGUI as sg
class SimuladorDeDado:
	def __init__(self):
		self.valor_minimo = 1
		self.valor_maximo = 6
		self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '
		sg.theme('Dark Grey 13')

		self.layout = [[sg.Text(('Deseja jogar o dado? '),size=(35,5))],
			[sg.Button(('Sim'),size=(15,1))], [sg.Button(('Não'),size=(15,1))],
		]
	
	def Iniciar(self):
		self.window = sg.Window('Simulador de dados', self.layout)
		self.eventos, self.valores = self.window.read()
		try:
			if self.eventos == 'Sim':
				self.ValorAleatorio()
		
			elif self.eventos =='Não':
				print('Tudo bem! Volte sempre!')			
		except:
			print('Ocorreu um erro, tente novamente mais tarde!')
	def ValorAleatorio(self):
		print(f'O valor tirado no dado é {random.randint(self.valor_minimo, self.valor_maximo)}!')


simulador = SimuladorDeDado()
simulador.Iniciar()		
