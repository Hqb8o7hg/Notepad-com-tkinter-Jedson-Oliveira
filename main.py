import tkinter


def novo_arquivo():
    escreve_texto.delete(1.0, 'end')

def salvar():
    container = escreve_texto.get(1.0, "end")
    with open('teste.py', 'w') as arquivo:
        arquivo.write(container)


def abrir_documento():

    with open('teste.py', 'r') as arquivo:
        mostra = arquivo.read()
        escreve_texto.insert(1.0, mostra)

def atualiza_fonte():
    tamanho_fon = spin_size.get()
    fonte = limite_fonte.get()
    escreve_texto.config(font="{} {}".format(fonte, tamanho_fon))


tela = tkinter.Tk()  # Cria a tela
tela.title('Notepad')  # Renomeia a tela
tela.geometry("1280x720")
# Formata um texto e permite que escrevamos na tela
escreve_texto = tkinter.Text(tela, font="Arial 20 bold", width=1280, height=720)

frame = tkinter.Frame(tela, height=30)  # Cria a barra na parte superior da tela
frame.pack(fill="x")

fonte_texto = tkinter.Label(frame, text=" Font: ")
fonte_texto.pack(side="left")

limite_fonte = tkinter.Spinbox(frame, values=("Arial", "Verdana"))
limite_fonte.pack(side="left")

tamanho_fonte = tkinter.Label(frame, text=" Font size: ")
tamanho_fonte.pack(side="left")

spin_size = tkinter.Spinbox(
    frame,
    from_=0,
    to=60)
spin_size.pack(side="left")

botao_atualizar = tkinter.Button(frame, text="UP", command=atualiza_fonte)
botao_atualizar.pack(side="left")

escreve_texto.pack()  # escreve na tela o texto
main_menu = tkinter.Menu(tela)  # Cria o menu

Arquivo_menu = tkinter.Menu(main_menu, tearoff=0)  # Cria um novo menu
Arquivo_menu.add_command(label='New', command=novo_arquivo)  # Renomeia o novo menu
Arquivo_menu.add_command(label="Save", command=salvar)
Arquivo_menu.add_command(label="Open..", command=abrir_documento)
Arquivo_menu.add_command(label="Exit", command=tela.quit)

main_menu.add_cascade(label="Arquivo", menu=Arquivo_menu)  # Formata o menu
tela.config(menu=main_menu)  # Define o menu

tela.mainloop()  # Loop especifico da biblioteca
