# from enum import Enum

import math
import random
from decimal import ROUND_HALF_UP, Decimal

import pyautogui


class Calc(object):

    def __init__(self) -> None:
        pyautogui.PAUSE = 0

    if (True):
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

        # 'input': [77 + adjx4input, 77 + adjy4input]
        'input': [246 + adjx4input, 77 + adjy4input]
    }

    calcchar = {
        '+': 'plus',
        '-': 'minus',
        '*': 'asterisc',
        '/': 'slash',
        '%': 'percent'}

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

    def convert2input(self, input, output):
        """
        '1 + 3 = * 4 =' の場合
            eval        pyautogui
        1   1           typewrite(1)
        +   1 +         click('+')
        3   1 + 3       typewrite(3)
        =   r=eval(1+3) click('=')
        *   r *         click(*)
        4   r * 4       typewrite(4)
        =   r=eval(r*4) click('=')

        """
        result = 0
        target = ''

        input_list = input.split()
        for i in input_list:
            # if i not in ['+', '-', '*', '/', '=', '%']:
            #     print(f'type {i}')
            # else:
            #     print(f'click {i}')

            if i == '=':
                # calc.typewrite(str(target), f'{target}')
                calc.click('equal', '= was typed')
                result = eval(target)
                target = str(result)
            elif i in self.calcchar.keys():
                calc.click(self.calcchar[i], f'click {i}')
                target = target + i
            else:
                calc.typewrite(i, f'{i} was typed')
                target = target + i
        self.confirm(f'{input} : eval result {result} and result {output}')


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

# # 3.3.1 初期処理 プログラムを開始すると、入力待ちモードに遷移する。また、「＝」ボタンは無効化する。
# print('\n3.3.1 初期処理 プログラムを開始すると、入力待ちモードに遷移する。また、「＝」ボタンは無効化する。')
# calc.confirm('プログラムを開始すると、入力待ちモードに遷移する。また、「＝」ボタンは無効化する。')

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

# # 3.2.1.3 演算子の入力 操作エリアから「加算・減算・乗算・除算・剰余」を表す、「＋」「－」「＊」「／」「％」を入力できる。
# print('\n3.2.1.3 演算子の入力 操作エリアから「加算・減算・乗算・除算・剰余」を表す、「＋」「－」「＊」「／」「％」を入力できる。')
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


# # 3.2.1.4 特殊演算の入力 　四則演算・剰余以外の特殊な演算として、
# # 操作エリアから、「平方根」「符号反転」を表す、「√」「＋／－」を入力できる。
# print('\n3.2.1.4 特殊演算の入力 　四則演算・剰余以外の特殊な演算として、操作エリアから、「平方根」「符号反転」を表す、「√」「＋／－」を入力できる。')
# calc.clear()

# calc.typewrite('9', '9を入力')
# calc.click('root', 'ルートを入力(3)')

# calc.clear()

# calc.typewrite('4', '4を入力')
# calc.click('plusandminus', 'プラス/マイナスを入力(-4)')

# print('\n3.2.1.5 演算実行の入力 操作エリアから「＝」を入力できる。')
# calc.clear()

# calc.typewrite('9', '9を入力')
# calc.click('percent', 'パーセントを入力')
# calc.typewrite('4', '4を入力')
# calc.click('equal', 'equalを入力(1)')

# print('\n3.2.1.6 クリアの入力 操作エリアから入力内容のクリアを表す、「C」を入力できる。')
# calc.clear()

# calc.typewrite('9', '9を入力')
# calc.click('percent', 'パーセントを入力')
# calc.typewrite('4', '4を入力')
# calc.click('equal', 'equalを入力(1)')

# calc.clear()

# # > 3.2.2.1 基本演算 入力情報に従って、「加算・減算・乗算・除算・剰余」を実行できる。
# print('3.2.2.1 基本演算 入力情報に従って、「加算・減算・乗算・除算・剰余」を実行できる。')
# print(' => 3.2.1.3で実施済み')


# # 3.2.2.2 繰り返し演算 　一度演算した後、繰り返し演算が実行できる。
# print('\n3.2.2.2 繰り返し演算 　一度演算した後、繰り返し演算が実行できる。')
# calc.clear()
# calc.click('one', '1を入力')
# calc.click('plus', '+を入力')
# calc.click('two', '2を入力')
# calc.click('equal', '=を入力(3)')
# calc.click('plus', '+を入力')
# calc.click('seven', '7を入力')
# calc.click('equal', '=を入力(10)')

