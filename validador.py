from modulos import *
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
