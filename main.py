# Test Main

from ui.settingsWindow import SettingsWindow
from ui.overlay import ClipboardOverlay
from core.hotKeys import HotkeyManager

overlay = ClipboardOverlay()
hotkeys = None


def start_app():
    global hotkeys
    hotkeys = HotkeyManager(
        on_show_overlay_callback=overlay.show_thread_safe
    )
    hotkeys.start()
    overlay.root.mainloop()


if __name__ == "__main__":
    settings = SettingsWindow(on_start_callback=start_app)
    settings.run()
