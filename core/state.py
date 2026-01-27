# State management for the clipboard application

class AppState:
    def __init__(self):
        self.clipboard_items = [] # List to store clipboard items
        self.max_items = 20 # Maximum number of clipboard items to store
        self.overlay_visible = False # Overlay visibility flag
        self.selected_index = 0 # Currently selected clipboard item index

state = AppState()
