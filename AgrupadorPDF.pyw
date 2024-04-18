from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.filedialog import askopenfilenames
from PyPDF2 import PdfMerger
from PIL import Image, ImageTk
import os

def mesclarPdf(arquivos, caminhoDestino, nomeArquivo):
    with PdfMerger() as pdf_agrupado:
        for pdf in arquivos:
            pdf_agrupado.append(pdf)
        pdf_agrupado.write(os.path.join(caminhoDestino, nomeArquivo))

def BuscarArquivos():
    arquivos = askopenfilenames(filetypes=[('Arquivos em PDF', '*.pdf')])

    if arquivos:
        try:   
            nomeArquivo = filedialog.asksaveasfilename(title='Nome do arquivo PDF agrupado', defaultextension='.pdf', filetypes=[('Arquivos PDF', '*.pdf')])
            if nomeArquivo:
                mesclarPdf(arquivos, os.path.dirname(nomeArquivo), nomeArquivo)
                messagebox.showinfo(title='Agrupador de PDFs', message='Arquivos agrupados com sucesso!')
        except PermissionError:
            messagebox.showerror(title='Erro', message='Permissão negada para salvar o arquivo.')
        except Exception as e:
            messagebox.showerror(title='Erro', message=f'Ocorreu um erro ao mesclar os PDFs: {e}')

janela = Tk()
caminhoExe = os.path.dirname(os.path.realpath(__file__))
imagemDeFundo = Image.open(f'{caminhoExe}\\images\\logo_fapec.png').resize((170,60))
imagemDeFundo = ImageTk.PhotoImage(imagemDeFundo)

janela.geometry('380x220')
janela.title('Agrupador de arquivos PDF')
janela.iconbitmap(f'{caminhoExe}\\images\\agrupadorPDF.ico')
janela['bg'] = '#000040'
janela.resizable(False, False)
divisoria1 = Frame(janela, width = 380, height = 65, bg = 'white')
divisoria1.grid(row = 0, column = 0)
divisoria2 = Frame(janela, width = 380, height = 140, borderwidth = 2, relief = 'raised', bg = 'white')
divisoria2.grid(row = 1, column = 0,pady = 25)

icone = Label(divisoria1, image = imagemDeFundo, bg = 'white' ).place(x = 0,y = 0)
saudacao = Label(divisoria2, text = 'Agrupador de arquivos PDFs', font = ('Verdana', '12', 'bold'), bg = 'white').grid(row=0, column=0, padx = 5, pady = 5)
botao = Button(divisoria2, text = 'Buscar arquivos', command = BuscarArquivos, font = ('Verdana', '12', 'bold'), fg = 'white', bg = '#CD5B45').grid(row=1, column=0, padx = 5, pady = 5)

janela.mainloop()