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
        # ========================
        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(3,2)
        # Name label
        self.textonombre = wx.StaticText(self.panel, label="Nombre:")
        self.sizer.Add(self.textonombre, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        # Clave label
        self.textoclave = wx.StaticText(self.panel, label="Clave:")
        self.sizer.Add(self.textoclave, pos=(1, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        # Check pass login state
        self.textoestado = wx.StaticText(self.panel, label="Estado: ")
        self.sizer.Add(self.textoestado, pos=(2, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        # Texto Nombre
        self.textoname = wx.TextCtrl(self.panel)
        self.sizer.Add(self.textoname, pos=(0, 1), span=(1, 3), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)
        # Texto Password
        self.textopass = wx.TextCtrl(self.panel)
        self.sizer.Add(self.textopass, pos=(1, 1), span=(1, 3), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)
        # Boton de Verificacion
        self.boton = wx.Button(self.panel, label="Log In", size=(50, 25))
        self.sizer.Add(self.boton, pos=(3,3), flag=wx.RIGHT | wx.BOTTOM)

        self.panel.Bind(wx.EVT_BUTTON, self.Validar, self.boton)
        self.panel.SetSizerAndFit(self.sizer)

        self.Show(True)

    def Validar(self, event):
        usuario = self.textoname.GetValue()
        password = self.textopass.GetValue()
        if (usuario == "Alejandrino" and password == "RamonSilva"):
            self.textoestado.SetLabel("Bienvenido puede ingresar")
            nv = NuevaVentana(None)
            nv.Show()
        else:
            self.textoestado.SetLabel("Ingreso Incorrecto")

class NuevaVentana(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        panel = wx.Panel(self, -1)
        txt = wx.StaticText(panel, label="Entramos!!!")
        self.Centre()



if __name__=='__main__':
    app = wx.App()
    ventanaPrincipal(None,title='Bienvenido a RamSys S.A')
    app.MainLoop()
