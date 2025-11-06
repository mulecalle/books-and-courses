from tkinter import *

class MiApp:

    def __init__(self, parent=None, **configs):

        # ################# #
        # Defino parametros #
        # ################# #
        ancho_boton = 10
        self.theme_background = "gray"

        # ############################ #
        # Defino variables por defecto #
        # ############################ #
        self.temas = StringVar()

        self.nombres = StringVar()
        self.nombres.set("VyH")

        self.side_option = StringVar()
        self.side_option.set(LEFT)

        self.fill_option = StringVar()
        self.fill_option.set(NONE)

        self.expand_option = StringVar()
        self.expand_option.set(YES)

        self.anchor_option = StringVar()
        self.anchor_option.set(N)


        # ################# #
        # Ventana principal #
        # ################# #
        self.myParent = parent
        self.myParent.geometry("700x600")


        # ################# #
        # Agrego contenedor #
        # ################# #
        self.Contenedor = Frame(self.myParent, bg="#444")
        self.Contenedor.pack(expand=YES, fill=BOTH)


        # ############################ #
        # Agrego Secciones Principales #
        # ############################ #
        #####  CERRAR #####
        self.seccion_cerrar = Frame(self.Contenedor, height=22, borderwidth=2, relief=RAISED)
        self.seccion_cerrar.pack(side=TOP, expand=NO, fill=X)
        self.cerrar = Frame(self.seccion_cerrar, height=22)
        self.cerrar.pack(side=TOP, expand=YES, fill=X)

        #####  SECCION CONTROLES #####
        self.seccion_controles = Frame(self.Contenedor, borderwidth=2, relief=RAISED)
        self.seccion_controles.pack(side=TOP, expand=NO, fill=BOTH)
        Label(self.seccion_controles, text="Controles", bg="black", fg="OrangeRed", justify=LEFT).pack(side=TOP, expand=NO, fill=X, anchor=W)
        self.controles = Frame(self.seccion_controles, bg=self.theme_background)
        self.controles.pack(side=TOP, expand=NO, fill=X)

        #####  SECCION REPRESENTACION #####
        self.seccion_representacion = Frame(self.Contenedor, borderwidth=2, relief=RAISED)
        self.seccion_representacion.pack(side=BOTTOM, expand=YES, fill=BOTH)
        Label(self.seccion_representacion, text="Representación gráfica", bg="black", fg="OrangeRed", justify=LEFT).pack(side=TOP, expand=NO, fill=X, anchor=W)
        self.representacion = Frame(self.seccion_representacion, bg="black")
        self.representacion.pack(side=TOP, expand=YES, fill=BOTH)


        # ######### #
        # Controles #
        # ######### #
        self.temas_opciones = Frame(self.controles, borderwidth=1, bg="black")
        self.nombres_opciones = Frame(self.controles, borderwidth=1, bg="black")
        self.side_contenedor = Frame(self.controles, borderwidth=1, bg="black")
        self.fill_contenedor = Frame(self.controles, borderwidth=1, bg="black")
        self.expand_contenedor = Frame(self.controles, borderwidth=1, bg="black")
        self.anchor_contenedor = Frame(self.controles, borderwidth=1, bg="black")

        self.temas_opciones.pack(side=LEFT, expand=NO, anchor=N)
        self.nombres_opciones.pack(side=LEFT, expand=YES, anchor=N)
        self.side_contenedor.pack(side=LEFT, expand=YES, anchor=N)
        self.fill_contenedor.pack(side=LEFT, expand=YES, anchor=N)
        self.expand_contenedor.pack(side=LEFT, expand=YES, anchor=N)
        self.anchor_contenedor.pack(side=LEFT, expand=NO, anchor=N)

        Label(self.temas_opciones, borderwidth=4, relief=RAISED, text="Temas", bg="black", fg="OrangeRed").pack(fill=X)
        Label(self.nombres_opciones, borderwidth=4, relief=RAISED, text="Opciones", bg="black", fg="OrangeRed").pack(fill=X)
        Label(self.side_contenedor, borderwidth=4, relief=RAISED, text="Side", bg="black", fg="OrangeRed").pack(fill=X)
        Label(self.fill_contenedor, borderwidth=4, relief=RAISED, text="Fill", bg="black", fg="OrangeRed").pack(fill=X)
        Label(self.expand_contenedor, borderwidth=4, relief=RAISED, text="Expand", bg="black", fg="OrangeRed").pack(fill=X)
        Label(self.anchor_contenedor, borderwidth=4, relief=RAISED, text="Anchor", bg="black", fg="OrangeRed").pack(fill=X)

        # ############## #
        # Representacion #
        # ############## #
        self.representacion_superior = Frame(self.representacion)
        self.representacion_superior.pack(side=TOP, expand=YES, fill=BOTH)

        self.deslizador_central = Frame(self.representacion_superior, bg=self.theme_background, borderwidth=4, relief=SUNKEN, width=250)
        self.deslizador_central.pack(side=LEFT, expand=YES, fill=BOTH)

        self.deslizador_vertical = Frame(self.representacion_superior, bg=self.theme_background, borderwidth=4, relief=SUNKEN, width=50)
        self.deslizador_vertical.pack(side=RIGHT, expand=NO, fill=Y)

        self.deslizador_horizontal = Frame(self.representacion, bg=self.theme_background, borderwidth=4, relief=SUNKEN, height=50)
        self.deslizador_horizontal.pack(side=TOP, fill=X)


        # ############################## #
        # Texto de botones parte grafica #
        # ############################## #
        self.botonVyH = Button(self.deslizador_central, text="VyH")
        self.botonVyH.pack()
        self.botonV = Button(self.deslizador_vertical, text="V")
        self.botonV.pack()
        self.botonH = Button(self.deslizador_horizontal, text="H")
        self.botonH.pack()
        self.elegir_nombre_botones = {"VyH": self.botonVyH, "V": self.botonV, "H": self.botonH}

        # #################### #
        # Nombres en controles #
        # #################### #
        temas = ["gray", "black", "white"]
        nombres = ["VyH", "V", "H"]
        side_options = [LEFT, TOP, RIGHT, BOTTOM]
        fill_options = [X, Y, BOTH, NONE]
        expand_options = [YES, NO]
        anchor_options = [NW, N, NE, E, SE, S, SW, W, CENTER]

        # ##################### #
        # Opciones de controles #
        # ##################### #
        for opcion in temas:
            boton1 = Radiobutton(self.temas_opciones, text=str(opcion), indicatoron=0, value=opcion, command=self.changeTheme, variable=self.temas)
            boton1["width"] = ancho_boton
            boton1.pack(side=TOP)

        for opcion in nombres:
            boton = Radiobutton(self.nombres_opciones, text=str(opcion), indicatoron=0, value=opcion, command=self.reseteo, variable=self.nombres)
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        for opcion in side_options:
            boton = Radiobutton(self.side_contenedor, text=str(opcion), indicatoron=0, value=opcion, command=self.actualizar, variable=self.side_option)
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        for opcion in fill_options:
            boton = Radiobutton(self.fill_contenedor, text=str(opcion), indicatoron=0, value=opcion, command=self.actualizar, variable=self.fill_option)
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        for opcion in expand_options:
            boton = Radiobutton(self.expand_contenedor, text=str(opcion), indicatoron=0, value=opcion, command=self.actualizar, variable=self.expand_option)
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        for opcion in anchor_options:
            boton = Radiobutton(self.anchor_contenedor, text=str(opcion), indicatoron=0, value=opcion, command=self.actualizar, variable=self.anchor_option)
            boton["width"] = ancho_boton
            boton.pack(side=TOP)


        # ################# #
        # Boton de cancelar #
        # ################# #
        self.cancelar = Button(self.cerrar, text="Cancel", background="black", fg="OrangeRed")
        self.cancelar.pack(side=BOTTOM, anchor=S, expand=YES, fill=BOTH)
        self.cancelar.bind("<Button-1>", self.cerrarApp)

    # ######## #
    # Destruir #
    # ######## #
    def cerrarApp(self, event):
        self.myParent.destroy()

    def changeTheme(self):
        self.theme_background = self.temas.get()
        self.deslizador_central.config(bg = self.theme_background)
        self.deslizador_vertical.config(bg=self.theme_background)
        self.deslizador_horizontal.config(bg=self.theme_background)
        self.controles.config(bg=self.theme_background)


    # ######################### #
    # Defino funcion de reseteo #
    # ######################### #
    def reseteo(self):
        button = self.elegir_nombre_botones[self.nombres.get()]
        properties = button.pack_info()
        self.fill_option.set(properties["fill"])
        self.side_option.set(properties["side"])
        self.expand_option.set(properties["expand"])
        self.anchor_option.set(properties["anchor"])

    # ######################### #
    # Defino funcion actualizar #
    # ######################### #
    def actualizar(self):
        button = self.elegir_nombre_botones[self.nombres.get()]
        button.pack(fill= self.fill_option.get(), side= self.side_option.get(), expand= self.expand_option.get(), anchor= self.anchor_option.get())


if __name__ == '__main__':
    root = Tk()
    MiApp(root)
    root.mainloop()