from modulos import *
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