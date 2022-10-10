"""
Created on Fri Oct  7 14:39:38 2022

@author: huai

"""
import ipywidgets as widgets
from IPython.display import display, clear_output
#options
meal_dic = {
    '無':0,
    '牛肉麵\t100元':100,
    '肉燥飯\t50元':50,
    '餛飩麵\t70元':70,
    }
dessert_dic = {
    '無':0,
    '薯餅\t25元':25,
    '熱狗\t20元':20,
    '雞塊\t30元':30,
    }
drink_dic ={
    '無':0,
    '紅茶\t20元':20,
    '檸檬紅茶\t25元':25,
    '奶茶\t30元':30,
    }
#Drop down list
meal = widgets.Dropdown(
    options = meal_dic.keys(),
    value = '無',
    description = "主食: ",
    disabled = False,
)

dessert = widgets.Dropdown(
    options = dessert_dic.keys(),
    value = "無",
    description = "附餐: ",
    disabled = False,
)
drink = widgets.Dropdown(
    options = drink_dic.keys(),
    value = '無',
    description = "飲料",
    disabled = False,
)

amount_meal = widgets.Text(
    value='0',
    placeholder='請輸入數量',
    description='數量: ',
    disabled=False
)
amount_dessert = widgets.Text(
    value = "0",
    placeholder = "請輸入數量",
    description = "數量: ",
    disabled = False
)
amount_drink = widgets.Text(
    value = "0",
    placeholder = "請輸入數量",
    description = "數量: ",
    disabled = False
)

#shopping bag or nah
bag = widgets.Checkbox(
    #value = True,
    description = "加購購物袋",
    diabled = False
)

#read pic
file = open("beef_noodles.jpg", "rb")
beef = file.read()
file = open("Fried_Pork_Rice.jpg", "rb")
rice = file.read()
file = open("wonton_noodles.jpg", "rb")
noodles = file.read()
file = open("potato_cake.jpg", "rb")
hash = file.read()
file = open("chicken_nuggets.jpg", "rb")
chicken = file.read()
file = open("hot_dog.jpg", "rb")
hotdog = file.read()
file = open("black_tea.jpg", "rb")
blacktea = file.read()
file = open("lemon_black_tea.jpg", "rb")
lemon = file.read()
file = open("milk_tea.jpg", "rb")
milktea = file.read()

#build button
button_beef   = widgets.Button(description="牛肉麵")
button_rice   = widgets.Button(description="肉燥飯")
button_noodles = widgets.Button(description="餛飩麵")
button_hash   = widgets.Button(description="薯餅")
button_chicken = widgets.Button(description="雞塊")
button_hotdog  = widgets.Button(description="熱狗")
button_blacktea = widgets.Button(description="紅茶")
button_lemon  = widgets.Button(description="檸檬紅茶")
button_milktea= widgets.Button(description="奶茶")

#定義函示
def on_button_beef_clicked(_):
      with out:
        clear_output()
        display(
          widgets.Image(
            value = beef,
            format = 'jpg',
            width = 150,
            height = 150,
          )  
        )
        
def on_button_rice_clicked(_):
      with out:
        clear_output()
        display(
          widgets.Image(
                value = rice,
                format = 'jpg',
                width = 150,
                height = 150,
            )
        )

def on_button_noodles_clicked(_):
      with out:
        clear_output()
        display(
            widgets.Image(
                value = noodles,
                format = 'jpg',
                width = 150,
                height = 150,
            )
        )

def on_button_hash_clicked(_):
      with out:
        clear_output()
        display(
            widgets.Image(
                value = hash,
                format = 'jpg',
                width = 150,
                height = 150,
            )
        )
def on_button_chicken_clicked(_):
      with out:
        clear_output()
        display(
            widgets.Image(
                value = chicken,
                format = 'jpg',
                width = 150,
                height = 150,
            )
        )
def on_button_hotdog_clicked(_):
      with out:
        clear_output()
        display(
            widgets.Image(
                value = hotdog,
                format = 'jpg',
                width = 150,
                height = 150,
            )
        )
def on_button_blacktea_clicked(_):
      with out:
        clear_output()
        display(
            widgets.Image(
                value = blacktea,
                format = 'jpg',
                width = 150,
                height = 150,
            )
        )
def on_button_lemon_clicked(_):
      with out:
        clear_output()
        display(
            widgets.Image(
                value = lemon,
                format = 'jpg',
                width = 150,
                height = 150,
            )
        )
def on_button_milktea_clicked(_):
      with out:
        clear_output()
        display(
            widgets.Image(
                value = milktea,
                format = 'jpg',
                width = 150,
                height = 150,
            )
        )

button_beef.on_click(on_button_beef_clicked)
button_rice.on_click(on_button_rice_clicked)
button_noodles.on_click(on_button_noodles_clicked)
button_hash.on_click(on_button_hash_clicked)
button_chicken.on_click(on_button_chicken_clicked)
button_hotdog.on_click(on_button_hotdog_clicked)
button_blacktea.on_click(on_button_blacktea_clicked)
button_lemon.on_click(on_button_lemon_clicked)
button_milktea.on_click(on_button_milktea_clicked)


#排版
v_meal = widgets.VBox([button_beef,button_rice,button_noodles])
v_dessert = widgets.VBox([button_hash, button_chicken, button_hotdog])
v_drink = widgets.VBox([button_blacktea, button_lemon, button_milktea])
order_meal = widgets.HBox([v_meal, meal, amount_meal,])
order_dessert = widgets.HBox([v_dessert, dessert, amount_dessert])
order_drink = widgets.HBox([v_drink, drink, amount_drink])

menu = widgets.Tab([order_meal, order_dessert, order_drink, bag])
menu.set_title(0,"主食")
menu.set_title(1,"附餐")
menu.set_title(2,"飲料")
menu.set_title(3,"加購")
display(menu)
display(out)

