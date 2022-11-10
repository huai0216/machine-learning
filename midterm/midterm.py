import requests
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import fontManager
import ipywidgets as widgets
import folium
from IPython.display import display, clear_output
import time

# def Missing_Counts( Data, NoMissing=True ) : 
#     missing = Data.isnull().sum()  
    
#     if NoMissing==False :
#         missing = missing[ missing>0 ]
        
#     missing.sort_values( ascending=False, inplace=True )  
#     Missing_Count = pd.DataFrame( { 'Column Name':missing.index, 'Missing Count':missing.values } ) 
#     Missing_Count[ 'Percentage(%)' ] = Missing_Count['Missing Count'].apply( lambda x: '{:.2%}'.format(x/Data.shape[0] ))
#     return  Missing_Count
#read data
data = pd.read_csv('NPA_TD1.csv')
city_list = []
region_list = []

#create dataframe
select_df = pd.DataFrame(dict)

#get city name
for city_name in data["CityName"]:
  if city_name not in city_list:
    city_list.append(city_name)

city_list.remove("設置縣市")
city_list.remove(city_list[0])

#create dropdown selection
dict = {"CityName":data['CityName'],
      "RegionName":data['RegionName'],
      "Address":data['Address'],

}
question_dict = {"相機數量排名":0,
          "國道三號南到北經過數量":1,
          "顯示地圖":2      
           }
#create dropdown
city_drop = widgets.Dropdown(
    options = city_list,
    value = '連江縣',
    description = "設置縣市:",
    disabled = False,
)
question_drop = widgets.Dropdown(
    options = question_dict.keys(),
    value = "相機數量排名",
    description = "我想要",
    disabled = False,
)

#rank top 5 popo
count_branch = data['BranchNm'].value_counts()
count_df = count_branch.to_frame(name = "Count")
count_df = count_df.sort_values(by=['Count'], ascending=False).head()

#calculate number of cameras
camera = data[(data["CityName"]=="國道三號") & (data["direct"]=="往北")]
camera['CityName'].count()

#create map
map_data_lo = camera['Longitude'].to_list()
map_data_la = camera['Latitude'].to_list() 
fmap = folium.Map(location=[23.5827104, 121.320408], zoom_start=8)
for i in range(0, len(map_data_lo)):
    folium.Marker(
    location=[float(map_data_la[i]), float(map_data_lo[i])],
    popup="測速照相!!",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(fmap)

#create button
button_search = widgets.Button(description = "查詢")
button_question = widgets.Button(description = "查詢")
out = widgets.Output()

#show mandarin font
!wget -O TaipeiSansTCBeta-Regular.ttf https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download
fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

#set button
def on_button_search_clicked(b):
  with out:
    clear_output()
    print(select_df[(select_df["CityName"]==str(city_drop.value))])
def on_button_question_clicked(b):
  with out:
    clear_output()
    if(question_drop.value == "相機數量排名"):
      clear_output()
      print(count_df)
      count_df.plot(kind='bar')
      plt.title('數量前五名')
      plt.grid(True)
      plt.show(block=False)
      plt.close('all')
    elif(question_drop.value == "國道三號南到北經過數量"):
      clear_output()
      plt.show(block=False)
      plt.close('all')
      camera = data[(data["CityName"]=="國道三號") & (data["direct"]=="往北")]
      print("國道三號南到北一共會經過:\n{}台\n測速照相機".format(camera['CityName'].count()))
      
    elif(question_drop.value == "顯示地圖"):
      plt.show(block=False)
      plt.close('all')
      display(fmap)

#trigger
button_search.on_click(on_button_search_clicked)
button_question.on_click(on_button_question_clicked)

#composition
tab1 = widgets.HBox([city_drop,button_search])
tab2 = widgets.HBox([question_drop,button_question])
menu = widgets.Tab([tab1,tab2])
menu.set_title(0,"各縣市測速照相機")
menu.set_title(1,"我還想查詢")

#display
display(menu)
display(out)
