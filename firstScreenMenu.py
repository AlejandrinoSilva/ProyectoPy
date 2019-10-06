#!/usr/bin/python3
# -*- coding: utf-8 -*-
try:
    import wx
except ImportError:
    raise ImportError,"Se requiere el modulo wxPython"

class ventanaPrincipal(wx.Frame):
    def __init__(self, parent, title):
        super(ventanaPrincipal,self).__init__(parent,title=title, style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, size=(800, 600))
        # Centra la ventana
        self.Centre()
        # En caso que querramos insertar de forma manual la posicion usamos
        # self.SetPosition((x,y))
        self.InitUI()

    def InitUI(self):
        # Creamos la barra de Menu
        menubar = wx.MenuBar()
        # Creamos el Menu
        archivo = wx.Menu()
        archivo.Append(wx.ID_FILE, '&Archivo')
        archivo.Append(wx.ID_EDIT, '&Editar')
        archivo.Append(wx.ID_SAVE, '&Guardar')
        archivo.Append(wx.ID_HELP, '&Ayuda')
        archivo.AppendSeparator()

        edit = wx.Menu()
        edit.Append(wx.ID_ANY, "&XItem")
        edit.Append(wx.ID_ANY, "&YItem")
        edit.Append(wx.ID_ANY, "&ZItem")
        # Original archivo.AppendMenu(wx.ID_ANY, '&editar', edit)
        archivo.Append(wx.ID_ANY, '&editar', edit)

        opcion = wx.MenuItem(archivo, wx.ID_ANY, '&Quit')
        # Original archivo.AppendItem(opcion)
        archivo.Append(opcion)

        self.Bind(wx.EVT_MENU, self.OnQuit, opcion)
        menubar.Append(archivo, '&Archivo')
        self.SetMenuBar(menubar)


        # ========================
        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(3,2)

        self.texto = wx.StaticText(self.panel, label="Nombre:")
        self.sizer.Add(self.texto, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.textonuevo = wx.StaticText(self.panel, label="Me llamo: ")
        self.sizer.Add(self.textonuevo, pos=(1, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.textoedit = wx.TextCtrl(self.panel)
        self.sizer.Add(self.textoedit, pos=(0, 1), span=(1, 3), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

        self.boton = wx.Button(self.panel, label="Enviar", size=(90, 50))
        self.sizer.Add(self.boton, pos=(3,3), flag=wx.RIGHT | wx.BOTTOM)

        self.panel.Bind(wx.EVT_BUTTON, self.TomarTexto, self.boton)
        self.panel.SetSizerAndFit(self.sizer)

        self.Show(True)

    def TomarTexto(self, event):
        textomado = 'Hola Mundo'
        textomado = self.textoedit.GetValue()
        self.textonuevo.SetLabel(textomado)

    def OnQuit(self, e):
        self.Close()



if __name__=='__main__':
    app = wx.App()
    ventanaPrincipal(None,title='Bienvenido a RamSys S.A')
    app.MainLoop()
