# Clipboard management for storing and retrieving clipboard items

import pyperclip
from core.state import state


class ClipboardManager:

    @staticmethod
    def read_clipboard():
        try:
            text = pyperclip.paste()
            if isinstance(text, str) and text.strip():
                return text
        except Exception:
            pass
        return None

    @staticmethod
    def add_text(text: str):
        if not text:
            return

        if text in state.clipboard_items:
            state.clipboard_items.remove(text)

        state.clipboard_items.insert(0, text)

        if len(state.clipboard_items) > state.max_items:
            state.clipboard_items.pop()


    @staticmethod
    def get_all():
        return state.clipboard_items

    @staticmethod
    def remove(index: int):
        if 0 <= index < len(state.clipboard_items):
            del state.clipboard_items[index]

    @staticmethod
    def clear():
        state.clipboard_items.clear()

    @staticmethod
    def set_clipboard(text: str):
        pyperclip.copy(text)