# -*- coding: utf-8 -*-
from urllib.request import urlopen, Request
import urllib
import bs4
from datetime import datetime

location = '전주 상산고'
enc_location = urllib.parse.quote(location + '+날씨')

url = 'https://www.weather.go.kr/w/index.do' + enc_location
print(url)

req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html, 'html5lib')
temp_info = soup.find('div', class_='weather_graphic')
feel_info = soup.find('div', class_='sort')

if temp_info:
    curr_temp = temp_info.find('div', class_='temperature_text').text
    print('현재 ' + location + curr_temp + '입니다.')
else:
    print('현재 ' + location + ' 날씨 정보를 가져올 수 없습니다.')
    
if feel_info:
    curr_temp_feel = feel_info.find('dd', class_='desc').text
    print('현재 ' + location + ' 체감 온도는 ' + curr_temp_feel + '입니다.')
else:
    print('현재 ' + location + ' 날씨 정보를 가져올 수 없습니다.')





