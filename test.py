"""
前提 ： Caluclator.pyを画面上同じ位置において実行する必要がある。
        Calculation.pyの入力エリアや+ボタンといったコンポーネントの座標をXYで定義している。
            pyautogui.position()
            pyatuogui.moveTo(X,Y)
"""
import datetime
import math
import random
from decimal import ROUND_HALF_UP, Decimal

import pyautogui


class Calc(object):

    def __init__(self) -> None:
        """
        変数
        self.XY : Caluclator.py の入力エリアやボタンの座標を定義
        self.adx* : 座標を環境により調整する変数
        self.calchar : +-*/%の演算子を'plus'等に変換する辞書。self.XY へのアクセス時に使う
        self.zero2nine : 0-9 の数字を'zero'等に変換する辞書。self.XY へのアクセス時に使う
        """

        """ pyautoguiの遷移をスムースにするために設定 """
        pyautogui.PAUSE = 0

        """ テスト環境が2つあったため、テスト環境1の場合True、テスト
        環境2の場合Falseにすることで環境を切り替え """
        if (True):
            self.adjx = 0
            self.adjy = 0
            self.adjx4input = 0
            self.adjy4input = 0
        else:
            self.adjx = 50
            self.adjy = 610
            self.adjx4input = 233
            self.adjy4input = 640

        self.XY = {
            'plus': [51 + self.adjx, 125 + self.adjy],
            'minus': [126 + self.adjx, 125 + self.adjy],
            'asterisc': [183 + self.adjx, 125 + self.adjy],
            'slash': [242 + self.adjx, 125 + self.adjy],
            'one': [51 + self.adjx, 190 + self.adjy],
            'two': [126 + self.adjx, 190 + self.adjy],
            'three': [183 + self.adjx, 190 + self.adjy],
            'equal': [242 + self.adjx, 190 + self.adjy],
            'four': [51 + self.adjx, 248 + self.adjy],
            'five': [126 + self.adjx, 248 + self.adjy],
            'six': [183 + self.adjx, 248 + self.adjy],
            'clear': [242 + self.adjx, 248 + self.adjy],
            'seven': [51 + self.adjx, 312 + self.adjy],
            'eight': [126 + self.adjx, 312 + self.adjy],
            'nine': [183 + self.adjx, 312 + self.adjy],
            'zero': [242 + self.adjx, 312 + self.adjy],
            'period': [51 + self.adjx, 368 + self.adjy],
            'root': [126 + self.adjx, 368 + self.adjy],
            'percent': [183 + self.adjx, 368 + self.adjy],
            'plusandminus': [242 + self.adjx, 368 + self.adjy],

            # 入力エリアの右端にくるように調整する
            'input': [246 + self.adjx4input, 77 + self.adjy4input],

            'flip': [235 + self.adjx, 45 + self.adjy],
            'min': [262 + self.adjx, 45 + self.adjy],
            'close': [285 + self.adjx, 45 + self.adjy]
        }

        """ 記号からXYを利用するのにcalccharを利用 """
        self.calcchar = {
            '+': 'plus',
            '-': 'minus',
            '*': 'asterisc',
            '/': 'slash',
            '%': 'percent'}

        """ 数字からXYを利用するのにzero2nineを利用 """
        self.zero2nine = [
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
        """
        inputとして指定された式を入力する

        変数
        input : '1 + 2 ='というような式の文字列。pyautogui.typewrie()への
                インプットとなる
        message : inputに伴うメッセージの文字列。self.confirm()への
                インプットとなる。
        """

        """
        入力エリアの右端にカーソルをあわせてクリックしてからtypewrite()をコール
        クリック位置を間違うと左側にアペンドされる形態で入力、表示されてしまう。
        """
        pyautogui.click(
            self.XY['input'][0],
            self.XY['input'][1],
            clicks=1,
            interval=0.5)
        pyautogui.typewrite(input)

        if message:
            self.confirm(message)

    def typewrite_clear(self, input, message=False):
        """
        inputとして指定された式を入力し、その後クリアする

        変数
        input : '1 + 2 ='というような式の文字列。pyautogui.typewrie()への
                インプットとなる
        message : inputに伴うメッセージの文字列。self.typewrite()への
                  インプットとなる
        """

        self.typewrite(input, message)
        self.clear()

    def click(self, pos=False, message=False):
        """posが指定された場合posの位置でクリック。
        指定が無い場合その場でクリック

        posにはself.XYのキーを指定する。キーに対応する座標位置ででクリックを行う。

        変数
        pos : self.XYのキー。キーが有効か無効か判断するロジックを追加したほうが良い。
        message : def click()の最後でself.confirmを呼出し、
                  messageを引数として指定している
        """
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
        """
        self.click()にposをmessageを渡し、その後self.clear()をコールしてCをクリックする

        変数
        pos : self.XYのキー。self.click()へのインプットとなる
        message : メッセージ。self.click()へのインプットとなる
        """
        self.click(pos, message)
        self.clear()

    def moveTo(self, pos):
        """
        指定されたposへ移動する

        変数
        pos: self.XYのキー。pyautogui.moveToへのインプットとなる
        """

        # print(self.XY[pos][0], self.XY[pos][1])
        pyautogui.moveTo(self.XY[pos][0], self.XY[pos][1])

    def clear(self):
        """
        クリアをクリックする
        """
        pyautogui.click(
            self.XY['clear'][0],
            self.XY['clear'][1],
            clicks=1,
            interval=0,
            button='left')

    def confirm(self, message):
        """
        pyautoguiのconfirmをコールし、messageを表示。同じ内容をコンソールに表示する

        変数
        message: pyautoguiのconfirmへ渡し、かつ、コンソールに表示されるメッセージ
        """

        result = pyautogui.confirm(message)
        print(f'{message} {result}')

    def convert2input(self, input, output, func):
        """
        inputで指定された式をCalculator.pyに入力する

        変数
        input: '1 + 3 = * 4 ='というようなインプット。
        このインプットをCalculator.pyに入力し、かつevalで計算する
        output: 呼び出し元が想定される解をoutputとして指定
        func: Calculator.pyへの入力にあたりcalc.typewriteかcalc.click_stringのいずれかを指定

        '1 + 3 = * 4 =' の場合
        eval        pyautogui
        1   1           typewrite(1)
        +   1 + click('+')
        3   1 + 3       typewrite(3)
        =   r = eval(1 + 3) click('=')
        *   r * click(*)
        4   r * 4       typewrite(4)
        =   r = eval(r * 4) click('=')

        """
        result = 0
        target = ''

        input_list = input.split()
        for i in input_list:

            if i == '=':
                self.click('equal', '= was typed')
                result = eval(target)
                target = str(result)
            elif i in self.calcchar.keys():  # '+': 'plus', '-': 'minus', '*': 'asterisc', '/': 'slash', '%': 'percent'}
                self.click(self.calcchar[i], f'click {i}')
                target = target + i
            elif i == 'c' or i == 'C':
                self.clear()
                target = ''
            else:
                # calc.typewrite(i, f'{i} was typed')
                func(i, f'{i} was typed')
                target = target + i
        self.confirm(f'{input} : eval result {result} and result {output}')

    def click_string(self, strnum, message=''):
        """
        strnumで指定した数字をCalculator.pyへ入力する。 指定できるのは数字1組のみ

        変数
        strnum: '123'というような数字を一組だけ指定する
        message: 最後にself.confirmをコールしている。その際messageが渡される
        """
        for s in strnum:
            # print(f'{s=} {self.zero2nine[int(s)]}')
            if s == '.':
                self.click('period')
                continue
            if s in '0123456789':
                self.click(self.zero2nine[int(s)])
                continue
            print(f'input {strnum} is valid?')
        self.confirm(f'{strnum} typed')


calc = Calc()

# calc.click_clear('clear')


def test31():
    """ 3.1概要 """
    print('3.1 概要')
    calc.confirm('電卓アプリケーション起動直後のステータス確認 ： =が無効')
    calc.click('flip', 'アプリヘッダーのみ')
    calc.click('flip', 'アプリ本体再表示')
    calc.click('close', 'アプリ終了')


# def test331():
#     """ 3.3.1 初期処理 プログラムを開始すると、入力待ちモードに遷移する。また、「＝」ボタンは無効化する。
#     print('3.3.1 初期処理 プログラムを開始すると、入力待ちモードに遷移する。また、「＝」ボタンは無効化する。')
#     calc.confirm('プログラムを開始すると、入力待ちモードに遷移する。また、「＝」ボタンは無効化する。') """

#     # print('クリックして0～9を入力できる。')


def test3211():
    """ 3.2.1.1 整数の入力 　操作エリアから0～9を入力できる。 """
    print('3.2.1.1 整数の入力 　操作エリアから0～9を入力できる。')
    print('typewrite 0 - 9')
    calc.clear()
    for n in range(10):
        calc.typewrite_clear(str(n), str(n) + 'を入力')

    print('click 0 - 9')
    calc.clear()
    for n in range(10):
        calc.click_clear(calc.zero2nine[n], str(n) + 'をクリック')


def test3212():
    """ 3.2.1.2 小数の入力 　操作エリアから「．」を入力することで、小数を表現できる。 """
    calc.click('period', '.を入力')
    calc.typewrite('123', '小数点以下(123)を入力')
    calc.click('plus', 'プラスを入力')
    calc.click('one', '1を入力')
    calc.click('period', '.を入力')
    calc.typewrite('377', '小数点以下(377)を入力 => 1.5')
    calc.click('equal', 'equalを入力(1.5)')


def test3213():
    """ 3.2.1.3 演算子の入力 操作エリアから「加算・減算・乗算・除算・剰余」を表す、「＋」「－」「＊」「／」「％」を入力できる。 """
    print('3.2.1.3 演算子の入力 操作エリアから「加算・減算・乗算・除算・剰余」を表す、「＋」「－」「＊」「／」「％」を入力できる。')
    # 「＋」
    calc.clear()
    calc.typewrite('123', '123を入力')
    calc.click('plus', 'プラスを入力')
    calc.typewrite('77', '77を入力')
    calc.click('equal', 'equalを入力(200)')

    calc.clear()

    calc.typewrite('123', '123を入力')
    calc.click('plus', 'プラスを入力')
    calc.typewrite('73', '73を入力')
    calc.click('plusandminus', 'プラス/マイナスを入力')
    calc.click('equal', 'equalを入力(50)')

    # 「－」
    calc.clear()

    calc.typewrite('123', '123を入力')
    calc.click('minus', 'マイナスを入力')
    calc.typewrite('23', '23を入力')
    calc.click('equal', 'equalを入力(100)')

    calc.clear()

    calc.typewrite('10', '10を入力')
    calc.click('minus', 'マイナスを入力')
    calc.typewrite('30', '30を入力')
    calc.click('equal', 'equalを入力(-20)')

    # 「＊」
    calc.clear()

    calc.typewrite('10', '10を入力')
    calc.click('asterisc', 'アスタリスクを入力')
    calc.typewrite('30', '30を入力')
    calc.click('equal', 'equalを入力(300)')

    calc.clear()

    calc.typewrite('10', '10を入力')
    calc.click('asterisc', 'アスタリスクを入力')
    calc.typewrite('30', '30を入力')
    calc.click('plusandminus', 'プラス/マイナスを入力')
    calc.click('equal', 'equalを入力(-300)')

    # 「／」

    calc.clear()

    calc.typewrite('9', '9を入力')
    calc.click('slash', 'スラッシュを入力')
    calc.typewrite('4', '4を入力')
    calc.click('equal', 'equalを入力(2.25)')

    calc.clear()

    calc.typewrite('9', '9を入力')
    calc.click('slash', 'スラッシュを入力')
    calc.typewrite('4', '4を入力')
    calc.click('plusandminus', 'プラス/マイナスを入力')
    calc.click('equal', 'equalを入力(-2.25)')

    # 「％」
    calc.clear()

    calc.typewrite('9', '9を入力')
    calc.click('percent', 'パーセントを入力')
    calc.typewrite('4', '4を入力')
    calc.click('equal', 'equalを入力(1)')

    calc.clear()


def test3214():
    """ 3.2.1.4 特殊演算の入力 　四則演算・剰余以外の特殊な演算として、
    操作エリアから、「平方根」「符号反転」を表す、「√」「＋／－」を入力できる。 """
    print('3.2.1.4 特殊演算の入力 　四則演算・剰余以外の特殊な演算として、操作エリアから、「平方根」「符号反転」を表す、「√」「＋／－」を入力できる。')
    calc.clear()

    calc.typewrite('9', '9を入力')
    calc.click('root', 'ルートを入力(3)')

    calc.clear()

    calc.typewrite('4', '4を入力')
    calc.click('plusandminus', 'プラス/マイナスを入力(-4)')


def test3215():
    print('3.2.1.5 演算実行の入力 操作エリアから「＝」を入力できる。')
    calc.clear()

    calc.typewrite('9', '9を入力')
    calc.click('percent', 'パーセントを入力')
    calc.typewrite('4', '4を入力')
    calc.click('equal', 'equalを入力(1)')


def test3216():
    print('3.2.1.6 クリアの入力 操作エリアから入力内容のクリアを表す、「C」を入力できる。')
    calc.clear()

    calc.typewrite('9', '9を入力')
    calc.click('percent', 'パーセントを入力')
    calc.typewrite('4', '4を入力')
    calc.click('equal', 'equalを入力(1)')

    calc.clear()

# # > 3.2.2.1 基本演算 入力情報に従って、「加算・減算・乗算・除算・剰余」を実行できる。


def test3221():
    print('3.2.2.1 基本演算 入力情報に従って、「加算・減算・乗算・除算・剰余」を実行できる。')
    print(' => 3.2.1.3で実施済み')


def test3222():
    """ 3.2.2.2 繰り返し演算 　一度演算した後、繰り返し演算が実行できる。"""
    print('3.2.2.2 繰り返し演算 　一度演算した後、繰り返し演算が実行できる。')
    calc.clear()
    calc.click('one', '1を入力')
    calc.click('plus', '+を入力')
    calc.click('two', '2を入力')
    calc.click('equal', '=を入力(3)')
    calc.click('plus', '+を入力')
    calc.click('seven', '7を入力')
    calc.click('equal', '=を入力(10)')


def test323():
    """ 3.2.3 特殊演算 「平方根・符号反転」を実行できる。 """
    print('3.2.3 特殊演算   「平方根・符号反転」を実行できる。')
    print(' => 3.2.1.4で実施済み')


def test324():
    """ 3.2.4 表示機能 """
    print('3.2.4 表示機能')

    """ 操作エリアからの入力情報や演算結果は、表示エリアに表示できる。なお、入出力する桁数は、
    最大で整数部 3 桁、小数部 3 桁とする（○○○.○○○）。"""
    calc.clear()
    calc.click('one', '(整数部3桁入力)1を入力')
    calc.click('two', '(整数部3桁入力)2を入力')
    calc.click('three', '(整数部3桁入力)3を入力(123)')

    calc.clear()
    calc.click('one', '(整数部4桁入力)1を入力')
    calc.click('two', '(整数部4桁入力)2を入力')
    calc.click('three', '(整数部4桁入力)3を入力(123)')
    calc.click('four', '(整数部4桁入力)4を入力(123のまま)')

    calc.clear()
    calc.click('zero', '(小数部3桁入力)0を入力')
    calc.click('period', '(小数部3桁入力).を入力')
    calc.click('one', '(小数部3桁入力)1を入力')
    calc.click('two', '(小数部3桁入力)2を入力')
    calc.click('three', '(小数部3桁入力)3を入力(0.123)')

    calc.clear()
    calc.click('zero', '(小数部4桁入力)0を入力')
    calc.click('period', '(小数部4桁入力).を入力')
    calc.click('one', '(小数部4桁入力)1を入力')
    calc.click('two', '(小数部4桁入力)2を入力')
    calc.click('three', '(小数部4桁入力)3を入力(0.123)')
    calc.click('four', '(小数部4桁入力)4を入力(0.123のまま)')

    calc.clear()
    calc.click('one', '(整3+小3桁入力)1を入力')
    calc.click('two', '(整3+小3桁入力)2を入力')
    calc.click('three', '(整3+小3桁入力)3を入力(123)')
    calc.click('period', '(整3+小3桁入力).を入力')
    calc.click('four', '(整3+小3桁入力)4を入力')
    calc.click('five', '(整3+小3桁入力)5を入力')
    calc.click('six', '(整3+小3桁入力)6を入力(123.456)')

#
# 詳細設計
#


def test331():
    """ 3.3.1 初期処理 プログラムを開始すると、入力待ちモードに遷移する。また、「＝」ボタンは無効化する。 """
    print('3.3.1 初期処理 プログラムを開始すると、入力待ちモードに遷移する。また、「＝」ボタンは無効化する。')
    print('Calculator.py実施直後に確認済み')


def test3321():
    """ 3.3.2.1 入力待ちモード """
    print('3.3.2.1 入力待ちモード 操作エリアから「0 ～ 9」か「．」の入力がある場合は、入力情報を表示エリアに表示し、入力処理 1 に遷移する。ただし、未入力の状態で「．」を選択した場合は、「0.」を表示する。')
    print('3.2.1.1, 3.2.1.2で実施済み')


def test3322():
    """ 3.3.2.2 入力処理 1 モード、入力処理 2 モード
    >操作エリアから「0 ～ 9」か「．」の入力がある場合は、表示エリアに数値を表示する。ただし、以下のルールがある。
    >
    > 数値が既に存在する場合は、右から連結して表示する
    > 例：12 の状態で 1 を入力すると、121 となる"""
    print('3.3.2.2 入力処理 1 モード、入力処理 2 モード')
    calc.clear()
    for i in range(3):
        v = random.randint(0, 9)
        calc.click(calc.zero2nine[v], f'{v}を入力')
    """ > 先頭に 0 がある場合は、0 を 2 回続けて入力できない。また、0 の後に数値を入力した場合は、0 を別の数値に上書きする """
    calc.clear()
    calc.click('zero', '0を入力')
    calc.click('zero', '続けて0を入力(表示の0は一つのまま)')

    for i in range(1, 10):
        calc.clear()
        calc.click('zero', '0を入力')
        calc.click(calc.zero2nine[i], f'{i}を入力(0が消えてこの値のみ表示されている)')

    """ > 未入力の状態で「.」を選択した場合は、先頭に 0.を付与する """
    calc.clear()
    calc.click('period', '.を入力(0.が表示されている)')

    """ > 小数は最大で 3 桁までしか入力できない """
    """ > 入力値の制限は、最大値（999.999）、最小値（－999.999）とする """
    calc.clear()
    v1 = str(random.randint(100, 999))
    calc.typewrite(v1, f'整数部として{v1}を入力')

    v2 = random.randint(0, 9)
    calc.click(calc.zero2nine[v2], f'更に{v2}をクリック。{v1}のままである')

    calc.click('period', '.を入力')

    v3 = str(random.randint(100, 999))
    calc.typewrite(v3, f'小数部として{v3}を入力')

    v4 = random.randint(0, 9)
    calc.click(calc.zero2nine[v4], f'更に{v4}をクリック。{v1}.{v3}のままである')


def test3331():
    """ 3.3.3.1 入力処理 1 モード 演算子（＋、－、＊、／、％）を入力した場合は、表示エリアの入力情報と入力した演算子を記憶し、入力処理 2
    に遷移する。また、表示エリアをクリアし、（＋、－、＊、／、％）ボタンを無効化し、「＝」ボタンを有効化する。"""
    print('3.3.3.1 入力処理 1 モード 演算子（＋、－、＊、／、％）を入力した場合は、表示エリアの入力情報と入力した演算子を記憶し、入力処理 2 に遷移する。また、表示エリアをクリアし、（＋、－、＊、／、％）ボタンを無効化し、「＝」ボタンを有効化する。')
    # + - * / %
    for calcchar in calc.calcchar:
        input_val1 = ''
        calc.clear()

        # 整数部３桁入力
        for i in range(3):
            v = random.randint(0, 9)
            calc.click(calc.zero2nine[v])
            input_val1 = input_val1 + str(v)

        calc.click('period')
        input_val1 = input_val1 + '.'

        # 小数部３桁入力
        for i in range(3):
            v = random.randint(0, 9)
            calc.click(calc.zero2nine[v])
            input_val1 = input_val1 + str(v)

        calc.confirm(f'{input_val1}が入力された')
        calc.click(
            calc.calcchar[calcchar],
            f'{calcchar}が入力され、+-*/%が無効化され、=が有効化された')

        input_val2 = ''

        # 整数部３桁入力
        for i in range(3):
            v = random.randint(0, 9)
            calc.click(calc.zero2nine[v])
            input_val2 = input_val2 + str(v)

        calc.click('period')
        input_val2 = input_val2 + '.'

        # 小数部３桁入力
        for i in range(3):
            v = random.randint(0, 9)
            calc.click(calc.zero2nine[v])
            input_val2 = input_val2 + str(v)

        left_side = input_val1 + ' ' + calcchar + ' ' + input_val2
        result = eval(left_side)
        calc.click('equal', f'{input_val2}が入力され=が入力された。{result} =が無効化された')


def test3332():
    """ 3.3.3.2 入力待ちモード 繰り返し演算（1回演算した後、続けて演算子（＋、－、＊、／、％）を入力）した場合は、表示エリアの入力情報と選択した演算子を取得する。さらに、表示エリアをクリアし、入力処理
     2 に遷移する。また、「＋、－、＊、／、％」ボタンを無効化、「＝」ボタンを有効化する。 """
    print('3.3.3.2 入力待ちモード')
    calc.clear()
    calc.confirm('最初の演算(=を入力)後+を入力した時点で「＋、－、＊、／、％」ボタンを無効化、「＝」ボタンを有効化')

    calc.clear()
    calc.convert2input('1 + 3 = + 4 =', 8, calc.typewrite)
    calc.clear()
    calc.convert2input('2 + 3 = + 4 =', 9, calc.click_string)
    calc.clear()
    calc.convert2input('122 + 8 = + 5 =', 135, calc.click_string)

    calc.clear()
    calc.confirm('最初の演算(=を入力)後-を入力した時点で「＋、－、＊、／、％」ボタンを無効化、「＝」ボタンを有効化')
    calc.convert2input('1 + 3 = - 4 =', 0, calc.click_string)

    calc.clear()
    calc.confirm('最初の演算(=を入力)後*を入力した時点で「＋、－、＊、／、％」ボタンを無効化、「＝」ボタンを有効化')
    calc.convert2input('1 + 3 = * 4 =', 16, calc.click_string)

    calc.clear()
    calc.confirm('最初の演算(=を入力)後/を入力した時点で「＋、－、＊、／、％」ボタンを無効化、「＝」ボタンを有効化')
    calc.convert2input('1 + 3 = / 4 =', 1, calc.click_string)

    calc.clear()
    calc.confirm('最初の演算(=を入力)後%を入力した時点で「＋、－、＊、／、％」ボタンを無効化、「＝」ボタンを有効化')
    calc.convert2input('1 + 3 = % 3 =', 1, calc.click_string)

    calc.clear()
    calc.convert2input('1.5 + 3.3 = * 4 =', 19.2, calc.click_string)
    calc.clear()
    calc.convert2input('999.999 * 999.999 =', 999998.000001, calc.click_string)


def test3341():
    """> 　特殊演算を行う場合は、演算結果を表示エリアに表示する。
        >
        > 表示エリアが空欄以外で、√ を入力する場合は、表示エリアの入力情報から平方根を演算し、表示エリアに表示する。なお、出力が小数第 4 位以降となる場合は、小数第 4 位を四捨五入し、3 桁で表示する。
        > 表示エリアが空欄以外で、＋／－を入力する場合は、表示エリアの入力情報から符号を反転し、表示エリアに表示する。 """
    print('3.3.4.1 入力待ちモード、入力処理 1 モード、入力処理 2 モード')
    # root
    s1 = str(100)
    print(s1)
    calc.clear()
    calc.click('root', 'rootをクリックしても何も起きない')
    calc.click('nine', '9をクリック')
    calc.click('root', f'rootをクリック。{math.sqrt(9)}')
    calc.clear()
    calc.click('three', '3をクリック')

    result = Decimal(str(math.sqrt(3))).quantize(
        Decimal('0.001'), rounding=ROUND_HALF_UP)
    calc.click('root', f'rootをクリック。{result}')

    # + and -
    calc.clear()
    calc.confirm('何も無い状態でプラス・マイナスを押す')
    calc.click('plusandminus')
    calc.confirm('何も起きない')

    calc.clear()
    for strnum in ['456', '123.456', '0.000', '999.999']:
        calc.click_string(strnum)
        calc.click('plusandminus')
        calc.confirm(f'{strnum} to -{strnum}')
        calc.clear()

    calc.clear()
    for strnum in ['456', '123.456', '0.000', '999.999']:
        calc.click_string(strnum)
        calc.click('plusandminus')
        calc.confirm('マイナス')
        calc.click('plusandminus')
        calc.confirm('プラス')
        calc.click('plusandminus')
        calc.confirm('マイナス')
        calc.clear()


def test335():
    """ 3.3.5 クリアイベント
     > 3.3.5.1 入力待ちモード、入力処理 1 モード、入力処理 2 モード
     > 　「C」を選択した場合は、表示エリアの文字、表示エリアと演算子の入力情報、ボタンの状態を初期状態に戻す。
     また、入力待ちモードに遷移する。"""
    print('3.3.5 クリアイベント')
    calc.clear()
    calc.confirm('1 + 2 Cが入力で、Cがクリックされた時点で=のみ無効であることを確認する')
    calc.convert2input('1 + 2 C', 0, calc.click_string)
    calc.confirm('入力待ちモード。=だけ無効化されていることを確認する')
    calc.convert2input('3 + 4 =', 7, calc.click_string)


def test3361():
    # 3.3.6.1 入力待ちモード、入力処理 2 モード
    print('3.3.6.1 入力待ちモード、入力処理 2 モード')
    """ > 　表示エリアが空欄でない状態で、「＝」ボタンを選択した場合、下記の演算結果を表示エリアに表示し、入力待ちモードに遷移する。遷移する際、「＋、－、＊、／、％」ボタンを有効化し、＝」を無効化する。
    なお、出力結果は、小数となる場合は、小数第 4 位を四捨五入し、3 桁として表示する。
    >
    > 通常の演算の場合
    > 演算子が「＋」の場合
    > 演算結果＝入力処理 1 モードの入力情報＋入力処理 2 モードの入力情報"""

    calc.clear()
    calc.click('one', '1を入力')
    calc.confirm('=が無効化されていることを確認')
    calc.click('two', '2を入力(12になる)')
    calc.confirm('=が無効化されていることを確認')
    calc.click('three', '3を入力(123になる)')
    calc.confirm('=が無効化されていることを確認')
    calc.click('plus', '+を入力(=が有効化されるが表示エリアは空白')
    calc.confirm('=が有効化されるが表示エリアは空白。これが正しいか不明')
    calc.click('seven', '7を入力')
    calc.confirm('=が有効化されていることを確認。まだ押なさい')
    calc.click('seven', '7を入力')
    calc.click('equal', '(設計書の確認事項)=を入力(200)。=のみが無効化されることを確認する')
    calc.confirm('ここから繰り返し演算')
    calc.click('plus', '+を入力(=が有効化されるが表示エリアは空白')
    calc.confirm('=が有効化されるが表示エリアは空白。これが正しいか不明')
    calc.click_string('145')
    calc.click('equal', '(設計書の確認事項)=を入力(345)。=のみが無効化されることを確認する')

    """ > 演算子が「－」の場合
    > 演算結果＝入力処理 1 モードの入力情報－入力処理 2 モードの入力情報"""

    calc.clear()
    calc.click('one', '1を入力')
    calc.confirm('=が無効化されていることを確認')
    calc.click('two', '2を入力(12になる)')
    calc.confirm('=が無効化されていることを確認')
    calc.click('three', '3を入力(123になる)')
    calc.confirm('=が無効化されていることを確認')
    calc.click('minus', '-を入力(=が有効化されるが表示エリアは空白)')
    calc.confirm('=が有効化されるが表示エリアは空白。これが正しいか不明)')
    calc.click('two', '2を入力')
    calc.confirm('=が有効化されていることを確認。まだ押なさい')
    calc.click('three', '3を入力')
    calc.click('equal', '(設計書の確認事項)=を入力(100)。=のみが無効化されることを確認する')
    calc.confirm('ここから繰り返し演算')
    calc.click('minus', '-を入力(=が有効化されるが表示エリアは空白)')
    calc.confirm('=が有効化されるが表示エリアは空白。これが正しいか不明)')
    calc.click_string('77')
    calc.click('equal', '(設計書の確認事項)=を入力(23)。=のみが無効化されることを確認する')

    """ > 演算子が「＊」の場合
    > 演算結果＝入力処理 1 モードの入力情報＊入力処理 2 モードの入力情報"""
    calc.clear()
    calc.click_string('0.123')
    calc.confirm('=が無効化されていることを確認')
    calc.click('asterisc', '*を入力(=が有効化されるが表示エリアは空白)')
    calc.confirm('=が有効化されるが表示エリアは空白。これが正しいか不明')
    calc.click_string('0.456')
    calc.confirm('=が有効化されていることを確認')
    calc.click('equal', '(設計書の確認事項)=を入力(0.056)。=のみが無効化されることを確認する')
    calc.confirm('ここから繰り返し演算')
    calc.click('asterisc', '*を入力(=が有効化されるが表示エリアは空白)')
    calc.confirm('=が有効化されるが表示エリアは空白。これが正しいか不明')
    calc.click_string('999.999')
    calc.click('equal', '(設計書の確認事項)=を入力(56)。=のみが無効化されることを確認する')

    """ > 演算子が「／」の場合
    > 演算結果＝入力処理 1 モードの入力情報／入力処理 2 モードの入力情報"""
    calc.clear()
    calc.click_string('0.123')
    calc.confirm('=が無効化されていることを確認')
    calc.click('slash', 'slashを入力(=が有効化されるが表示エリアは空白)')
    calc.confirm('=が有効化されるが表示エリアは空白。これが正しいか不明')
    calc.click_string('0.456')
    calc.confirm('=が有効化されていることを確認')
    calc.click('equal', '(設計書の確認事項)=を入力(0.27)。=のみが無効化されることを確認する')
    calc.confirm('ここから繰り返し演算')
    calc.click('slash', 'slashを入力(=が有効化されるが表示エリアは空白)')
    calc.confirm('=が有効化されるが表示エリアは空白。これが正しいか不明')
    calc.click_string('333.333')
    calc.click('equal', '(設計書の確認事項)=を入力(0.001)。=のみが無効化されることを確認する')

    """ > 演算子が「％」の場合
    > 演算結果＝入力処理 1 モードの入力情報％入力処理 2 モードの入力情報"""
    calc.clear()
    calc.click_string('8')
    calc.confirm('=が無効化されていることを確認')
    calc.click('percent', '%を入力(=が有効化されるが表示エリアは空白)')
    calc.confirm('=が有効化されるが表示エリアは空白。これが正しいか不明')
    calc.click_string('3')
    calc.confirm('=が有効化されていることを確認')
    calc.click('equal', '(設計書の確認事項)=を入力(2)。=のみが無効化されることを確認する')

    calc.clear()
    calc.click_string('89')
    calc.confirm('=が無効化されていることを確認')
    calc.click('percent', '%を入力(=が有効化されるが表示エリアは空白)')
    calc.confirm('=が有効化されるが表示エリアは空白。これが正しいか不明')
    calc.click_string('9')
    calc.confirm('=が有効化されていることを確認')
    calc.click('equal', '(設計書の確認事項)=を入力(8)。=のみが無効化されることを確認する')

    calc.confirm('ここから繰り返し演算')
    calc.click('percent', '%を入力(=が有効化されるが表示エリアは空白)')
    calc.confirm('=が有効化されるが表示エリアは空白。これが正しいか不明')
    calc.click_string('3')
    calc.click('equal', '(設計書の確認事項)=を入力(2)。=のみが無効化されることを確認する')

    """ > 繰り返し演算の場合
    > 演算子が「＋」の場合
    > 演算結果＝入力待ちモードの入力情報＋入力処理 2 モードの入力情報
    > 演算子が「－」の場合
    > 演算結果＝入力待ちモードの入力情報－入力処理 2 モードの入力情報
    > 演算子が「＊」の場合
    > 演算結果＝入力待ちモードの入力情報＊入力処理 2 モードの入力情報
    > 演算子が「／」の場合
    > 演算結果＝入力待ちモードの入力情報／入力処理 2 モードの入力情報
    > 演算子が「％」の場合
    > 演算結果＝入力待ちモードの入力情報％入力処理 2 モードの入力情報


    > 　また、演算結果の最大、最小の処理は以下とする。
    > 最大：演算結果＞ 3000 の場合
    > 演算結果＝ 3000
    > 最小：演算結果＜－3000 の場合
    > 演算結果＝－3000 """
    print('最大値、最小値')

    calc.clear()
    calc.click_string('501')
    calc.click('asterisc', '*を入力')
    calc.click('six', '6を入力')
    calc.click('equal', '=を入力結果は3000')

    calc.clear()
    calc.click_string('501')
    calc.click('plusandminus', '+-をクリック')
    calc.click('asterisc', '*を入力')
    calc.click('six', '6を入力')
    calc.click('equal', '=を入力結果は-3000')


def test34():
    """ 3.4 制限事項
    > テスト項目を記述するのが面倒になることが予想されるため、プログラムに入力できる最大、最小の数値は 999.999
    と－999.999 に制限する。また、演算結果の最大、最小は、3000 と－3000 に制限する """
    print('3.4 制限事項')
    calc.clear()
    calc.click_string('999.999')
    calc.click('plus', '+を入力')
    calc.click_string('999.999')
    calc.click('equal', '=を入力。1999.998')

    calc.clear()
    calc.click_string('999.999')
    calc.click('plusandminus', '+-をクリック')
    calc.click('minus', '-を入力')
    calc.click_string('999.999')
    calc.click('equal', '=を入力。-1999.998')


def keep_time():

    dt_now = datetime.datetime.now()
    print(f'\n{dt_now}')


keep_time()
# test31()  # script  -c 'python ../test.py' test31.log

# test3211()  # script  -c 'python ../test.py' test32.log
# test3212()
# test3213()
# test3214()
# test3215()
# test3216()
# test3221()
# test3222()
# test323()
# test324()

# test331()  # script  -c 'python ../test.py' test331.log

# test3321()  # script  -c 'python ../test.py' test332.log
# test3322()

# test3331()  # script  -c 'python ../test.py' test3331.log
# test3332()  # script  -c 'python ../test.py' test3332.log

# test3341()  # script  -c 'python ../test.py' test334.log

# test335()  # script  -c 'python ../test.py' test335.log

# test3361()  # script  -c 'python ../test.py' test336.log

test34()  # script  -c 'python ../test.py' test34.log
