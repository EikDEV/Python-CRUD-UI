# Importar interface gráfica
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# Importar gerador de PDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
# Importar browser padrão
import webbrowser
# Importar conector mysql
import mysql.connector

root = Tk()
class Relatorios():
    def print_produtos(self):
        webbrowser.open("C:/Users/Eik/Desktop/produto.pdf")
    def gerar_relatorio_produto(self):
        self.c = canvas.Canvas("C:/Users/Eik/Desktop/produto.pdf")

        self.id_rel = self.id_entry.get()
        self.nome_rel = self.nome_entry.get()
        self.valor_rel = self.valor_entry.get()
        self.qtd_rel = self.qtd_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do Produto')

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, 'Código: ')
        self.c.drawString(50, 670, 'Nome: ')
        self.c.drawString(50, 640, 'Valor: ')
        self.c.drawString(50, 610, 'Quantidade: ')

        self.c.setFont("Helvetica", 18)
        self.c.drawString(125, 700, self.id_rel)
        self.c.drawString(110, 670, self.nome_rel)
        self.c.drawString(110, 640, 'R$' +self.valor_rel)
        self.c.drawString(160, 610, self.qtd_rel)

        self.c.rect(20, 590, 550,  5, fill=True, stroke=False)

        self.c.showPage()
        self.c.save()
        self.print_produtos()

