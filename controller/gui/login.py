import wx
import controller

class LoginFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Login Page', size=(400, 300),
                         style=wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER & ~wx.MAXIMIZE_BOX)
        panel = wx.Panel(self)

        # Set dark theme colors
        panel.SetBackgroundColour('#2E2E2E')
        text_color = '#FFFFFF'
        error_color = '#ff0033'
        input_bg_color = '#3C3F41'
        input_fg_color = '#FFFFFF'
        button_color = '#5A6268'
        button_fg_color = '#FFFFFF'

        # Outer sizer to vertically center the contents
        outer_sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(outer_sizer)

        # Inner sizer to hold the login form
        loginContainer = wx.BoxSizer(wx.VERTICAL)

        # Title text
        title = wx.StaticText(panel, label="Login Page")
        title_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title.SetFont(title_font)
        title.SetForegroundColour(text_color)
        loginContainer.Add(title, 0, wx.ALL | wx.CENTER, 10)

        # User ID input
        self.idInput = wx.TextCtrl(panel, style=wx.TE_CENTER, size=(0, -1))
        self.idInput.SetBackgroundColour(input_bg_color)
        self.idInput.SetForegroundColour(input_fg_color)
        loginContainer.Add(self.idInput, 0, wx.ALL | wx.CENTER, 5)

        # Password input
        self.passwordInput = wx.TextCtrl(panel, style=wx.TE_PASSWORD | wx.TE_CENTER, size=(0, -1))
        self.passwordInput.SetBackgroundColour(input_bg_color)
        self.passwordInput.SetForegroundColour(input_fg_color)
        loginContainer.Add(self.passwordInput, 0, wx.ALL | wx.CENTER, 5)

        # Login button
        loginButton = wx.Button(panel, label='Login')
        loginButton.SetBackgroundColour(button_color)
        loginButton.SetForegroundColour(button_fg_color)
        loginButton.Bind(wx.EVT_BUTTON, self.login)
        loginContainer.Add(loginButton, 0, wx.ALL | wx.CENTER, 10)

        # Error msg
        self.error = wx.StaticText(panel, label="")
        error_font = wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.error.SetFont(error_font)
        self.error.SetForegroundColour(error_color)
        loginContainer.Add(self.error, 0, wx.ALL | wx.CENTER, 10)

        # Adjust input widths to 1/3 of the current window width
        input_width = self.GetSize().GetWidth() // 3
        self.idInput.SetMinSize((input_width, -1))
        self.passwordInput.SetMinSize((input_width, -1))

        # Add the login container to the outer sizer and center it vertically
        outer_sizer.AddStretchSpacer(1)  # Stretchable empty space before the login form
        outer_sizer.Add(loginContainer, 0, wx.CENTER)
        outer_sizer.AddStretchSpacer(1)  # Stretchable empty space after the login form

        self.Centre()  # Center the window on the screen
        self.Show()

    def login(self, event):
        userID = self.idInput.GetValue()
        password = self.passwordInput.GetValue()
        if userID == "breton123" and password == "test":
            self.open_controller_frame()
        if userID == "" or password == "":
             self.error.SetLabel("")
        else:
            self.error.SetLabel("Invalid Credentials")
            #wx.MessageBox("Invalid credentials", "Error", wx.OK | wx.ICON_ERROR)

    def open_controller_frame(self):
        self.Hide()  # Hide the login frame
        controller_frame = controller.ControllerFrame()
        controller_frame.Show()
        self.Close()  # Close the login frame after opening the controller frame
