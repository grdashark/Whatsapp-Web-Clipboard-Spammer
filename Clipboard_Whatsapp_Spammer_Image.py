from io import BytesIO
from PIL import ImageGrab, Image, ImageEnhance
import win32clipboard
import pyautogui
import keyboard
import random
import time

# Made by Grdashark

count = 0
clipboard_image = None
start_bind = "ctrl+alt+shift+x"
print(f"Press '{start_bind}' to start. To stop the tool, hold 'd'")


def send_to_clipboard(image):
    output = BytesIO()
    image.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()


def start():
    global count, clipboard_image

    if clipboard_image:
        random_contrast = random.uniform(1, 10.5)

        enhancer = ImageEnhance.Contrast(Image.open("../clipboard_img.png"))
        new_image = enhancer.enhance(random_contrast)

        new_image.save("random_contrast_modified_image.jpg")

        send_to_clipboard(new_image)
        keyboard.press("ctrl")
        keyboard.press("v")
        pyautogui.click()

    else:
        print("No image data found in clipboard.")


while True:
    if keyboard.is_pressed(start_bind):
        print("Sending images...")
        while True:
            count += 1
            if count < 2:
                clipboard_image = ImageGrab.grabclipboard().convert('RGB')
                clipboard_image.save("original_clip_image.png")
            if keyboard.is_pressed("d"):
                keyboard.release("ctrl")
                print("-"*42+f"\n{count} Images with a random hue has been copied and pasted.\n"+"-"*42)
                input('Press "Enter" to leave the app')
                print("Exiting...")
                exit()
            else:
                time.sleep(0.05)
                start()
