import tkinter as tk
from tkinter import messagebox
import random

# Listas de palavras relacionadas à liderança
categorias = {
    "Características": ['empatia', 'comunicacao', 'motivacao', 'resiliencia', 'integridade', 'autoconfiança', 'humildade', 'proatividade', 'visao', 'autodisciplina'],
    "Habilidades": ['estrategia', 'tomada de decisao', 'gestao', 'negociacao', 'resolucao de conflitos', 'delegacao', 'planejamento', 'mentoria', 'inovacao', 'feedback'],
    "Equipe": ['colaboracao', 'inclusao', 'confiança', 'diversidade', 'trabalho em team', 'empoderamento', 'sinergia', 'desempenho', 'cooperacao', 'engajamento']
}

# Função do Jogo da Forca
def jogo_forca():
    def selecionar_categoria():
        janela_categoria = tk.Toplevel()
        janela_categoria.title("Escolher Categoria")

        tk.Label(janela_categoria, text="Escolha uma categoria:", font=("Arial", 14)).pack(pady=10)
        
        def iniciar_jogo(categoria):
            nonlocal palavra_secreta
            palavra_secreta = random.choice(categorias[categoria])
            janela_categoria.destroy()
            atualizar_interface()

        for categoria in categorias:
            tk.Button(
                janela_categoria, text=categoria, font=("Arial", 12),
                command=lambda c=categoria: iniciar_jogo(c)
            ).pack(pady=5)

    def resetar_jogo():
        nonlocal palavra_secreta, letras_acertadas, letras_erradas, tentativas_restantes
        selecionar_categoria()  # Permite escolher uma nova categoria
        letras_acertadas = ""
        letras_erradas = ""
        tentativas_restantes = 6

    def verificar_letra():
        nonlocal letras_acertadas, letras_erradas, tentativas_restantes

        letra = entrada_letra.get().lower()
        if not letra or len(letra) != 1:
            messagebox.showerror("Erro", "Digite apenas uma letra.")
            return

        if letra in letras_acertadas + letras_erradas:
            messagebox.showinfo("Atenção", "Você já digitou essa letra.")
            return

        if letra in palavra_secreta:
            letras_acertadas += letra
        else:
            letras_erradas += letra
            tentativas_restantes -= 1

        atualizar_interface()

        if tentativas_restantes == 0:
            messagebox.showinfo("Fim de jogo", f"Você perdeu! A palavra era: {palavra_secreta}")
            resetar_jogo()
        elif all(letra in letras_acertadas for letra in palavra_secreta):
            messagebox.showinfo("Parabéns", "Você ganhou!")
            resetar_jogo()

    def atualizar_interface():
        palavra_mostrada = ''.join([letra if letra in letras_acertadas else '*' for letra in palavra_secreta])
        label_palavra.config(text=f"Palavra: {palavra_mostrada}")
        label_tentativas.config(text=f"Tentativas restantes: {tentativas_restantes}")
        label_letras_erradas.config(text=f"Letras erradas: {', '.join(letras_erradas)}")
        entrada_letra.delete(0, tk.END)

    # Configurando a interface do jogo da forca
    janela_forca = tk.Toplevel()
    janela_forca.title("Jogo da Forca")
    letras_acertadas = ""
    letras_erradas = ""
    tentativas_restantes = 6
    palavra_secreta = ""

    label_palavra = tk.Label(janela_forca, text="Escolha uma categoria para começar!", font=("Arial", 16))
    label_palavra.pack(pady=10)

    label_tentativas = tk.Label(janela_forca, text=f"Tentativas restantes: {tentativas_restantes}", font=("Arial", 12))
    label_tentativas.pack(pady=5)

    label_letras_erradas = tk.Label(janela_forca, text="Letras erradas: ", font=("Arial", 12))
    label_letras_erradas.pack(pady=5)

    entrada_letra = tk.Entry(janela_forca, font=("Arial", 14))
    entrada_letra.pack(pady=5)

    botao_verificar = tk.Button(janela_forca, text="Verificar Letra", command=verificar_letra)
    botao_verificar.pack(pady=10)

    botao_resetar = tk.Button(janela_forca, text="Trocar Categoria", command=resetar_jogo)
    botao_resetar.pack(pady=10)

    selecionar_categoria()

# Função do Simulador de Decisões do Líder
def simulador_decisoes():
    cenarios = [
        {
            "cenario": "Um dos membros da sua equipe está desmotivado e entregando menos do que o esperado.",
            "opcoes": {
                "1": ("Conversa individualmente para entender a situação e oferecer apoio.", 10),
                "2": ("Dá um aviso formal, enfatizando a importância de cumprir metas.", -5),
                "3": ("Ignora o problema e foca em outros membros mais produtivos.", -10)
            }
        },
        {
            "cenario": "Dois membros estão discutindo frequentemente, prejudicando o trabalho.",
            "opcoes": {
                "1": ("Organiza uma reunião para mediar o conflito e encontrar uma solução conjunta.", 10),
                "2": ("Pede para que ambos resolvam o problema sozinhos.", -5),
                "3": ("Escolhe um lado e repreende o outro membro.", -10)
            }
        },
        {
            "cenario": "Você está sob pressão para entregar resultados rápidos em um projeto importante.",
            "opcoes": {
                "1": ("Prioriza a tarefa mais importante e delega as outras.", 10),
                "2": ("Decide fazer tudo sozinho para garantir a qualidade.", -5),
                "3": ("Sente-se sobrecarregado e compartilha sua frustração com a equipe.", -10)
            }
        }
    ]

    def exibir_cenario(index, pontuacao):
        if index >= len(cenarios):
            if pontuacao >= 20:
                messagebox.showinfo("Resultado", f"Parabéns! Você foi um excelente líder! Pontuação: {pontuacao}")
            elif pontuacao >= 10:
                messagebox.showinfo("Resultado", f"Você foi um líder razoável. Pontuação: {pontuacao}")
            else:
                messagebox.showinfo("Resultado", f"Sua liderança teve dificuldades. Pontuação: {pontuacao}")
            return

        cenario = cenarios[index]
        janela_cenario = tk.Toplevel()
        janela_cenario.title("Simulador de Decisões do Líder")

        tk.Label(janela_cenario, text=cenario["cenario"], font=("Arial", 14)).pack(pady=10)

        for key, (descricao, valor) in cenario["opcoes"].items():
            tk.Button(
                janela_cenario,
                text=f"{key}. {descricao}",
                font=("Arial", 12),
                command=lambda v=valor, i=index + 1: [
                    janela_cenario.destroy(),
                    exibir_cenario(i, pontuacao + v)
                ]
            ).pack(pady=5)

    exibir_cenario(0, 0)

# Interface principal
janela_principal = tk.Tk()
janela_principal.title("Jogos Interativos")
janela_principal.geometry("400x300")

label_titulo = tk.Label(janela_principal, text="Escolha seu jogo", font=("Arial", 18))
label_titulo.pack(pady=20)

botao_forca = tk.Button(janela_principal, text="Jogo da Forca", command=jogo_forca, font=("Arial", 14))
botao_forca.pack(pady=10)

botao_simulador = tk.Button(janela_principal, text="Simulador de Decisões", command=simulador_decisoes, font=("Arial", 14))
botao_simulador.pack(pady=10)

janela_principal.mainloop()
