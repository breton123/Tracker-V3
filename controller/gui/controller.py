import wx
import wx.grid

class ControllerFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Controller Page', size=(600, 400),
                         style=wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER & ~wx.MAXIMIZE_BOX)
        panel = wx.Panel(self)

        # Set dark theme colors
        panel.SetBackgroundColour('#2E2E2E')
        text_color = '#FFFFFF'
        grid_bg_color = '#3C3F41'
        grid_fg_color = '#FFFFFF'
        grid_border_color = '#5A6268'

        # Create a Grid
        self.grid = wx.grid.Grid(panel)
        self.grid.CreateGrid(5, 3)  # 5 rows and 3 columns

        # Set column labels
        self.grid.SetColLabelValue(0, "Account")
        self.grid.SetColLabelValue(1, "Enabled")
        self.grid.SetColLabelValue(2, "Settings")

        # Apply dark theme to the grid
        self.grid.SetBackgroundColour(grid_bg_color)
        self.grid.SetGridLineColour(grid_border_color)
        self.grid.SetLabelBackgroundColour(grid_bg_color)
        self.grid.SetLabelTextColour(text_color)
        self.grid.SetDefaultCellBackgroundColour(grid_bg_color)
        self.grid.SetDefaultCellTextColour(text_color)

        # Sample data
        accounts = [
            ("Account1", True),
            ("Account2", False),
            ("Account3", True),
            ("Account4", True),
            ("Account5", False),
        ]

        # Fill grid with sample data
        for row, (account, enabled) in enumerate(accounts):
            self.grid.SetCellValue(row, 0, account)
            self.grid.SetCellValue(row, 1, "Yes" if enabled else "No")

        # Create and set cell renderer for the "Settings" column
        self.grid.SetCellRenderer(2,2, wx.grid.GridCellAutoWrapStringRenderer())

        # Create a sizer to arrange the components
        outer_sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(outer_sizer)

        # Inner sizer to center the grid
        grid_container = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(panel, label="Welcome to the Controller Page!")
        title_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title.SetFont(title_font)
        title.SetForegroundColour(text_color)
        grid_container.Add(title, 0, wx.ALL | wx.CENTER, 10)
        grid_container.Add(self.grid, 1, wx.EXPAND | wx.ALL, 10)

        outer_sizer.AddStretchSpacer(1)  # Stretchable empty space before the grid container
        outer_sizer.Add(grid_container, 0, wx.CENTER)
        outer_sizer.AddStretchSpacer(1)  # Stretchable empty space after the grid container

        self.Centre()  # Center the window on the screen
        self.Show()
