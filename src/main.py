import tkinter as tk
from tkinter import messagebox, filedialog, messagebox
import os, sys

class Configuracoes:
	lista_de_disciplinas = []
	diretorio_raiz = ""
	mais = True
	contador = 0

def solicita_nomes_disciplinas():
	tela_solicita_disciplina()

def tela_solicita_disciplina():
	print("Processo de input do usuário...")
	cria_tela()

def cria_tela():

	def submit():
		print("Salvando o input...")
		config.lista_de_disciplinas.append(disciplina_var.get())
		verifica_caso_finalizado()
		print("Verificando se há mais alguma disciplina...")
		if(config.mais == True):
			print("Há mais disciplinas, destruindo a tela anterior e criando uma nova...")
			tela.destroy()
			cria_tela()
		else:
			print("Não há mais disciplinas...")
			tela.destroy()
			define_raiz()
			cria_pastas()
	
	print("criando tela...")
	tela = tk.Tk()
	tela.geometry("185x80")

	disciplina_var = tk.StringVar()
			
	disciplina_label = tk.Label(tela, text = 'Digite o nome da disciplina', font=('calibre', 10, 'bold'))
			
	disciplina_entry = tk.Entry(tela,textvariable = disciplina_var,font=('calibre',10,'normal'))

	enviar_btn =tk.Button(tela,text = 'Enviar', command = submit)

	disciplina_label.grid(row=0,column=0)
	disciplina_entry.grid(row=1,column=0)
	enviar_btn.grid(row=2,column=0)

	tela.mainloop()

def verifica_caso_finalizado():
	config.mais = messagebox.askyesno(title="Disciplina", message="Há mais alguma discilplina que você deseja adicionar?")

def define_raiz():
	messagebox.showinfo(title="Raiz",message="Na próxima tela, selecione onde você deseja criar as pastas.")
	print("Salvando diretório raiz para criação das pastas...")
	config.diretorio_raiz = filedialog.askdirectory()

def cria_pastas():
	print("Criando as pastas...")
	for disciplina in config.lista_de_disciplinas:
		try:
			print("Criando a pasta {0}".format(disciplina))
			os.mkdir(os.path.join(str(config.diretorio_raiz), str(disciplina)))
		except:
			print("Ocorreu um erro...")
			messagebox.showerror(title="Erro",message="Erro durante a criação dos diretórios.")
			sys.exit()

	messagebox.showinfo(title="Fim", message="As pastas para as disciplinas solicitadas foram criadas")
	sys.exit()

if __name__ == "__main__":
	config = Configuracoes()
	solicita_nomes_disciplinas()