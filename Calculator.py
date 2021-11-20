#
# プログラム：電卓プログラム(Calculator.py)
# 作成者：T.Yamaura, Y.Ohmori
#
import tkinter
import tkinter as tk
import math
from tkinter import RIGHT

#電卓アプリケーションクラス
class Calculator(tk.Frame):
  def __init__(self, master):
    super().__init__(master)

    #GUIの設定
    master.title('電卓アプリケーション')
    master.geometry('290x380')
    master.resizable(0,0)

    self.operator = ''

    dispFlame = tk.LabelFrame(master)
    btnFlame = tk.LabelFrame(master)
    dispFlame.pack()
    btnFlame.pack()

    self.display = tk.Entry(dispFlame, width=22, justify=RIGHT,font=10)
    self.display.pack()

    #入力値の最大・最小値
    self.MAX_VALUE = 999.999
    self.MIN_VALUE = -999.999

    #ボタン設定と配置
    btn7 = tk.Button(btnFlame, text="7", font=15, width=4,height=2,command=lambda: self.btn_clk('7'))
    btn8 = tk.Button(btnFlame, text="8", font=15, width=4,height=2,command=lambda: self.btn_clk('8'))
    btn9 = tk.Button(btnFlame, text="9", font=15, width=4,height=2,command=lambda: self.btn_clk('9'))
    btn4 = tk.Button(btnFlame, text="4", font=15, width=4,height=2,command=lambda: self.btn_clk('4'))
    btn5 = tk.Button(btnFlame, text="5", font=15, width=4,height=2,command=lambda: self.btn_clk('5'))
    btn6 = tk.Button(btnFlame, text="6", font=15, width=4,height=2,command=lambda: self.btn_clk('6'))
    btn3 = tk.Button(btnFlame, text="3", font=15, width=4,height=2,command=lambda: self.btn_clk('3'))
    btn2 = tk.Button(btnFlame, text="2", font=15, width=4,height=2,command=lambda: self.btn_clk('2'))
    btn1 = tk.Button(btnFlame, text="1", font=15, width=4,height=2,command=lambda: self.btn_clk('1'))
    btn0 = tk.Button(btnFlame, text="0", font=15, width=4,height=2,command=lambda: self.btn_clk('0'))    
    self.plus_btn = tk.Button(btnFlame, text="+", font=15, width=4,height=2, command=lambda: self.operate('+'))
    self.minus_btn = tk.Button(btnFlame, text="-", font=15, width=4,height=2, command=lambda: self.operate('-'))
    self.multi_btn = tk.Button(btnFlame, text="*", font=15, width=4,height=2, command=lambda: self.operate('*'))
    self.div_btn = tk.Button(btnFlame, text="/", font=15, width=4,height=2, command=lambda: self.operate('/'))
    self.eq_btn = tk.Button(btnFlame, text="=", font=15, width=4,height=2,command=lambda: self.calculate())
    clear_btn = tk.Button(btnFlame, text="C", font=15, width=4,height=2,command=lambda: self.clear_clk())
    self.dot_btn = tk.Button(btnFlame, text=".", font=15, width=4,height=2,command=lambda: self.btn_clk('.'))
    sqrt_btn = tk.Button(btnFlame, text="√", font=15, width=4,height=2,command=lambda: self.sp_clk('root'))
    surplus_btn = tk.Button(btnFlame, text="%", font=15, width=4,height=2,command=lambda: self.operate('%'))    
    negate_btn = tk.Button(btnFlame, text="+/-", font=15, width=4,height=2,command=lambda: self.sp_clk('+/-'))      
    
    self.plus_btn.grid(row=0,column=0,sticky='WE')
    self.minus_btn.grid(row=0,column=1,sticky='WE')  
    self.multi_btn.grid(row=0,column=2,sticky='WE')    
    self.div_btn.grid(row=0,column=3,sticky='WE')      
    btn1.grid(row=1,column=0,sticky='WE')
    btn2.grid(row=1,column=1,sticky='WE')
    btn3.grid(row=1,column=2,sticky='WE')
    btn4.grid(row=2,column=0,sticky='WE')
    btn5.grid(row=2,column=1,sticky='WE')
    btn6.grid(row=2,column=2,sticky='WE')
    btn7.grid(row=3,column=0,sticky='WE')
    btn8.grid(row=3,column=1,sticky='WE')
    btn9.grid(row=3,column=2,sticky='WE')
    btn0.grid(row=3,column=3,sticky='WE')
    self.eq_btn.grid(row=1,column=3,sticky='WE')
    clear_btn.grid(row=2, column=3,sticky='WE')
    self.dot_btn.grid(row=4,column=0,sticky='WE')
    sqrt_btn.grid(row=4, column=1,sticky='WE')    
    surplus_btn.grid(row=4, column=2,sticky='WE')    
    negate_btn.grid(row=4, column=3,sticky='WE')   

    self.eq_btn.config(state=tk.DISABLED) 
    
  #数値、.の入力処理
  def btn_clk(self, arg):
    dispStr = self.display.get()    
    if arg.isdigit() == True:    
      if int(arg) >= 0 or int(arg) <= 9:
        if self.display.get() == "0" and int(arg) == 0:
          pass
        else:
          if self.display.get() == "0":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, arg)
            self.MinMax(dispStr)
          else:
            if dispStr.find('.') != -1:
              splitStr = dispStr.split('.')
              if len(splitStr[-1]) < 3:
                self.display.insert(tk.END, arg)
                self.MinMax(dispStr)
            else:
              self.display.insert(tk.END, arg)
              self.MinMax(dispStr)
    elif str(arg) == '.':
      if dispStr == '': 
        self.display.insert(tk.END, 0)
        self.display.insert(tk.END, arg)
      elif dispStr.find('.') != -1:
        pass
      else:
        self.display.insert(tk.END, arg)
        self.dot_btn.config(state=tk.DISABLED)

  #特殊計算
  def sp_clk(self,arg):
    dispStr = self.display.get()
    if self.display.get() != '':
      if arg == '+/-':
        #符号反転
        if self.display.get().find('-') == -1:
          self.display.insert(0, '-')
        else:
          self.display.delete(0, tk.END)
          self.display.insert(0, dispStr.strip('-'))
      elif arg == 'root':
        #平方根の計算
        value = format(math.sqrt(float(self.display.get())),'.3f') 
        value = str(value)

        while True:
          if ("." in value and value[-1] == "0") or (value[-1] == "."):
            value = value[:-1]
            continue
          break

        self.display.delete(0, tk.END)
        self.display.insert(0, value)        

  #クリア処理
  def clear_clk(self):
    self.val1 = 0
    self.operator = ''
    self.display.delete(0, tk.END)
    self.dot_btn.config(state=tk.NORMAL)
    self.btn_able()    

  #ボタンクリック無効化
  def btn_disable(self):
    self.plus_btn.config(state=tk.DISABLED)
    self.minus_btn.config(state=tk.DISABLED)
    self.multi_btn.config(state=tk.DISABLED)
    self.div_btn.config(state=tk.DISABLED)

  #ボタンクリック有効化
  def btn_able(self):
    self.plus_btn.config(state=tk.NORMAL)
    self.minus_btn.config(state=tk.NORMAL)
    self.multi_btn.config(state=tk.NORMAL)
    self.div_btn.config(state=tk.NORMAL)
    self.dot_btn.config(state=tk.NORMAL)

  #入力値の最大・最小の判定
  def MinMax(self, preStr):
    if float(self.display.get()) > self.MAX_VALUE or float(self.display.get()) < self.MIN_VALUE:
      self.display.delete(0, tk.END)
      self.display.insert(tk.END, preStr)

  #演算子入力
  def operate(self, dat):
    if self.display.get() != '' and dat != '':
      self.operator = dat
      self.val1 = self.display.get()
      self.display.delete(0, tk.END)
      self.btn_disable()
      self.dot_btn.config(state=tk.NORMAL)
      self.eq_btn.config(state=tk.NORMAL)

  #演算処理
  def calculate(self):
    if self.display.get() != '':
      val1 = float(self.val1)
      val2 = float(self.display.get())
      if self.operator == '+':
        result = float(format(val1 + val2, '.3f'))
      elif self.operator == '-':
        result = float(format(val1 - val2, '.3f'))
      elif self.operator == '*':
        result = float(format(val1 * val2, '.3f'))
      elif self.operator == '/':
        result = float(format(val1 / val2, '.3f'))
      elif self.operator == '%':
        result = float(format(val1 % val2, '.3f'))      
      elif self.operator == '':
        return

      #最大値・最小値のリミット処理
      if result > 3000:
        result = 3000
      elif result < -3000:
        result = -3000

      result = str(result)
      while True:
        if ("." in result and result[-1] == "0") or (result[-1] == "."):
          result = result[:-1]
          continue
        break

      self.display.delete(0, tk.END)
      self.display.insert(0, result)
      self.btn_able()
      self.eq_btn.config(state=tk.DISABLED) 

#メインルーチン
def main():
  win = tk.Tk()
  root = Calculator(master=win)
  root.mainloop()

if __name__ == "__main__":
  main()


