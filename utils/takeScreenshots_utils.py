import pyautogui
from pathlib import Path

def take_fullscreen_screenshot():
    screenshot = pyautogui.screenshot()
    dir_path=Path.cwd()
    screenshots_dir = dir_path / "screenshots"
    screenshot_path = screenshots_dir / "full_screen.png"
    screenshot.save(screenshot_path)
    print("Screenshot saved as full_screen.png")
    return screenshot_path
