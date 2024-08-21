import wx
import login



if __name__ == '__main__':
    app = wx.App()
    login_frame = login.LoginFrame()
    app.MainLoop()
