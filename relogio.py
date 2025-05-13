import tkinter as tk 
import time 
def janela_relogio():
        
    def fechar_janela(): 
        janela.destroy() 

    # Função que atualiza o relógio 
    def atualizar_relogio() : 
        tempo_atual = time.strftime("%H:%M:%S") # Formato: horas:minutos:segundos 
        relogio.config(text=tempo_atual)  # Atualiza o texto do label 
        relogio.after(1000, atualizar_relogio)  # Chama a função novamente após 1000ms (1 segundo) 

    # Criando a janela principal 
    janela = tk.Tk() 
    janela.title("Relógio Digital")  # Título da janela 
    janela.geometry("300x150")  # Tamanho da janela 
    tk.Label(janela, text= "Horario de Brasilia: ").pack(pady=10) 

    # Criando o label para mostrar a hora 
    relogio = tk.Label(janela, font=("Hariel", 48), bg="black", fg="white") 
    relogio.pack(expand=True) 
    tk.Button(janela, text="Fechar", command=fechar_janela).pack(pady=20) 

    # Chama a função para atualizar a hora 
    atualizar_relogio() 

    # Inicia o loop da interface gráfica 
  