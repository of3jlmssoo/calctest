# from enum import Enum

import pyautogui


class Calc(object):

    def __init__(self) -> None:
        pyautogui.PAUSE = 0

    adjx = 0
    adjy = 0
    XY = {
        'plus': [51 + adjx, 125 + adjy],
        'minus': [126 + adjx, 125 + adjy],
        'asterisc': [183 + adjx, 125 + adjy],
        'slash': [242 + adjx, 125 + adjy],
        'one': [51 + adjx, 190 + adjy],
        'two': [126 + adjx, 190 + adjy],
        'three': [183 + adjx, 190 + adjy],
        'equal': [242 + adjx, 190 + adjy],
        'four': [51 + adjx, 248 + adjy],
        'five': [126 + adjx, 248 + adjy],
        'six': [183 + adjx, 248 + adjy],
        'clear': [242 + adjx, 248 + adjy],
        'seven': [51 + adjx, 312 + adjy],
        'eight': [126 + adjx, 312 + adjy],
        'nine': [183 + adjx, 312 + adjy],
        'zero': [242 + adjx, 312 + adjy],
        'period': [51 + adjx, 368 + adjy],
        'root': [126 + adjx, 368 + adjy],
        'percent': [183 + adjx, 368 + adjy],
        'plusandminus': [242 + adjx, 368 + adjy],

        'input': [77 + adjx, 77 + adjy]
    }
    zero2nine = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine']

    def typewrite(self, input, message=False):
        self.moveTo('input')
        self.click()
        pyautogui.typewrite(input)

        if message:
            self.confirm(message)

    def typewrite_clear(self, input, message=False):
        self.typewrite(input, message)
        self.clear()

    def click(self, pos=False, message=False):

        if pos:
            pyautogui.click(
                self.XY[pos][0],
                self.XY[pos][1],
                clicks=1,
                interval=0,
                button='left')
        else:
            pyautogui.click()

        if message:
            self.confirm(message)

    def click_clear(self, pos, message=False):
        # inmessage = input()
        self.click(pos, message)
        self.clear()

    def moveTo(self, pos):
        # print(self.XY[pos][0], self.XY[pos][1])
        pyautogui.moveTo(self.XY[pos][0], self.XY[pos][1])

    def clear(self):
        pyautogui.click(
            self.XY['clear'][0],
            self.XY['clear'][1],
            clicks=1,
            interval=0,
            button='left')

    def confirm(self, message):
        result = pyautogui.confirm(message)
        print(f'{message} {result}')


# pyautogui.moveTo(XY['plus'][0], XY['plus'][1])
# pyautogui.moveTo(XY['minus'][0], XY['minus'][1])
# pyautogui.moveTo(XY['asterisc'][0], XY['asterisc'][1])
# pyautogui.moveTo(XY['slash'][0], XY['slash'][1])
# pyautogui.moveTo(XY['one'][0], XY['one'][1])
# pyautogui.moveTo(XY['two'][0], XY['two'][1])
# pyautogui.moveTo(XY['three'][0], XY['three'][1])
# pyautogui.moveTo(XY['equal'][0], XY['equal'][1])
# pyautogui.moveTo(XY['four'][0], XY['four'][1])
# pyautogui.moveTo(XY['five'][0], XY['five'][1])
# pyautogui.moveTo(XY['clear'][0], XY['clear'][1])
# pyautogui.moveTo(XY['seven'][0], XY['seven'][1])
# pyautogui.moveTo(XY['eight'][0], XY['eight'][1])
# pyautogui.moveTo(XY['nine'][0], XY['nine'][1])
# pyautogui.moveTo(XY['zero'][0], XY['zero'][1])
# pyautogui.moveTo(XY['period'][0], XY['period'][1])
# pyautogui.moveTo(XY['root'][0], XY['root'][1])
# pyautogui.moveTo(XY['percent'][0], XY['percent'][1])
# pyautogui.moveTo(XY['plusandminus'][0], XY['plusandminus'][1])


calc = Calc()

calc.click_clear('clear')

print('クリックして0～9を入力できる。')

for n in range(10):
    calc.click_clear(calc.zero2nine[n], str(n) + 'をクリック')

# 3.2.1.1 整数の入力 　操作エリアから0～9を入力できる。
print('\n3.2.1.1 整数の入力 　操作エリアから0～9を入力できる。')
for n in range(10):
    calc.typewrite_clear(str(n), str(n) + 'を入力')

# 3.2.1.2 小数の入力 　操作エリアから「．」を入力することで、小数を表現できる。
