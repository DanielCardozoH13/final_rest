from tkinter import *
import requests #modulo para realizar peticiones http
from tkinter import ttk
import tkinter.font as tkFont

"""consumo de API PokéAPI, 'https://pokeapi.co/api/v2/')
    con Python y presentación gráfica en tkinter
    autores: Daniel Cardozo, Cristian Chivata, Santiago Giraldo
"""
class PokeApi():
    def __init__(self):
        self.principal = Tk()
        self.principal.title("Consumo API")
        self.principal.geometry("400x220")
        self.principal.resizable(False, False)
        self.ventana_principal() #funcion que contiene parte de la interfaz gráfica
        self.principal.mainloop()


    def get_json(self,parametro):
        url = "https://pokeapi.co/api/v2/"+parametro #se hace la solicitud http por metodo get del modulo request
        self.response = requests.get(url)
        return self.response.json()

    def crear_tabla(self, arg): #función para crear ventana emergente con tabla y datos obtenidos por el metodo get
        ventana_table = Toplevel(self.principal)
        ventana_table.title("Listado")
        ventana_table.geometry("500x400")
        ventana_table.resizable(False,False)
        ventana_table.focus_get()
        ventana_table.grab_set()

        encabezados = (u"Id",   u"Nombre", u"Url")
        pokemon_table = Table(ventana_table, title="Consumo API: PokéAPI ('https://pokeapi.co/api/v2/')", headers=encabezados)
        pokemon_table.pack(fill=BOTH, expand=True)

        registros = self.get_json(arg)
        i=1
        for row in registros["results"]:
            fila_table = (str(i),str(row["name"]),str(row["url"]))
            pokemon_table.add_row(fila_table)
            i+=1


    def ventana_principal(self):
        color="#A9A9A9"
        fuente=('Consolas', 12, 'bold')
        self.marco_botones = Frame(self.principal)
        self.marco_botones.pack(fill=X, side=TOP, pady=20, padx=8, ipady=30,expand=True)
        label_listas = Label(self.marco_botones, font=fuente,
                                   text="Seleccione un botón para consumir la API", justify="center",  width=7).pack(fill=X, side=TOP, pady=15, padx=10)
        self.btn_pokemon = Button(self.marco_botones,text="Pokemon",font=fuente, bg=color, bd=2, command=lambda: self.crear_tabla("pokemon")).pack(fill=X, side="top",pady=1, padx=60)
        self.btn_tipos = Button(self.marco_botones,text="Tipos",font=fuente, bg=color, bd=2, command=lambda: self.crear_tabla("type")).pack(fill=X, side="top",pady=1, padx=60)
        self.btn_generacion = Button(self.marco_botones,text="Generaciones",font=fuente, bg=color, bd=2, command=lambda: self.crear_tabla("generation")).pack(fill=X, side="top",pady=1, padx=60)


class Table(Frame):
    def __init__(self, parent=None, title="", headers=[], height=10, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self._title = Label(self, text=title, background="#ECCCCE", font=("Helvetica", 16))
        self._headers = headers
        self._tree = ttk.Treeview(self,
                                  height=height,
                                  columns=self._headers,
                                  show="headings")
        self._title.pack(side=TOP, fill="x")

        # Agregamos dos scrollbars
        vsb = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)
        vsb.pack(side='right', fill='y')
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self._tree.xview)
        hsb.pack(side='bottom', fill='x')

        self._tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        self._tree.pack(side="top", expand=True, fill=BOTH)

        for header in self._headers:
            self._tree.heading(header, text=header.title())
            self._tree.column(header, stretch=True,
                              width=tkFont.Font().measure(header.title()))

    def add_row(self, row):
        self._tree.insert('', 'end', values=row)
        for i, item in enumerate(row):
            col_width = tkFont.Font().measure(item)
            if self._tree.column(self._headers[i], width=None) < col_width:
                    self._tree.column(self._headers[i], width=col_width)

def main():
    poke = PokeApi()

if __name__ == '__main__':
    main()