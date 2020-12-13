from tkinter import *

def solicita_nomes_disciplinas():
	cont = 1
	fim = False
	disciplina = input("Digite o nome da disciplina:")
	lista_discilplinas[0] = disciplina
	
	while(fim == False):
		print("Deseja adicionar o nome de mais alguma disciplina?")
		resp = input("Pressione ENTER para prosseguir ou digite N para e pressione ENTER se já digitou todos os nomes das discilpinas")
		if (resp == "N"):
			fim = True
		else:
			disciplina = input("Digite o nome da disciplina:")
			lista_discilplinas[cont] = disciplina

#def solicita_raiz_da_estrutura()
#	tkinter.messagebox.showinfo(title="")
#	Ok, agora nós temos os nomes das disciplinas.Selecione na tela a seguir onde as pastas deverão ser criadas.")

if __name__ == '__main__':

	tkinter.messagebox.showinfo(title="create-dir-for-each-classes",message="Criador de estrutura de diretórios para disciplinas da faculdade\n================================================================\n=================== Criado por Otavio Ramos ====================")

	lista_discilplinas = {}

	print("Para podermos criar a estrutura de diretórios, digite abaixo, conforme solicitado, os nomes das disciplinas.")

	solicita_nomes_disciplinas()


	