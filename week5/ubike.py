import csv
import ipywidgets as widgets
from IPython.display import display, clear_output
sarea_dic = {
    '新店區':0,
    '汐止區':1,
    '三重區':2,
    '新莊區':3,
    '蘆洲區':4,
    '中和區':5,
    '永和區':6,
    '板橋區':7,
    '泰山區':8,
    '土城區':9,
    '樹林區':10,
    '鶯歌區':11,
    '淡水區':12,
    '五股區':13,
    '三峽區':14,
    '林口區':15,
    '瑞芳區':16,
    '深坑區':17,
    '八里區':18
}
show_dic = {
    '所有站點':0,
    '有車可借的站點':1,
    '無車可借的站點':2,

}
ad_drop = widgets.Dropdown(
    options = sarea_dic.keys(),
    value = '新店區',
    description = "行政區",
    disabled = False,
)
show_drop = widgets.Dropdown(
    options = show_dic.keys(),
    value = '所有站點',
    description = "請幫我顯示",
    disabled = False
)
snum = widgets.Checkbox(
    #value = True,
    description = "編號",
    disabled = False,
)
# sna = widgets.Checkbox(
#     #value = True
#     description = "站名",
#     disabled = False
# )
tot = widgets.Checkbox(
    #value = True
    description = "停車格數量",
    disabled = False
)
sbi = widgets.Checkbox(
    description = "目前可借數量",
    disabled = False
)
# sarea = widgets.Checkbox(
#     description = "行政區",
#     disabled = False
# )
mday = widgets.Checkbox(
    description = "資料更新時間",
    disabled = False
)
lat = widgets.Checkbox(
    description = "經度",
    disabled = False
)
lng = widgets.Checkbox(
    description = "經度",
    disabled = False
)
ar = widgets.Checkbox(
    description = "位址",
    disabled = False
)
# sareaen = widgets.Checkbox(
#     description = "Administrative area",
#     disabled = False
# )
snaen = widgets.Checkbox(
    description = "site name",
    disabled = False
)
aren = widgets.Checkbox(
    description = "address",
    disabled = False
)
bemp = widgets.Checkbox(
    description = "空位數量",
    disabled = False
)
act = widgets.Checkbox(
    description = "全站禁用狀態",
    disabled = False    
)
button_search = widgets.Button(description = "查詢")
out = widgets.Output()
col1 = widgets.VBox([ar,tot,sbi,bemp])
col2 = widgets.VBox([act,mday,lat,lng])
col3 = widgets.VBox([snaen,aren])
choose = widgets.HBox([ad_drop, show_drop])
check = widgets.HBox([col1,col2,col3,button_search])
ubike = widgets.Tab([choose, check])
#ubike = widgets.VBox([choose,check,button_search])
ubike.set_title(0,"我想要查詢")
ubike.set_title(1,"我還想要看")
def on_button_search_clicked(b):
  with out:
    clear_output()
    print("編號_站名",end='')
    num_show = 0
    x=[]
    if(ar.value == 1):
      print('_位址',end='')
      x.append(8)
      num_show += 1
    if(tot.value == 1):
      x.append(2)
      num_show += 1
      print('_停車格數量',end='')
    if(sbi.value == 1):
      x.append(3)
      num_show += 1
      print('_目前可借數量',end='')
    if(bemp.value == 1):
      x.append(12)
      num_show += 1
      print('_空位數量',end='')
    if(act.value == 1):
      x.append(13)
      num_show += 1
      print('_全站禁用狀態',end = '')
    if(mday.value == 1):
      x.append(5)
      num_show += 1
      print('_資料更新時間', end = '')
    if(lat.value == 1):
      x.append(6)
      num_show += 1
      print('_經度', end = '')
    if(lng.value == 1):
      x.append(7)
      num_show += 1
      print('_緯度', end = '')
    if(snaen.value == 1):
      x.append(10)
      num_show += 1
      print('_site name', end = '')
    if(aren.value == 1):
      x.append(11)
      num_show += 1
      print('_address', end = '')

    with open('ntpc_youbike.csv','r',encoding = 'utf8') as csvfile:
      plots = csv.reader(csvfile, delimiter=',')
      print('\n')
      for row in plots:
        
        count = 0
        if(str(row[4]) == ad_drop.value):
          
            if(show_drop.value == "所有站點"):
              print(row[0]+"_"+row[1],end='')
              if(num_show == 0):
                print('\n')
              else :
                for i in range(num_show):
                  print("_"+row[int(x[i])],end = '')
                  count += 1
                  if count == num_show:
                    print('\n')
            elif(show_drop.value == "有車可借的站點"):
              if(str(row[3])!='0'):
                print(row[0]+"_"+row[1],end='')
                if(num_show == 0):  
                  print('\n')
                else :
                  for i in range(num_show):
                    print('_'+row[int(x[i])],end = '')
                    count += 1
                    if count == num_show:
                      print('\n')
            elif(show_drop.value == "無車可借的站點"):
              if(str(row[3])=='0'):
                print(row[0]+"_"+row[1],end='')
                if(num_show == 0):
                  print('\n')
                else :  
                  for i in range(num_show):
                    print('_'+row[int(x[i])],end = '')
                    count += 1
                    if count == num_show:
                      print('\n')

button_search.on_click(on_button_search_clicked)
display(ubike)
display(out)