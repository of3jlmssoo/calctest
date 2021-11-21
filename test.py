# from enum import Enum

import pyautogui


class Calc(object):

    def __init__(self) -> None:
        pyautogui.PAUSE = 0

    if (False):
        adjx = 0
        adjy = 0
        adjx4input = 0
        adjy4input = 0
    else:
        adjx = 50
        adjy = 610
        adjx4input = 233
        adjy4input = 640

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

        'input': [77 + adjx4input, 77 + adjy4input]
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
        # self.moveTo('input')
        # self.click()
        pyautogui.click(
            self.XY['input'][0],
            self.XY['input'][1],
            clicks=1,
            interval=0.5)
        pyautogui.typewrite(input)

        if message:
            self.confirm(message)

    def typewrite_clear(self, input, message=False):
        self.typewrite(input, message)
        self.clear()

    def click(self, pos=False, message=False):

        if pos:

            # print(f'{self.XY[pos][0]=}, {self.XY[pos][1]=}')
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

# # print('クリックして0～9を入力できる。')
# for n in range(10):
#     calc.click_clear(calc.zero2nine[n], str(n) + 'をクリック')

# # 3.2.1.1 整数の入力 　操作エリアから0～9を入力できる。
# print('\n3.2.1.1 整数の入力 　操作エリアから0～9を入力できる。')
# for n in range(10):
#     calc.typewrite_clear(str(n), str(n) + 'を入力')

# # 3.2.1.2 小数の入力 　操作エリアから「．」を入力することで、小数を表現できる。
# calc.click('period', '.を入力')
# calc.typewrite('123', '小数点以下(123)を入力')
# calc.click('plus', 'プラスを入力')
# calc.click('one', '1を入力')
# calc.click('period', '.を入力')
# calc.typewrite('377', '小数点以下(377)を入力 => 1.5')
# calc.click('equal', 'equalを入力(1.5)')

# 3.2.1.3 演算子の入力 操作エリアから「加算・減算・乗算・除算・剰余」を
# 表す、「＋」「－」「＊」「／」「％」を入力できる。

# # 「＋」
# calc.typewrite('123', '123を入力')
# calc.click('plus', 'プラスを入力')
# calc.typewrite('77', '77を入力')
# calc.click('equal', 'equalを入力(200)')

# calc.clear()

# calc.typewrite('123', '123を入力')
# calc.click('plus', 'プラスを入力')
# calc.typewrite('73', '73を入力')
# calc.click('plusandminus', 'プラス/マイナスを入力')
# calc.click('equal', 'equalを入力(50)')


# # 「－」
# calc.clear()

# calc.typewrite('123', '123を入力')
# calc.click('minus', 'マイナスを入力')
# calc.typewrite('23', '23を入力')
# calc.click('equal', 'equalを入力(100)')

# calc.clear()

# calc.typewrite('10', '10を入力')
# calc.click('minus', 'マイナスを入力')
# calc.typewrite('30', '30を入力')
# calc.click('equal', 'equalを入力(-20)')

# # 「＊」
# calc.clear()

# calc.typewrite('10', '10を入力')
# calc.click('asterisc', 'アスタリスクを入力')
# calc.typewrite('30', '30を入力')
# calc.click('equal', 'equalを入力(300)')

# calc.clear()

# calc.typewrite('10', '10を入力')
# calc.click('asterisc', 'アスタリスクを入力')
# calc.typewrite('30', '30を入力')
# calc.click('plusandminus', 'プラス/マイナスを入力')
# calc.click('equal', 'equalを入力(-300)')

# # 「／」

# calc.clear()

# calc.typewrite('9', '9を入力')
# calc.click('slash', 'スラッシュを入力')
# calc.typewrite('4', '4を入力')
# calc.click('equal', 'equalを入力(2.25)')

# calc.clear()

# calc.typewrite('9', '9を入力')
# calc.click('slash', 'スラッシュを入力')
# calc.typewrite('4', '4を入力')
# calc.click('plusandminus', 'プラス/マイナスを入力')
# calc.click('equal', 'equalを入力(-2.25)')


# 「％」
# calc.clear()

# calc.typewrite('9', '9を入力')
# calc.click('percent', 'パーセントを入力')
# calc.typewrite('4', '4を入力')
# calc.click('equal', 'equalを入力(1)')

# calc.clear()


# 3.2.1.4 特殊演算の入力 　四則演算・剰余以外の特殊な演算として、
# 操作エリアから、「平方根」「符号反転」を表す、「√」「＋／－」を入力できる。

# calc.clear()

# calc.typewrite('9', '9を入力')
# calc.click('root', 'ルートを入力(3)')

# calc.clear()

# calc.typewrite('4', '4を入力')
# calc.click('plusandminus', 'プラス/マイナスを入力(-4)')


# 3.2.2.2 繰り返し演算 　一度演算した後、繰り返し演算が実行できる。

# calc.clear()
# calc.click('one', '1を入力')
# calc.click('plus', '+を入力')
# calc.click('two', '2を入力')
# calc.click('equal', '=を入力(3)')
# calc.click('plus', '+を入力')
# calc.click('seven', '7を入力')
# calc.click('equal', '=を入力(10)')

# 3.2.4 表示機能
# 操作エリアからの入力情報や演算結果は、表示エリアに表示できる。なお、入出力する桁数は、
# 最大で整数部 3 桁、小数部 3 桁とする（○○○.○○○）。
# calc.clear()
# calc.click('one', '(整数部3桁入力)1を入力')
# calc.click('two', '(整数部3桁入力)2を入力')
# calc.click('three', '(整数部3桁入力)3を入力(123)')

# calc.clear()
# calc.click('one', '(整数部4桁入力)1を入力')
# calc.click('two', '(整数部4桁入力)2を入力')
# calc.click('three', '(整数部4桁入力)3を入力(123)')
# calc.click('four', '(整数部4桁入力)4を入力(123)')

# calc.clear()
# calc.click('zero', '(小数部3桁入力)0を入力')
# calc.click('period', '(小数部3桁入力).を入力')
# calc.click('one', '(小数部3桁入力)1を入力')
# calc.click('two', '(小数部3桁入力)2を入力')
# calc.click('three', '(小数部3桁入力)3を入力(0.123)')

# calc.clear()
# calc.click('zero', '(小数部4桁入力)0を入力')
# calc.click('period', '(小数部4桁入力).を入力')
# calc.click('one', '(小数部4桁入力)1を入力')
# calc.click('two', '(小数部4桁入力)2を入力')
# calc.click('three', '(小数部4桁入力)3を入力(0.123)')
# calc.click('four', '(小数部4桁入力)4を入力(0.123)')

calc.clear()
calc.click('one', '(整3+小3桁入力)1を入力')
calc.click('two', '(整3+小3桁入力)2を入力')
calc.click('three', '(整3+小3桁入力)3を入力(123)')
calc.click('period', '(整3+小3桁入力).を入力')
calc.click('four', '(整3+小3桁入力)4を入力')
calc.click('five', '(整3+小3桁入力)5を入力')
calc.click('six', '(整3+小3桁入力)6を入力(123.456)')
