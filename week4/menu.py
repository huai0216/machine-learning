"""
Created on Fri Oct  7 14:39:38 2022

@author: huai

"""
import ipywidgets as widgets
from IPython.display import display, clear_output
#options
meal_dic = {
    '無\t':0,
    '牛肉麵\t100元':100,
    '肉燥飯\t50元':50,
    '餛飩麵\t70元':70,
    }
dessert_dic = {
    '無\t':0,
    '薯餅\t25元':25,
    '熱狗\t20元':20,
    '雞塊\t30元':30,
    }
drink_dic ={
    '無\t':0,
    '紅茶\t20元':20,
    '檸檬紅茶\t25元':25,
    '奶茶\t30元':30,
    }
#Drop down list
meal = widgets.Dropdown(
    options = meal_dic.keys(),
    value = '無\t',
    description = "主食: ",
    disabled = False,
)

dessert = widgets.Dropdown(
    options = dessert_dic.keys(),
    value = "無\t",
    description = "附餐: ",
    disabled = False,
)
drink = widgets.Dropdown(
    options = drink_dic.keys(),
    value = '無\t',
    description = "飲料",
    disabled = False,
)
meal_amount = widgets.BoundedIntText(
    value=0,
    min=0,
    max=10,
    step=1,
    description='數量: ',
    disabled=False
)

dessert_amount = widgets.BoundedIntText(
    value=0,
    min=0,
    max=10,
    step=1,
    description='數量: ',
    disabled=False
)

drink_amount = widgets.BoundedIntText(
    value=0,
    min=0,
    max=10,
    step=1,
    description='數量: ',
    disabled=False
)

#shopping bag or nah
bag = widgets.Checkbox(
    #value = True,
    description = "加購購物袋1元",
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
button_check = widgets.Button(description="確認訂單")
out = widgets.Output()
#定義函示

def on_button_check_clicked(_):
      price = meal_dic[meal.value]*meal_amount.value\
            +dessert_dic[dessert.value]*dessert_amount.value\
              +drink_dic[drink.value]*drink_amount.value
      with out:
        clear_output()
        if(meal_amount.value==0) and (dessert_amount.value==0)and(drink_amount.value==0):
          print("你沒有點任何餐點，請重新下單")
        elif(meal_amount.value==0):
          meal.value = "無\t"
          
          if(dessert_amount.value == 0) : 
            dessert.value = "無\t"
          elif(drink_amount.value == 0) :
            drink.value = "無\t"
        else :
          if(dessert_amount.value==0):
            dessert.value = "無\t"
          elif(drink_amount.value==0):
            drink.value = "無\t"
        if(meal.value == "無\t") :
          meal_amount.value = 0
          if(dessert.value == '無\t'):
            dessert_amount.value = 0
          elif(drink.value == '無\t'):
            drink.value = 0
        else :
          if(dessert.value == "無\t"):
            dessert_amount.value = 0
          elif(drink.value == '無\t'):
            drink_amount.value = 0
        if(bool(bag.value)):
          price += 1
          print("您點的\n主餐為:{}\t數量:{}\n附餐為:{}\t數量:{}\n飲料為:{}\t數量:{}\n加購一個購物袋\t1 元\n總金額為\t{}元"\
                .format(meal.value,meal_amount.value,dessert.value,dessert_amount.value,drink.value,drink_amount.value,price))
        else:
          print("您點的\n主餐為:{}\t數量:{}\n附餐為:{}\t數量:{}\n飲料為:{}\t數量:{}\n總金額為\t{}元"\
                .format(meal.value,meal_amount.value,dessert.value,dessert_amount.value,drink.value,drink_amount.value,price))
        #          .format(meal.value,meal_amount.value,dessert.value,dessert_amount.value,drink.value,drink_amount.value,price))
        # if(bool(bag.value)):
        #   price += 1
        #   print("您點的主餐為:{}{}份，附餐為:{}{}份，飲料為:{}{}份，加點購物袋的金額為\t{}元"\
        #          .format(meal.value,meal_amount.value,dessert.value,dessert_amount.value,drink.value,drink_amount.value,price))
        # else :
        #   print("您點的主餐為:{}{}份，附餐為:{}{}份，飲料為:{}{}份，總金額為{}元"\
        #         .format(meal.value,meal_amount.value,dessert.value,dessert_amount.value,drink.value,drink_amount.value,price))
        # else :
        #     print("您點的主餐為:{}{}份，附餐為:{}{}份，飲料為:{}{}份，總金額為{}元"\
        #           .format(meal.value,meal_amount.value,dessert.value,dessert_amount.value,drink.value,drink_amount.value,price))

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
button_check.on_click(on_button_check_clicked)


#排版
v_meal = widgets.VBox([button_beef,button_rice,button_noodles])
v_dessert = widgets.VBox([button_hash, button_chicken, button_hotdog])
v_drink = widgets.VBox([button_blacktea, button_lemon, button_milktea])
order_meal = widgets.HBox([v_meal, meal, meal_amount,])
order_dessert = widgets.HBox([v_dessert, dessert, dessert_amount])
order_drink = widgets.HBox([v_drink, drink, drink_amount])
order_bag = widgets.HBox([bag, button_check])

menu = widgets.Tab([order_meal, order_dessert, order_drink, order_bag])
menu.set_title(0,"主食")
menu.set_title(1,"附餐")
menu.set_title(2,"飲料")
menu.set_title(3,"加購")
display(menu)
display(out)

