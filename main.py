from ui.settingsWindow import SettingsWindow
from ui.overlay import ClipboardOverlay
from core.hotKeys import HotkeyManager

hotkeys = None
overlay = None


def open_settings():
    settings = SettingsWindow(on_start_callback=start_app)
    settings.run()


def start_app():
    global hotkeys, overlay

    overlay = ClipboardOverlay(
        on_open_settings=open_settings,
        on_stop_listener=stop_hotkeys
    )

    hotkeys = HotkeyManager(
        on_show_overlay_callback=overlay.show_thread_safe
    )
    hotkeys.start()

    overlay.root.mainloop()


def stop_hotkeys():
    global hotkeys
    if hotkeys:
        hotkeys.stop()
        hotkeys = None


if __name__ == "__main__":
    open_settings()
