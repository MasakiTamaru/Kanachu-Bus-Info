#神奈中バスロケで乗りたいバスのurlを変数に入れておくと
#プログラムを実行したらどのバスがあと何分で到着するかを表示

#時間管理
import datetime
now = datetime.datetime.now()

# スクレイピングに必要なライブラリをインポート
import urllib.request as req
import sys
sys.path.append('/home/pi/.local/lib/python3.5/site-packages/')
from bs4 import BeautifulSoup

# chrome driver and selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep

# headless mode
from selenium.webdriver.chrome.options import Options
options = Options()
# options.add_argument('--headless') # if this row is not comment out, headless mode.

# -------------------------------------------------------------------------------------------

# input バージョン
# where_to_take_the_bus = input('乗車バス停名: ')
# where_to_get_off_the_bus = input('降車バス停名: ')


where_to_take_the_bus = '芹が谷団地前'
where_to_get_off_the_bus = '上大岡駅'

driver = webdriver.Chrome('C:\Test_Folder\chromedriver_win32\chromedriver', options=options)
driver.set_page_load_timeout(100)    # 少し待機
driver.get('http://real.kanachu.jp/pc/top')
search_first_bar = driver.find_element_by_name("fNM")
search_first_bar.send_keys(where_to_take_the_bus)
search_second_bar = driver.find_element_by_name("tNM")
search_second_bar.send_keys(where_to_get_off_the_bus)
search_second_bar.submit()

driver.set_page_load_timeout(300)    # 少し待機
url = driver.current_url
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

result = []      #何系統のバスか
when = []        #到着情報1
becoming = []    #到着情報2
all_info = ""    #上記のすべての情報を持った配列

inner_list = soup.find_all(class_="inner2 pa01")

#table 左の情報をスクレイピング

#何系統のバスか
for inner in inner_list:
    wrap_list = inner.find_all(class_="wrap")
    for wrap in wrap_list:
        col_list = wrap.find_all(class_="col01")
        for col in col_list:
            table_list = col.find_all(class_="table01")
            for table in table_list:
                result_row = []
                cell = table.get_text()
                tmp_1 = cell.replace("\n", "")
                tmp_2 = tmp_1.replace("\t", "")
                tmp_3 = tmp_2.replace("\r", "")
                result_row.append(tmp_3)
                result.append(result_row)

#到着情報1
for wrap in wrap_list:
    col_list = wrap.find_all(class_="col02")
    for col in col_list:
        frame_list = col.find_all(class_="frameBox03")
        for frame in frame_list:
            title_list = frame.find_all(class_="title01")
            for title in title_list:
                result_row_1 = []
                cell_1 = title.get_text()
                tmp_4 = cell_1.replace("\n", "")
                tmp_5 = tmp_4.replace("\t", "")
                tmp_6 = tmp_5.replace("\r", "")
                tmp_7 = tmp_6.replace("\u3000", "")
                result_row_1.append(tmp_7)
                when.append(result_row_1)

#到着情報2
for wrap in wrap_list:
    col_list = wrap.find_all(class_="col02")
    for col in col_list:
        frame_list = col.find_all(class_="frameBox03")
        for frame in frame_list:
            wrap_1_list = frame.find_all(class_="wrap")
            for wrap_1 in wrap_1_list:
                departure_list = wrap_1.find_all(class_="placeArea01 departure")
                for departure in departure_list:
                    result_row_2 = []
                    cell_2 = departure.get_text()
                    tmp_8 = cell_2.replace("\n", "")
                    tmp_9 = tmp_8.replace("\t", "")
                    tmp_10 = tmp_9.replace("\r", "")
                    result_row_2.append(tmp_10)
                    becoming.append(result_row_2)


#ここから下で情報表示
print("データ取得時刻: " + str(now.hour) + "時" + str(now.minute) + "分" + str(now.second) + "秒")

# #resultの要素数を調整
bus_num_info = []
bus_time_info = []
for i in range(len(result)):
    if i % 2 == 0:
        bus_num_info.append(result[i])
    else:
        bus_time_info.append(result[i])

f = open('result.txt', 'w', encoding='utf-8', newline='\n')

for i in range(int(len(result) / 2)):
    f.writelines(str(bus_num_info[i]) + str(bus_time_info[i]) + str(when[i]) + str(becoming[i]) + '\n')

f.close()

# webページを閉じる
driver.close()