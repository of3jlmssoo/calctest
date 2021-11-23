# def convert2input(self, input, output):
#     """
#    '1 + 3 = * 4 =' の場合
#        eval        pyautogui
#     1   1           typewrite(1)
#     +   1 + click('+')
#     3   1 + 3       typewrite(3)
#     =   r = eval(1 + 3) click('=')
#     *   r * click(*)
#     4   r * 4       typewrite(4)
#     =   r = eval(r * 4) click('=')

#     """
#     result = 0
#      target = ''

#       input_list = input.split()
#        for i in input_list:
#             # if i not in ['+', '-', '*', '/', '=', '%']:
#             #     print(f'type {i}')
#             # else:
#             #     print(f'click {i}')

#             if i == '=':
#                 # calc.typewrite(str(target), f'{target}')
#                 calc.click('equal', '= was typed')
#                 result = eval(target)
#                 target = str(result)
#             elif i in self.calcchar.keys():
#                 calc.click(self.calcchar[i], f'click {i}')
#                 target = target + i
#             else:
#                 calc.typewrite(i, f'{i} was typed')
#                 target = target + i
#         self.confirm(f'{input} : eval result {result} and result {output}')

def funcA(secondarg=''):
    print('funcA', secondarg)


def funcB(secondarg=''):
    print('funcB', secondarg)


def func_caller(func, secondarg=''):
    print(f'func_caller called {func=}')
    func(secondarg)
    print('func_caller ended')


func_caller(funcA)
func_caller(funcA, 'original message')
