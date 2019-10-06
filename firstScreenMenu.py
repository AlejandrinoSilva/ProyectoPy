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
        archivo.Append(wx.ID_FILE, '&File')
        archivo.Append(wx.ID_EDIT, '&Edit')
        archivo.Append(wx.ID_SAVE, '&Save')
        archivo.Append(wx.ID_HELP, '&Help')
        archivo.AppendSeparator()

        edit = wx.Menu()
        edit.Append(wx.ID_ANY, "&XItem")
        edit.Append(wx.ID_ANY, "&YItem")
        edit.Append(wx.ID_ANY, "&ZItem")

        archivo.AppendMenu(wx.ID_ANY, 'E&ditar', edit)

        opcion = wx.MenuItem(archivo, wx.ID_ANY, '&Quit')
        archivo.AppendItem(opcion)

        self.Bind(wx.EVT_MENU, self.OnQuit, opcion)
        menubar.Append(archivo, '&Archivo')
        self.SetMenuBar(menubar)
        self.Show(True)

    def OnQuit(self, e):
        self.Close()



if __name__=='__main__':
    app = wx.App()
    ventanaPrincipal(None,title='Bienvenido a RamSys S.A')
    app.MainLoop()
