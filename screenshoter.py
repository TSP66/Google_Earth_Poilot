import pyautogui
import PIL
import struct

def get_dimensions(test):

  
    with open(test, "rb") as f:
        data = bytearray(f.read())

    width = struct.unpack_from('<i', data, 18)
    height = struct.unpack_from('<i', data, 22)

    print(width[0])
    print(height[0])

    return int(width[0]), int(height[0])


def take_shot(number):
    myScreenshot = pyautogui.screenshot()
    n = r'Shots/' + str(number) + '.png'
    myScreenshot.save(n)


