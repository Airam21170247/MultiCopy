# Mouse utilities using pynput to get mouse position.

from pynput.mouse import Controller

_mouse = Controller()

def get_mouse_position(): # Get the current mouse position
    return _mouse.position