# # 3.2.3 特殊演算 「平方根・符号反転」を実行できる。
# print('\n3.2.3 特殊演算 「平方根・符号反転」を実行できる。')
# print(' => 3.2.1.4で実施済み')


# # 3.2.4 表示機能
# print('\n3.2.4 表示機能')

# # 操作エリアからの入力情報や演算結果は、表示エリアに表示できる。なお、入出力する桁数は、
# # 最大で整数部 3 桁、小数部 3 桁とする（○○○.○○○）。
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

# calc.clear()
# calc.click('one', '(整3+小3桁入力)1を入力')
# calc.click('two', '(整3+小3桁入力)2を入力')
# calc.click('three', '(整3+小3桁入力)3を入力(123)')
# calc.click('period', '(整3+小3桁入力).を入力')
# calc.click('four', '(整3+小3桁入力)4を入力')
# calc.click('five', '(整3+小3桁入力)5を入力')
# calc.click('six', '(整3+小3桁入力)6を入力(123.456)')

#
# 詳細設計
#

# # 3.3.1 初期処理 プログラムを開始すると、入力待ちモードに遷移する。また、「＝」ボタンは無効化する。
# print('\n3.3.1 初期処理 プログラムを開始すると、入力待ちモードに遷移する。また、「＝」ボタンは無効化する。')
# print('Calculator.py実施直後に確認済み')

# # 3.3.2.1 入力待ちモード
# print('\n3.3.2.1 入力待ちモード 操作エリアから「0 ～ 9」か「．」の入力がある場合は、入力情報を表示エリアに表示し、入力処理 1 に遷移する。ただし、未入力の状態で「．」を選択した場合は、「0.」を表示する。')
# print('\n3.2.1.1, 3.2.1.2で実施済み')


# # 3.3.2.2 入力処理 1 モード、入力処理 2 モード
print('\n3.3.2.2 入力処理 1 モード、入力処理 2 モード')
# # > 　操作エリアから「0 ～ 9」か「．」の入力がある場合は、表示エリアに数値を表示する。ただし、以下のルールがある。
# # >
# # > 数値が既に存在する場合は、右から連結して表示する
# # > 例：12 の状態で 1 を入力すると、121 となる
# for i in range(3):
#     v = random.randint(0, 9)
#     calc.click(calc.zero2nine[v], f'{v}を入力')
# # > 先頭に 0 がある場合は、0 を 2 回続けて入力できない。また、0 の後に数値を入力した場合は、0 を別の数値に上書きする
# calc.clear()
# calc.click('zero', '0を入力')
# calc.click('zero', '続けて0を入力(表示の0は一つのまま)')

# for i in range(1, 10):
#     calc.clear()
#     calc.click('zero', '0を入力')
#     calc.click(calc.zero2nine[i], f'{i}を入力(0が消えてこの値のみ表示されている)')

# # > 未入力の状態で「.」を選択した場合は、先頭に 0.を付与する
# calc.clear()
# calc.click('period', '.を入力(0.が表示されている)')

# # > 小数は最大で 3 桁までしか入力できない
# # > 入力値の制限は、最大値（999.999）、最小値（－999.999）とする
# v1 = str(random.randint(100, 999))
# calc.typewrite(v1, f'整数部として{v1}を入力')

# v2 = random.randint(0, 9)
# calc.click(calc.zero2nine[v2], f'更に{v2}をクリック。{v1}のままである')

# calc.click('period', '.を入力')

# v3 = str(random.randint(100, 999))
# calc.typewrite(v3, f'小数部として{v3}を入力')

# v4 = random.randint(0, 9)
# calc.click(calc.zero2nine[v4], f'更に{v4}をクリック。{v1}.{v3}のままである')

# # 3.3.3.1 入力処理 1 モード 演算子（＋、－、＊、／、％）を入力した場合は、表示エリアの入力情報と入力した演算子を記憶し、入力処理 2
# # に遷移する。また、表示エリアをクリアし、（＋、－、＊、／、％）ボタンを無効化し、「＝」ボタンを有効化する。
# print('\n3.3.3.1 入力処理 1 モード 演算子（＋、－、＊、／、％）を入力した場合は、表示エリアの入力情報と入力した演算子を記憶し、入力処理 2 に遷移する。また、表示エリアをクリアし、（＋、－、＊、／、％）ボタンを無効化し、「＝」ボタンを有効化する。')
# # + - * / %
# for calcchar in calc.calcchar:
#     input_val1 = ''
#     calc.clear()

