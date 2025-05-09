import tkinter as tk
from tkinter import messagebox
import random

# Caracteres disponíveis para a senha
letras = 'abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ!@#$%¨&*()-=+.?0123456789'

def gerar_senhas():
    try:
        qtd_senhas = int(entry_qtd_senhas.get())
        tamanho = int(entry_tamanho.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos.")
        return

    if qtd_senhas <= 0 or tamanho <= 0:
        messagebox.showwarning("Aviso", "Os valores devem ser maiores que zero.")
        return

    output.delete('1.0', tk.END)

    for _ in range(qtd_senhas):
        senha = ''.join(random.choice(letras) for _ in range(tamanho))
        output.insert(tk.END, senha + '\n')

# Interface gráfica
root = tk.Tk()
root.title("Gerador de Senhas")

tk.Label(root, text="Quantidade de senhas:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_qtd_senhas = tk.Entry(root)
entry_qtd_senhas.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Quantidade de caracteres da senha:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_tamanho = tk.Entry(root)
entry_tamanho.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Gerar Senhas", command=gerar_senhas).grid(row=2, column=0, columnspan=2, pady=10)

output = tk.Text(root, height=10, width=40)
output.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
