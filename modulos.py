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