#     # 整数部３桁入力
#     for i in range(3):
#         v = random.randint(0, 9)
#         calc.click(calc.zero2nine[v])
#         input_val1 = input_val1 + str(v)

#     calc.click('period')
#     input_val1 = input_val1 + '.'

#     # 小数部３桁入力
#     for i in range(3):
#         v = random.randint(0, 9)
#         calc.click(calc.zero2nine[v])
#         input_val1 = input_val1 + str(v)

#     calc.confirm(f'{input_val1}が入力された')
#     calc.click(
#         calc.calcchar[calcchar],
#         f'{calcchar}が入力され、+-*/%が無効化され、=が有効化された')

#     input_val2 = ''

#     # 整数部３桁入力
#     for i in range(3):
#         v = random.randint(0, 9)
#         calc.click(calc.zero2nine[v])
#         input_val2 = input_val2 + str(v)

#     calc.click('period')
#     input_val2 = input_val2 + '.'

#     # 小数部３桁入力
#     for i in range(3):
#         v = random.randint(0, 9)
#         calc.click(calc.zero2nine[v])
#         input_val2 = input_val2 + str(v)

#     left_side = input_val1 + ' ' + calcchar + ' ' + input_val2
#     result = eval(left_side)
#     calc.click('equal', f'{input_val2}が入力され=が入力された。{result} =が無効化された')


# # 3.3.3.2 入力待ちモード 繰り返し演算（1回演算した後、続けて演算子（＋、－、＊、／、％）を入力）した場合は、表示エリアの入力情報と選択した演算子を取得する。さらに、表示エリアをクリアし、入力処理
# # 2 に遷移する。また、「＋、－、＊、／、％」ボタンを無効化、「＝」ボタンを有効化する。
# print('\n3.3.3.2 入力待ちモード')
# calc.clear()
# calc.confirm('最初の演算(=を入力)後+を入力した時点で「＋、－、＊、／、％」ボタンを無効化、「＝」ボタンを有効化')
# calc.convert2input('1 + 3 = + 4 =', 8)

# calc.clear()
# calc.confirm('最初の演算(=を入力)後-を入力した時点で「＋、－、＊、／、％」ボタンを無効化、「＝」ボタンを有効化')
# calc.convert2input('1 + 3 = - 4 =', 0)

# calc.clear()
# calc.confirm('最初の演算(=を入力)後*を入力した時点で「＋、－、＊、／、％」ボタンを無効化、「＝」ボタンを有効化')
# calc.convert2input('1 + 3 = * 4 =', 16)

# calc.clear()
# calc.confirm('最初の演算(=を入力)後/を入力した時点で「＋、－、＊、／、％」ボタンを無効化、「＝」ボタンを有効化')
# calc.convert2input('1 + 3 = / 4 =', 1)

# calc.clear()
# calc.confirm('最初の演算(=を入力)後%を入力した時点で「＋、－、＊、／、％」ボタンを無効化、「＝」ボタンを有効化')
# calc.convert2input('1 + 3 = % 3 =', 1)

# calc.clear()
# calc.convert2input('1.5 + 3.3 = * 4 =', 19.2)
# calc.clear()
# calc.convert2input('999.999 * 999.999 =', 999998.000001)


# 3.3.4.1 入力待ちモード、入力処理 1 モード、入力処理 2 モード
# > 　特殊演算を行う場合は、演算結果を表示エリアに表示する。
# >
# > 表示エリアが空欄以外で、√ を入力する場合は、表示エリアの入力情報から平方根を演算し、表示エリアに表示する。なお、出力が小数第 4 位以降となる場合は、小数第 4 位を四捨五入し、3 桁で表示する。
# > 表示エリアが空欄以外で、＋／－を入力する場合は、表示エリアの入力情報から符号を反転し、表示エリアに表示する。
print('\n3.3.4.1 入力待ちモード、入力処理 1 モード、入力処理 2 モード')
# root
# calc.clear()
# calc.click('root', 'rootをクリックしても何も起きない')
# calc.click('nine', '9をクリック')
# calc.click('root', f'rootをクリック。{math.sqrt(9)}')
calc.clear()
calc.click('three', '3をクリック')
result = Decimal(str(math.sqrt(3))).quantize(
    Decimal('0.001'), rounding=ROUND_HALF_UP)
