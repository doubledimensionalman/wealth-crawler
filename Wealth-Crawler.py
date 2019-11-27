import requests
import json
import xlwt
import time
proname=list()
prolink=list()
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Worksheet')
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
for i in range(1,696):
    response = requests.get("http://finance.ccb.com/cn/finance/productnews_json/financelist_2852_{}.js".format(i),headers = headers)
    response.encoding = 'utf-8'
    new_str=response.text.replace("financeListCallback","").replace("\t","").replace("\n","").replace(" ","").replace("(","").replace(")","")
    print(new_str)
    new_dict=json.loads(new_str)
    for inf in new_dict["list"]:
        proname.append(inf["TITLE"])
        prolink.append(inf["FILENAME"])
        print(inf["TITLE"])
        print(inf["FILENAME"])
    #time.sleep(1)
    print(i)

for j in range(len(prolink)):
    worksheet.write(j,1,label=proname[j])
    worksheet.write(j,0,label=prolink[j])
        
workbook.save(r'D:\User Data\Desktop\wealth1.xls')

