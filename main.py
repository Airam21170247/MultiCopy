# Main entry point for the MultiCopy application.

import time
from core.hotKeys import HotkeyManager
from core.clipboardManager import ClipboardManager


def show_overlay_mock():
    print("\n📋 Clipboard items:")
    for i, item in enumerate(ClipboardManager.get_all()):
        print(f"{i}: {item[:50]}")


hotkeys = HotkeyManager(on_show_overlay_callback=show_overlay_mock)
hotkeys.start()

print("Running... Copy text and press Ctrl+Shift+V")
while True:
    time.sleep(1)