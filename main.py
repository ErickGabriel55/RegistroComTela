# importando as bibliotecas
from tkinter import *
from datetime import datetime

# função para a criação de arquivo e de exibição na tela para o usuário
def pegarnomeestudo():
    # coleta as informações passadas nas entradas e nos radiobuttons
    en = entrada_nome.get()
    es = estudou_nome.get()
    re = registrado.get()
    nome_arquivo = f"{es}.txt".title()
    # coleta a hora atual
    agora = datetime.now()
    # condições para exibir na tela caso o usuário tenha terminado u começado
    if re == 'começou':
        estudado = Label(tela, text=f"{en} está começando a estudar {es};\nÀs {agora.strftime('%H:%M')} na data {agora.strftime('%d/%m/%Y')}", font=('Montserrat Thin Regular', 11, 'bold'), fg=cor2, bg=cor4)
        estudado.place(x=20, y=315)
    elif re == 'terminou':
        estudado = Label(tela, text=f"{en} está terminando de estudar {es};\nÀs {agora.strftime('%H:%M')} na data {agora.strftime('%d/%m/%Y')}", font=('Montserrat Thin Regular', 11, 'bold'), fg=cor2, bg=cor4)
        estudado.place(x=20, y=315)
    # criação do arquivo com o nome do que a pessoa colocou na variável es
    with open (nome_arquivo, "a", encoding="utf-8") as document:
        document.write(f"\n{en} {re} a estudar {es} às {agora.strftime('%H:%M')} na data {agora.strftime('%d/%m/%Y')}!\n")



# cores que foram usadas no código
cor1 = '#080707' # preta
cor2 = '#ffffff' # branca
cor3 = '#808080' # cinza médio 
cor4 = '#22dce6' # ciano
cor5 = '#000536' # azul escuro
cor6 = '#28a745' # verde
cor7 = '#dc3545' # vermelha
cor8 = '#1D7130' # verde escuro
cor9 = '#94242E' # vermelho escuro

# criação da tela
tela = Tk()
tamanho = tela.geometry('400x400') # tamanho da tela
titulo = tela.title('Bater Ponto')
tela.config(bg=cor4)
tela.resizable(width=False, height=False) # torna a tela não redimensionável 

# labels, entradas (entry), botões (normais e radio buttons) do programa
sejabemvindo = Label(tela, text='Seja Bem Vindo', font=('Montserrat Thin Regular', 15, 'bold'), fg=cor2, bg=cor4) 
sejabemvindo.place(x=128, y=10)

registro = Label(tela, text='Registro', font=('Montserrat Thin Regular', 15, 'bold'), fg=cor2, bg=cor4) 
registro.place(x=160, y=46)

nome = Label(tela, text='Nome:', font=('Montserrat Thin Regular', 15, 'bold'), fg=cor2, bg=cor4)
nome.place(x=20, y=90)

entrada_nome = Entry(tela, width=33, font=('Montserrat Thin Regular', 11), fg=cor1, bg=cor2)
entrada_nome.place(x=90, y=95)

estudou = Label(tela, text='Estudou:', font=('Montserrat Thin Regular', 15, 'bold'), fg=cor2, bg=cor4)
estudou.place(x=20, y=135)

estudou_nome = Entry(tela, width=33, font=('Montserrat Thin Regular', 11), fg=cor1, bg=cor2)
estudou_nome.place(x=115, y=140)


registrado = StringVar()

botao1 = Radiobutton(tela, width=9, height=1, text='Começando', value='começou', variable=registrado, indicatoron=1, relief=FLAT, font=('Montserrat Thin Regular', 13, 'bold'), fg=cor2, activeforeground=cor2, bg=cor6, activebackground=cor8) 
botao1.place(x=60, y=210)
botao2 = Radiobutton(tela, width=9, height=1, text='Finalizando', value='terminou', variable=registrado, indicatoron=1, relief=FLAT, font=('Montserrat Thin Regular', 13,'bold'), fg=cor2, activeforeground=cor2, bg=cor7, activebackground=cor9) 
botao2.place(x=263, y=210)

botao3 = Button(tela, width=9, height=1, text='coletar', relief=FLAT, font=('Montserrat Thin Regular', 13,'bold'), fg=cor2, command=pegarnomeestudo, activeforeground=cor2, bg=cor7, activebackground=cor9) 
botao3.place(x=163, y=270)

# coloca a tela em um loop constante
tela.mainloop()

# Consertar:
# algumas coisas aceitarem a função title() que nem no do terminal
# Fazer com que os arquivos criados vão para uma pasta especifica (talves usando  a biblioteca OS)