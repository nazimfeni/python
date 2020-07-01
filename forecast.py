import pandas as pd
import requests # the modul is used for get request
from bs4 import BeautifulSoup #used for displayinf data

page=requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XvqMgqEzZ0w')

soup=BeautifulSoup(page.content,'html.parser')

week=soup.find(id='seven-day-forecast-body')

items=week.findAll(class_='tombstone-container')

period_names=[item.find(class_='period-name').get_text() for item in items]
short_descs=[item.find(class_='short-desc').get_text() for item in items]
temps=[item.find(class_='temp').get_text() for item in items]

weather_data=pd.DataFrame(
{

    'Period':period_names,
    'Short_Desc': short_descs,
    'Temperature':temps


})

print(weather_data)
weather_data.to_csv('result.csv') # export in CSV