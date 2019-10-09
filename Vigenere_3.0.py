import tkinter 
import VigenereLib

def crypto_tk(mens, senha):
    label_result['text'] = VigenereLib.crypto(mens, senha)

def decrypto_tk(mens, senha):
    label_result['text'] = VigenereLib.decrypto(mens, senha)

root = tkinter.Tk()

canvas = tkinter.Canvas(root, height=500, width=600)
canvas.pack()

imagem_de_fundo = tkinter.PhotoImage(file='cript.png')
background = tkinter.Label(root,image=imagem_de_fundo)
background.place(relheight=1, relwidth=1)

frame_mens = tkinter.Frame(root, bg='black', bd=5)
frame_mens.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

label_mens = tkinter.Label(frame_mens, text='Mensagem:',bg='light gray')
label_mens.place(relwidth=0.24, relheigh=1)

entrada_mens = tkinter.Entry(frame_mens)
entrada_mens.place(relx=0.25,relwidth=0.75, relheight=1)

frame_snh = tkinter.Frame(root, bg='black', bd=5)
frame_snh.place(relx=0.5, rely=0.22, relwidth=0.75, relheight=0.1, anchor='n')

label_snh = tkinter.Label(frame_snh, text='Senha:', bg='light gray')
label_snh.place(relwidth=0.24, relheigh=1)

entrada_snh = tkinter.Entry(frame_snh)
entrada_snh.place(relx=0.25,relwidth=0.75, relheight=1)

frame_botao = tkinter.Frame(root, bg='black', bd=5)
frame_botao.place(relx=0.5, rely=0.34, relwidth=0.75, relheight=0.1, anchor='n')

botao_crypt = tkinter.Button(frame_botao, bg='light gray', text='criptografar', command=lambda: crypto_tk(entrada_mens.get().upper(), entrada_snh.get().upper()))
botao_crypt.place(relx=0.05,relheight=1, relwidth=0.4)

botao_decrypt = tkinter.Button(frame_botao, bg='light gray', text='decifrar', command=lambda: decrypto_tk(entrada_mens.get().upper(), entrada_snh.get().upper()))
botao_decrypt.place(relx=0.56,relheight=1, relwidth=0.4)

lower_frame = tkinter.Frame(root, bg='black', bd=5)
lower_frame.place(relx=0.5, rely=0.46, relheight=0.5, relwidth=0.75, anchor='n')

label_result = tkinter.Label(lower_frame,text='')
label_result.place(relwidth=1, relheight=1)

root.mainloop()
