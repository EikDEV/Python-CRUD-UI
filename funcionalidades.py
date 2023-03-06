from modulos import *
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
            msg_sim_nao = messagebox.askyesno("Aviso", f'CRIAR o novo produto {nome}?')
            if msg_sim_nao == True:
                self.conecta_db()
                command = f'insert into tb_vendas (nome_produto, valor_produto, qtd_produto) values ("{nome}", "{valor}", "{qtd}");'
                self.cursor.execute(command)
                self.conn.commit()
                self.limpa_tela()
                self.busca_auto_db()
                self.desconecta_db()
                messagebox.showinfo("Aviso", "Produto CRIADO com sucesso!")
            else:
                msg = messagebox.showinfo("Aviso", "Operação cancelada!")
                self.limpa_tela()
    def atualiza_bd(self):
        id = self.id_entry.get()
        nome = self.nome_entry.get()
        valor = self.valor_entry.get()
        qtd = self.qtd_entry.get()
        if nome == "" or valor == "" or qtd == "" or id == "":
            msg = "Para ALTERAR um produto existente, é necessário preencher todos os campos corretamente."
            messagebox.showwarning("Aviso", msg)
        else:
            msg_sim_nao = messagebox.askyesno("Aviso", f'Deseja realmente ATUALIZAR o produto de ID {id} para {nome}, R${valor} e quantidade {qtd}?')
            if msg_sim_nao == True:
                self.conecta_db()
                command = f'update tb_vendas set nome_produto = "{nome}", valor_produto = "{valor}", qtd_produto = "{qtd}" where id_produto = "{id}";'
                self.cursor.execute(command)
                self.conn.commit()
                self.limpa_tela()
                self.busca_auto_db()
                self.desconecta_db()
                messagebox.showinfo("Aviso", "Produto ALTERADO com sucesso!")
            else:
                msg = messagebox.showinfo("Aviso", "Operação cancelada!")
                self.limpa_tela()
    def apaga_bd(self):
        id = self.id_entry.get()
        if id == "":
            msg = "Para APAGAR um produto existente, é necessário preencher o campo corretamente."
            messagebox.showwarning("Aviso", msg)
        else:
            msg_sim_nao = messagebox.askyesno("Aviso", f'Deseja realmente APAGAR o produto de ID {id}?')
            if msg_sim_nao == True:
                self.conecta_db()
                command = f'delete from tb_vendas where id_produto = {id};'
                self.cursor.execute(command)
                self.conn.commit()
                self.limpa_tela()
                self.busca_auto_db()
                self.desconecta_db()
                messagebox.showinfo("Aviso", "Produto APAGADO com sucesso!")
            else:
                msg = messagebox.showinfo("Aviso", "Operação cancelada!")
                self.limpa_tela()
    def duplo_click(self, event):
        self.limpa_tela()
        self.lista.selection()

        for n in self.lista.selection():
            col1, col2, col3, col4 = self.lista.item(n, 'values')
            self.id_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.valor_entry.insert(END, col3)
            self.qtd_entry.insert(END, col4)