calc.click('root', f'rootをクリック。{result}')

# + and -

# 3.3.5 クリアイベント
# > 3.3.5.1 入力待ちモード、入力処理 1 モード、入力処理 2 モード
# > 　「C」を選択した場合は、表示エリアの文字、表示エリアと演算子の入力情報、ボタンの状態を初期状態に戻す。また、入力待ちモードに遷移する。
print('\n3.3.5 クリアイベント')


# 3.3.6.1 入力待ちモード、入力処理 2 モード
# > 　表示エリアが空欄でない状態で、「＝」ボタンを選択した場合、下記の演算結果を表示エリアに表示し、入力待ちモードに遷移する。遷移する際、「＋、－、＊、／、％」ボタンを有効化し、「＝」を無効化する。なお、出力結果は、小数となる場合は、小数第 4 位を四捨五入し、3 桁として表示する。
# >
# > 通常の演算の場合
# > 演算子が「＋」の場合
# > 演算結果＝入力処理 1 モードの入力情報＋入力処理 2 モードの入力情報
# > 演算子が「－」の場合
# > 演算結果＝入力処理 1 モードの入力情報－入力処理 2 モードの入力情報
# > 演算子が「＊」の場合
# > 演算結果＝入力処理 1 モードの入力情報＊入力処理 2 モードの入力情報
# > 演算子が「／」の場合
# > 演算結果＝入力処理 1 モードの入力情報／入力処理 2 モードの入力情報
# > 演算子が「％」の場合
# > 演算結果＝入力処理 1 モードの入力情報％入力処理 2 モードの入力情報
# > 繰り返し演算の場合
# > 演算子が「＋」の場合
# > 演算結果＝入力待ちモードの入力情報＋入力処理 2 モードの入力情報
# > 演算子が「－」の場合
# > 演算結果＝入力待ちモードの入力情報－入力処理 2 モードの入力情報
# > 演算子が「＊」の場合
# > 演算結果＝入力待ちモードの入力情報＊入力処理 2 モードの入力情報
# > 演算子が「／」の場合
# > 演算結果＝入力待ちモードの入力情報／入力処理 2 モードの入力情報
# > 演算子が「％」の場合
# > 演算結果＝入力待ちモードの入力情報％入力処理 2 モードの入力情報
# > 　また、演算結果の最大、最小の処理は以下とする。
# > 最大：演算結果＞ 3000 の場合
# > 演算結果＝ 3000
# > 最小：演算結果＜－3000 の場合
# > 演算結果＝－3000

print('\n3.3.6.1 入力待ちモード、入力処理 2 モード')


# 3.4 制限事項
# > テスト項目を記述するのが面倒になることが予想されるため、プログラムに入力できる最大、最小の数値は 999.999 と－999.999 に制限する。また、演算結果の最大、最小は、3000 と－3000 に制限する
print('\n3.4 制限事項')

calcchar = {'+': 'plus', '-': 'minus', '*': 'asterisc', '/': 'slush'}


# def convert2input(input, output):
#     """
#     '1 + 3 = * 4 =' の場合
#         eval        pyautogui
#     1   1           typewrite(1)
#     +   1 +         click('+')
#     3   1 + 3       typewrite(3)
#     =   r=eval(1+3) click('=')
#     *   r *         click(*)
#     4   r * 4       typewrite(4)
#     =   r=eval(r*4) click('=')

#     """
#     result = 0
#     target = ''

#     input_list = input.split()
#     for i in input_list:
#         # if i not in ['+', '-', '*', '/', '=', '%']:
#         #     print(f'type {i}')
#         # else:
#         #     print(f'click {i}')

#         if i == '=':
#             # calc.typewrite(str(target), f'{target}')
#             calc.click('equal', '= was typed')
#             result = eval(target)
#             target = str(result)
#         elif i in ['+', '-', '*', '/']:
#             calc.click(self.calcchar[i], f'click {i}')
#             target = target + i
#         else:
#             calc.typewrite(i, f'{i} was typed')
#             target = target + i
#     print(f'{input} : eval result {result} and result {output}')


# convert2input('1 + 3 =', 4)
# convert2input('1 + 3 = * 4 =', 16)
# convert2input('1.5 + 3.3 = * 4 =', 19.2)
# convert2input('999.999 * 999.999 =', 999998.000001)
