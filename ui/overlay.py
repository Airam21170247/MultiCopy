# Overlay UI for displaying clipboard history and allowing selection.

import tkinter as tk
from core.clipboardManager import ClipboardManager
from core.state import state
from utils.mouse import get_mouse_position
from pynput.keyboard import Controller, Key

keyboard_controller = Controller() # Initialize keyboard controller

class ClipboardOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # hidden by default

        self.root.overrideredirect(True)  # no window decorations
        self.root.attributes("-topmost", True)

        self.root.configure(bg="white")

        self.frame = tk.Frame(self.root, bg="white", bd=1, relief="solid")
        self.frame.pack(fill="both", expand=True)

        self.items_widgets = []

        self.root.bind("<Escape>", lambda e: self.hide())
        self.root.bind("<Up>", self.select_up)
        self.root.bind("<Down>", self.select_down)
        self.root.bind("<Return>", self.paste_selected)

    # -----------------------------
    # SHOW / HIDE
    # -----------------------------
    def show(self):
        self.refresh_items()
        self.position_near_mouse()
        self.root.deiconify()
        self.root.focus_force()
        state.overlay_visible = True

    def hide(self):
        self.root.withdraw()
        state.overlay_visible = False

    # -----------------------------
    # POSITION
    # -----------------------------
    def position_near_mouse(self):
        x, y = get_mouse_position()
        self.root.geometry(f"+{x + 15}+{y + 15}")

    # -----------------------------
    # ITEMS
    # -----------------------------
    def refresh_items(self):
        for w in self.items_widgets:
            w.destroy()
        self.items_widgets.clear()

        items = ClipboardManager.get_all()

        if not items:
            label = tk.Label(
                self.frame,
                text="Clipboard vacío",
                bg="white",
                fg="gray",
                padx=10,
                pady=10
            )
            label.pack(fill="x")
            self.items_widgets.append(label)
            return

        for index, text in enumerate(items):
            preview = text.replace("\n", " ")[:60]

            label = tk.Label(
                self.frame,
                text=preview,
                anchor="w",
                bg="white",
                fg="black",
                padx=10,
                pady=6
            )
            label.pack(fill="x")
            label.bind("<Button-1>", lambda e, i=index: self.select_index(i))
            label.bind("<Double-Button-1>", lambda e, i=index: self.paste_index(i))

            self.items_widgets.append(label)

        state.selected_index = 0
        self.update_selection()

    # -----------------------------
    # SELECTION
    # -----------------------------
    def update_selection(self):
        for i, widget in enumerate(self.items_widgets):
            if i == state.selected_index:
                widget.configure(bg="#111", fg="white")
            else:
                widget.configure(bg="white", fg="black")

    def select_up(self, event=None):
        if state.selected_index > 0:
            state.selected_index -= 1
            self.update_selection()

    def select_down(self, event=None):
        if state.selected_index < len(self.items_widgets) - 1:
            state.selected_index += 1
            self.update_selection()

    def select_index(self, index):
        state.selected_index = index
        self.update_selection()

    # -----------------------------
    # PASTE
    # -----------------------------
    def paste_selected(self, event=None):
        self.paste_index(state.selected_index)

    def paste_index(self, index):
        items = ClipboardManager.get_all()
        if 0 <= index < len(items):
            ClipboardManager.set_clipboard(items[index])

            # Esperar un poco antes de pegar
            self.root.after(50, self.simulate_ctrl_v)

        self.hide()

    
    def simulate_ctrl_v(self):
        keyboard_controller.press(Key.ctrl)
        keyboard_controller.press('v')
        keyboard_controller.release('v')
        keyboard_controller.release(Key.ctrl)

        
    # -----------------------------
    # THREAD-SAFE SHOW
    # -----------------------------
    def show_thread_safe(self):
        self.root.after(0, self.show)