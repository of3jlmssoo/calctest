[『テストでバグ発見！（5）電卓プログラムに潜むバグ【出題編】』](https://monoist.itmedia.co.jp/mn/articles/2111/17/news009.html?utm_source=pocket_mylist)

- マウスでクリックしてのテストは面倒なので pyautogui を試してみる(主目的)
- テストのバリエーションが少ないためかバグは大きく 1 種類しか見つけることができなかった(%が無効化されない)
- バグにあたるのかわからないが遷移表ついて以下の所感を参照
- pyautogui を一通り試せたのでテストバリエーションを増やすことは一旦おいておく

## 所感

以下テストを一通り終えての所感。

- 入力待ちモードの定義が明確になっていないように読める。『3.3.1 初期処理　プログラムを開始すると、入力待ちモードに遷移する。また、「＝」ボタンは無効化する。』とあるが、入力待ちモードで「＝」ボタンは無効化されるのか、プログラムを開始して「＝」ボタンは無効化されるのか分からない。
- 入力待ちモードを表示エリアに何も表示されていない状態とすることもできない。モード遷移の際に表示エリアがクリアされてしまうため、"1+2="を入力する場合”+"を入力した時点で表示エリアがクリアされる。この際は入力処理 2 モードにいるはずである。
- 遷移表では入力待ちモードにおいて演算子入力イベントが発生した場合入力情報取得が行われ、入力処理 2 へ遷移する。しかし、プログラム起動直後やクリアで入力待ちモードになった場合、入力情報を取得できない。よって入力処理 2 へ遷移しない。
- 入力待ちモードの特殊演算においては特殊演算が行われ、入力待ちモードへ遷移(継続)することになっているが、ここでは入力値が無いため特殊演算は実行されない。
- 入力待ちモード、入力処理１モード、入力処理２モードが定義されているが画面上どのモードにいるか見た目で判断することが困難
- 入力エリアにカーソルをあわせ数値をキーボードから入力することができる。これを許容するのか不明
- 可能であればレイアウトを変更してもらいたい。演算子のうち％だけが離れてしまっている。また、％のレイアウトにより、2 つの特殊演算子が分断されている。デザイン上のこだわりがある場合やこのレイアウトがユーザーにとって使いやすいという場合はこの限りではないが

## ファイル

test.py : テスト実施用プログラム。アプリ表示位置を固定してテストを実施する。pyautogui が初のため設計書の記載を順にテストしている。
テストログ.md : 設計書の記載とそのテスト結果のメモ
readme.md : このファイル
