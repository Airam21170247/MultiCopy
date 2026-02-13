import json
import os

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.json")


def save_config(state, config):
    data = {
        "shortcut": config.show_overlay_hotkey,
        "max_items": state.max_items,
        "max_items_visible": state.max_items_visible,
        "clipboard_items": state.clipboard_items,
    }

    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_config(state, config):
    if not os.path.exists(CONFIG_FILE):
        return

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        config.show_overlay_hotkey = data.get("shortcut", config.show_overlay_hotkey)
        state.max_items = data.get("max_items", state.max_items)
        state.max_items_visible = data.get("max_items_visible", state.max_items_visible)

        state.clipboard_items.clear()
        state.clipboard_items.extend(data.get("clipboard_items", []))

    except Exception as e:
        print("Failed to load config:", e)