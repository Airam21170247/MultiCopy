# Clipboard management for storing and retrieving clipboard items

import pyperclip
from core.state import state


class ClipboardManager:

    @staticmethod
    def read_clipboard(): # Read current clipboard content
        try:
            text = pyperclip.paste()
            if isinstance(text, str) and text.strip():
                return text
        except Exception:
            pass
        return None

    @staticmethod
    def add_text(text: str): # Add text to clipboard history
        if not text:
            return

        # Do not add duplicate of the most recent item
        if state.clipboard_items and state.clipboard_items[0] == text:
            return

        state.clipboard_items.insert(0, text)

        # Enforce maximum items limit
        if len(state.clipboard_items) > state.max_items:
            state.clipboard_items.pop()

    @staticmethod
    def get_all(): # Get all stored clipboard items
        return state.clipboard_items

    @staticmethod
    def remove(index: int): # Remove clipboard item at specified index
        if 0 <= index < len(state.clipboard_items):
            del state.clipboard_items[index]

    @staticmethod
    def clear(): # Clear all clipboard items
        state.clipboard_items.clear()

    @staticmethod
    def set_clipboard(text: str): # Set system clipboard to specified text
        pyperclip.copy(text)
