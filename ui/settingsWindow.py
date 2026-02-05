# Settings window for the MultiCopy application.

import tkinter as tk
from tkinter import ttk
from utils.config import config


class SettingsWindow:
    def __init__(self, on_start_callback):
        self.on_start = on_start_callback

        self.root = tk.Tk()
        self.root.title("MultiCopy")
        self.root.geometry("400x280")
        self.center_window(400, 280)
        self.root.resizable(False, False)

        # ------------------------
        # Título
        # ------------------------
        title = ttk.Label(
            self.root,
            text="MultiCopy",
            font=("Segoe UI", 14, "bold")
        )
        title.pack(pady=(15, 10))

        # ------------------------
        # Hotkey
        # ------------------------
        hotkey_frame = ttk.Frame(self.root)
        hotkey_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(hotkey_frame, text="Show overlay hotkey:").pack(anchor="w")

        self.hotkey_entry = ttk.Entry(hotkey_frame)
        self.hotkey_entry.insert(0, config.show_overlay_hotkey)
        self.hotkey_entry.pack(fill="x", pady=5)

        # ------------------------
        # Start Button
        # ------------------------
        start_button = ttk.Button(
            self.root,
            text="Start",
            command=self.start
        )
        start_button.pack(pady=15)

    def start(self):
        config.show_overlay_hotkey = self.hotkey_entry.get().strip()
        self.root.destroy()
        self.on_start()

    def run(self):
        self.root.mainloop()
    
    def center_window(self, width, height):
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()

        x = (screen_w // 2) - (width // 2)
        y = (screen_h // 2) - (height // 2)

        self.root.geometry(f"{width}x{height}+{x}+{y}")