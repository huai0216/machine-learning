"""
Created on Fri Oct  7 14:39:38 2022

@author: huai

"""
import ipywidgets as widgets
from IPython.display import display, clear_output

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

meal = widgets.Dropdown(
    options = meal_dic.keys(),
    value = '無',
    description = "主食: ",
    disabled = False,
)

dessert = widgets.Dropdown(
    options = dessert_dic.keys(),
    value = "無",
    description = "點心: ",
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
order_meal = widgets.HBox([meal, amount_meal])
order_dessert = widgets.HBox([dessert, amount_dessert])
order_drink = widgets.HBox([drink, amount_drink])
display(order_meal)
display(order_dessert)
display(order_drink)
