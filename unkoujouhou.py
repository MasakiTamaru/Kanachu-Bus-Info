#神奈中バスロケで乗りたいバスのurlを変数に入れておくと
#プログラムを実行したらどのバスがあと何分で到着するかを表示

#時間管理
import datetime

# スクレイピングに必要なモジュールをインポート
import urllib.request as req
import sys
sys.path.append('/home/pi/.local/lib/python3.5/site-packages/')
from bs4 import BeautifulSoup

now = datetime.datetime.now()

url = "http://real.kanachu.jp/pc/displayapproachinfo?fNO=11140&tNO=11223&fNM=%8B%DA%82%AA%92%4A%92%63%92%6E%91%4F%28%89%A1%95%6C%8E%73%8D%60%93%EC%8B%E6%29&tNM=%8F%E3%91%E5%89%AA%89%77%28%89%A1%95%6C%8E%73%8D%60%93%EC%8B%E6%29"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

result = []      #何系統のバスか
when = []        #到着情報1
becoming = []   #到着情報2


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

#resultの要素数を10に調整
new_result = []
for i in range(19):
    if i % 2 == 0:
        new_result.append(zip(result[i], result[i+1]))

for new_result, when, becoming in zip(new_result, when, becoming):
    print(list(new_result), when, becoming)