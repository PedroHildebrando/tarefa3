import tkinter as tk 
import subprocess as sp 
import relogio 

janela = tk.Tk() 
janela.title("Sistema inicial") 
janela.geometry("300x300") 
janela.configure(bg="#43948e") 

def abrir_relogio(): 
    relogio.janela_relogio() 

def fechar_janela(): 
    janela.destroy() 

texto = tk.Label(janela, text="Janela principal", bg="#43948e", font=("Arial",20)) 
texto.pack(pady=20) 

tk.Label(janela, text= "Deseje abrir o relogio?", bg="#43948e").pack(pady=10)
verrelogio = tk.Button(janela, text="horário", font=("Arial",15), command=abrir_relogio, relief="solid") 
verrelogio.pack(pady=20) 

tk.Label(janela, text= "Realmente deseje fechar?", bg="#43948e").pack(pady=10)
fechar = tk.Button(janela, text="Fechar", font=("Arial",15), command=fechar_janela, relief="solid") 
fechar.pack(pady=20) 

janela.mainloop() 