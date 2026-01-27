# core/hotkeys.py

from pynput import keyboard
from core.clipboardManager import ClipboardManager
import threading
import time


class HotkeyManager:
    def __init__(self, on_show_overlay_callback=None):
        self.on_show_overlay = on_show_overlay_callback

        self.listener = keyboard.GlobalHotKeys({
            '<ctrl>+c': self._on_copy,
            '<ctrl>+<shift>+v': self._on_show_overlay
        })

    def _on_copy(self):
        # Ejecutar con pequeño delay en otro hilo
        threading.Thread(target=self._delayed_clipboard_read, daemon=True).start()

    def _delayed_clipboard_read(self):
        time.sleep(0.05)  # 50 ms (clave)
        text = ClipboardManager.read_clipboard()
        if text:
            ClipboardManager.add_text(text)

    def _on_show_overlay(self):
        if self.on_show_overlay:
            self.on_show_overlay()

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()