class Validadores:
    def validar_entry3(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 < value < 1000
    def validar_entry4(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 < value < 10000
    def validar_entry5(self, text):
        if text == "": return True
        try:
            value = float(text)
        except ValueError:
            return False
        return 0 < value < 100000
class Funcs():
    def limpa_tela(self):
        self.id_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.qtd_entry.delete(0, END)
    def conecta_db(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='pythoncrud'
        )
        self.cursor = self.conn.cursor()
    def desconecta_db(self):
        self.conn.close()
    def busca_db(self):
        self.lista.delete(*self.lista.get_children())
        nome = self.nome_entry.get()
        self.conecta_db()
        command = f'select id_produto, nome_produto, valor_produto, qtd_produto from tb_vendas where nome_produto like "%{nome}%";'
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        for i in result:
            self.lista.insert("", END, values=i)
        self.desconecta_db()
    def busca_auto_db(self):
        self.lista.delete(*self.lista.get_children())
        self.conecta_db()
        command_list = f'select id_produto, nome_produto, valor_produto, qtd_produto from tb_vendas order by nome_produto asc;'
        self.cursor.execute(command_list)
        result = self.cursor.fetchall()
        for i in result:
            self.lista.insert("", END, values=i)
        self.desconecta_db()
        self.limpa_tela()
    def insere_db(self):
        nome = self.nome_entry.get()
        valor = self.valor_entry.get()
        qtd = self.qtd_entry.get()
        if nome == "" or valor == "" or qtd == "":
            msg = "Para CADASTRAR um novo produto, é necessário preencher todos os campos corretamente."
            messagebox.showinfo("Aviso", msg)
        else:
            self.conecta_db()
            command = f'insert into tb_vendas (nome_produto, valor_produto, qtd_produto) values ("{nome}", "{valor}", "{qtd}");'
            self.cursor.execute(command)
            self.conn.commit()
            self.limpa_tela()
            self.busca_auto_db()
            self.desconecta_db()
    def atualiza_bd(self):
        id = self.id_entry.get()
        nome = self.nome_entry.get()
        valor = self.valor_entry.get()
        qtd = self.qtd_entry.get()
        if nome == "" or valor == "" or qtd == "" or id == "":
            msg = "Para ALTERAR um produto existente, é necessário preencher todos os campos corretamente."
            messagebox.showwarning("Aviso", msg)
        else:
            self.conecta_db()
            command = f'update tb_vendas set nome_produto = "{nome}", valor_produto = "{valor}", qtd_produto = "{qtd}" where id_produto = "{id}";'
            self.cursor.execute(command)
            self.conn.commit()
            self.limpa_tela()
            self.busca_auto_db()
            self.desconecta_db()
    def apaga_bd(self):
        id = self.id_entry.get()
        if id == "":
            msg = "Para APAGAR um produto existente, é necessário preencher o campo corretamente."
            messagebox.showwarning("Aviso", msg)
        else:
            self.conecta_db()
            command = f'delete from tb_vendas where id_produto = {id};'
            self.cursor.execute(command)
            self.conn.commit()
            self.limpa_tela()
            self.busca_auto_db()
            self.desconecta_db()
    def duplo_click(self, event):
        self.limpa_tela()
        self.lista.selection()

        for n in self.lista.selection():
            col1, col2, col3, col4 = self.lista.item(n, 'values')
            self.id_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.valor_entry.insert(END, col3)
            self.qtd_entry.insert(END, col4)
class Application(Funcs, Validadores, Relatorios):
    def __init__(self):
        self.root = root
        self.validar_entradas()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.busca_auto_db()
        self.menus()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de produtos")
        self.root.configure(background='#233466')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(1920, 1080)
        self.root.minsize(700, 500)
    def frames_da_tela(self):
        # Frame1 da tela (div)
        self.frame_1 = Frame(self.root, bd=4, bg='#fff', highlightbackground='#000', highlightthickness=1)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        # Frame2 da tela (div)
        self.frame_2 = Frame(self.root, bd=4, bg='#fff', highlightbackground='#000', highlightthickness=1)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def widgets_frame1(self):
        # Botão limpar
        self.btn_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#39b3e0', fg='#fff', font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.btn_limpar.place(relx=0.19, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão buscar
        self.btn_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#39b3e0', fg='#fff', font=('verdana', 8, 'bold'), command=self.busca_db)
        self.btn_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão novo
        self.btn_novo = Button(self.frame_1, text='Novo', bd=2, bg='#39b3e0', fg='#fff', font=('verdana', 8, 'bold'), command=self.insere_db)
        self.btn_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão alterar
        self.btn_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#39b3e0', fg='#fff', font=('verdana', 8, 'bold'), command=self.atualiza_bd)
        self.btn_alterar.place(relx=0.71, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão apagar
        self.btn_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#39b3e0', fg='#fff', font=('verdana', 8, 'bold'), command=self.apaga_bd)
        self.btn_apagar.place(relx=0.82, rely=0.1, relwidth=0.1, relheight=0.15)

        # Label Código / Entry Código (input)
        self.lb_id = Label(self.frame_1, text='Código', bg='#fff')
        self.lb_id.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.1)

        self.id_entry = Entry(self.frame_1, bd=2, validate="key", validatecommand=self.vcmd3)
        self.id_entry.place(relx=0.06, rely=0.16, relwidth=0.08, relheight=0.1)

        # Label Nome / Entry Nome (input)
        self.lb_nome = Label(self.frame_1, text='Nome', bg='#fff')
        self.lb_nome.place(relx=0.05, rely=0.3, relwidth=0.1, relheight=0.1)

        self.nome_entry = Entry(self.frame_1, bd=2)
        self.nome_entry.place(relx=0.06, rely=0.4, relwidth=0.34, relheight=0.1)

        # Label Valor / Entry Valor (input)
        self.lb_valor = Label(self.frame_1, text='Valor', bg='#fff')
        self.lb_valor.place(relx=0.05, rely=0.5, relwidth=0.1, relheight=0.1)

        self.lb_real = Label(self.frame_1, text='R$', bg='#fff')
        self.lb_real.place(relx=0.0001, rely=0.6, relwidth=0.1, relheight=0.1)

        self.valor_entry = Entry(self.frame_1, bd=2, validate="key", validatecommand=self.vcmd5)
        self.valor_entry.place(relx=0.06, rely=0.6, relwidth=0.2, relheight=0.1)

        # Label Quantidade / Entry Quantidade (input)
        self.lb_qtd = Label(self.frame_1, text='Quantidade', bg='#fff')
        self.lb_qtd.place(relx=0.6, rely=0.3, relwidth=0.1, relheight=0.1)

        self.qtd_entry = Entry(self.frame_1, bd=2, validate="key", validatecommand=self.vcmd4)
        self.qtd_entry.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.1)
    def lista_frame2(self):
        self.lista = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3", "col4",))
        self.lista.heading("#0", text="")
        self.lista.heading("#1", text="Código")
        self.lista.heading("#2", text="Nome")
        self.lista.heading("#3", text="Valor")
        self.lista.heading("#4", text="Quantidade")

        self.lista.column("#0", width=1)
        self.lista.column("#1", width=50)
        self.lista.column("#2", width=200)
        self.lista.column("#3", width=125)
        self.lista.column("#4", width=50)

        self.lista.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        self.lista.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.lista.bind("<Double-1>", self.duplo_click)
    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu1 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Relatórios", menu=filemenu1)

        filemenu.add_command(label="Sair", command=Quit)
        filemenu.add_command(label="Limpar tela", command=self.limpa_tela)

        filemenu1.add_command(label="Ficha do produto", command=self.gerar_relatorio_produto)
    def validar_entradas(self):
        self.vcmd3 = (self.root.register(self.validar_entry3), "%P")
        self.vcmd4 = (self.root.register(self.validar_entry4), "%P")
        self.vcmd5 = (self.root.register(self.validar_entry5), "%P")


Application()

