
import random

class SimuladorDeDado:
	def __init__(self):
		self.valor_minimo = 1
		self.valor_maximo = 6
		self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '
	
	
	def Iniciar(self):
		try:
			resposta = input(self.mensagem)
			if resposta in 'Simsim':
				self.ValorAleatorio()
			elif resposta in 'Nãonão':
				resposta =print('Tudo bem! Volte sempre!')
				return resposta
			else:
				print('Favor digitar Sim ou Não')	
		except:
			print('Ocorreu um erro, tente novamente mais tarde!')
	
	def ValorAleatorio(self):
		print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()		
