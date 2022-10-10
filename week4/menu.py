#建立元件
button_red = widgets.Button(description="紅色藥丸")
button_blue = widgets.Button(description="藍色藥丸")
out = widgets.Output()

#定義函式
def on_button_red_clicked(_):
      with out:
          clear_output()
          print("領你去看真相！")
def on_button_blue_clicked(_):
      with out:
          clear_output()
          print("歡迎來到安逸的虛擬世界～")
            
#設定按鈕被按下後會觸發的函式
button_red.on_click(on_button_red_clicked)
button_blue.on_click(on_button_blue_clicked)

#排版並輸出
#results = widgets.HBox([button_red,button_blue,out])
#results
display(button_red)
display(button_blue)
display(out)