import tkinter as tk
from tkinter import ttk

# Dicionário para armazenar o status das peças enviadas e recebidas
pecas_status = {}

# Função para simular o envio de peças
def enviar_pecas():
    quantidade = entry_quantidade.get()
    material = entry_material.get()
    
    if material and quantidade.isdigit():
        quantidade = int(quantidade)
        pecas_status[material] = "Enviado"
        status_label.config(text=f"{quantidade} peças do material '{material}' enviadas com sucesso!", fg="green")
    else:
        status_label.config(text="Insira o número do material e uma quantidade válida.", fg="red")

# Função para simular o recebimento de peças
def receber_pecas():
    quantidade = entry_quantidade_devolvidas.get()
    material = entry_material.get()
    
    if material in pecas_status and pecas_status[material] == "Enviado" and quantidade.isdigit():
        quantidade = int(quantidade)
        pecas_status[material] = "Devolvido"
        status_label.config(text=f"{quantidade} peças do material '{material}' devolvidas com sucesso!", fg="blue")
    else:
        status_label.config(text="Nenhum envio correspondente para este material ou quantidade inválida.", fg="red")

# Função para verificar o status de uma peça
def verificar_status():
    material = entry_material_status.get()
    
    if material in pecas_status:
        status_atual = pecas_status[material]
        status_label.config(text=f"Material '{material}' está com status: {status_atual}.", fg="black")
    else:
        status_label.config(text="Material não encontrado.", fg="red")

# Configuração da janela principal
root = tk.Tk()
root.title("G.E.I FLOW - Gerenciador de Envio e Recebimento de Peças")
root.geometry("700x500")
root.config(bg="#f0f8ff")  # Azul claro para o fundo

# Título
title_label = ttk.Label(root, text="G.E.I FLOW", font=("Arial", 24, "bold"), background="#4a90e2", foreground="white", padding=10)
title_label.pack(pady=10, fill='x')

# Envio de Peças - Frame
frame_envio = ttk.LabelFrame(root, text="Envio de Peças", padding=(20, 10), relief="solid")
frame_envio.pack(pady=10, padx=10, fill="x")

label_quantidade = ttk.Label(frame_envio, text="Quantidade a Enviar:", font=("Arial", 12))
label_quantidade.pack(side="left", padx=5)

entry_quantidade = ttk.Entry(frame_envio, width=10, font=("Arial", 12))
entry_quantidade.pack(side="left", padx=5)

label_material = ttk.Label(frame_envio, text="Número do Material:", font=("Arial", 12))
label_material.pack(side="left", padx=5)

entry_material = ttk.Entry(frame_envio, width=15, font=("Arial", 12))
entry_material.pack(side="left", padx=5)

btn_enviar = ttk.Button(frame_envio, text="Enviar", command=enviar_pecas)
btn_enviar.pack(side="left", padx=10)

# Recebimento de Peças - Frame
frame_recebimento = ttk.LabelFrame(root, text="Recebimento de Peças", padding=(20, 10), relief="solid")
frame_recebimento.pack(pady=10, padx=10, fill="x")

label_quantidade_devolvidas = ttk.Label(frame_recebimento, text="Quantidade Devolvidas:", font=("Arial", 12))
label_quantidade_devolvidas.pack(side="left", padx=5)

entry_quantidade_devolvidas = ttk.Entry(frame_recebimento, width=10, font=("Arial", 12))
entry_quantidade_devolvidas.pack(side="left", padx=5)

label_material_recebido = ttk.Label(frame_recebimento, text="Número do Material:", font=("Arial", 12))
label_material_recebido.pack(side="left", padx=5)

entry_material_devolvido = ttk.Entry(frame_recebimento, width=15, font=("Arial", 12))
entry_material_devolvido.pack(side="left", padx=5)

btn_receber = ttk.Button(frame_recebimento, text="Receber", command=receber_pecas)
btn_receber.pack(side="left", padx=10)

# Verificação de Status - Frame
frame_status = ttk.LabelFrame(root, text="Verificar Status da Peça", padding=(20, 10), relief="solid")
frame_status.pack(pady=10, padx=10, fill="x")

label_material_status = ttk.Label(frame_status, text="Número do Material:", font=("Arial", 12))
label_material_status.pack(side="left", padx=5)

entry_material_status = ttk.Entry(frame_status, width=15, font=("Arial", 12))
entry_material_status.pack(side="left", padx=5)

btn_verificar_status = ttk.Button(frame_status, text="Verificar", command=verificar_status)
btn_verificar_status.pack(side="left", padx=10)

# Prazos e Dias de Trabalho - Frame
frame_prazos = ttk.LabelFrame(root, text="Prazos e Dias de Trabalho", padding=(20, 10), relief="solid")
frame_prazos.pack(pady=10, padx=10, fill="x")

label_prazo = ttk.Label(frame_prazos, text="Prazo de Entrega (dias):", font=("Arial", 12))
label_prazo.pack(side="left", padx=5)

prazo_spinbox = ttk.Spinbox(frame_prazos, from_=1, to=30, width=5, font=("Arial", 12))
prazo_spinbox.pack(side="left", padx=5)

label_dias_trabalho = ttk.Label(frame_prazos, text="Dias de Trabalho/semana:", font=("Arial", 12))
label_dias_trabalho.pack(side="left", padx=5)

dias_spinbox = ttk.Spinbox(frame_prazos, from_=1, to=7, width=5, font=("Arial", 12))
dias_spinbox.pack(side="left", padx=5)

# Status de Operação
status_label = ttk.Label(root, text="", font=("Arial", 14), background="#f0f8ff", padding=10)
status_label.pack(pady=20)

# Rodapé
footer_label = ttk.Label(root, text="G.E.I FLOW - Gerenciamento de Envio e Recebimento de Peças", font=("Arial", 10), background="#f0f8ff")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
