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
        fileMenu = wx.Menu()
        # Creamos los items del Menu
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Salir', 'Salir de la App')
        menubar.Append(fileM
        enu, '&Archivo')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)
        self.Show(True)

    def OnQuit(self, e):
        self.Close()



if __name__=='__main__':
    app = wx.App()
    ventanaPrincipal(None,title='Bienvenido a RamSys S.A')
    app.MainLoop()
