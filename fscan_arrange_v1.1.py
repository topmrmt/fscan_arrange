# -*- coding:utf-8 -*-
#############################
#   _  _  ____  _  _  ____  #
#  ( \/ )(  _ \( \/ )(_  _) #
#  / \/ \ )   // \/ \  )(   #
#  \_)(_/(__\_)\_)(_/ (__)  #
#      fscan_arrange v1.1   #
#############################
import xlsxwriter
import re

ip_lis = []
lis_ok = []
with open('/Users/mistermt/Desktop/192.txt','r',encoding='GBK',errors='ignore') as f:
    lis = f.readlines()
    rawstr = "^(\d+\.\d+\.\d+\.\d+)\:(\d+) open"
    for line in lis:
        result = re.findall(rawstr,line)
        if len(result):
            line = line.split(' ')[0]
            lis_ok.append(line)
            ip_ = line.split(':')[0]
            print(ip_)
            ip_lis.append(ip_)

new_lis = list({}.fromkeys(ip_lis).keys())

dk = []
list_ip = []
for i in lis_ok:
    num00 = i.split(':')[0]
    num01 = i.split(':')[1]
    ip_dic = {}
    ip_dic[str(num00)] = str(num01)
    list_ip.append(ip_dic)

print(list_ip)

# list_ip = [{"1":"a"},{"1":"b"},{"2":"c"},{"2":"d"}]
#准备一个空的字典，放最终结果
list_res = {}
#遍历原始数据
for item in list_ip:
    #拿到最终字典的所有key
    keys = list(list_res.keys())
    #取每次遍历item的key
    key_item = list(item.keys())[0]
    #判断该key值是否在最终字典中存在，如果存在，则value值进行拼接；如果不存在，则添加数据
    if key_item in keys:
        list_res[key_item] = list_res[key_item] + " " + item[key_item]
    else:
        list_res[key_item] = item[key_item]

# 建文件及sheet.
workbook = xlsxwriter.Workbook('jieguo0209.xlsx')
worksheet = workbook.add_worksheet()

# Write some data headers. 带自定义粗体blod格式写表头
worksheet.write('A1', '序号')
worksheet.write('B1', 'IP')
worksheet.write('C1', '端口')

all_keys = list(list_res.keys())
all_ip_list =[]
for key in all_keys:
    all_ip_list.append([key,list_res[key]])

print(all_ip_list)

# Start from the first cell below the headers.
row = 1
col = 0

# Iterate over the data and write it out row by row.
i = 1
for ip, port in (all_ip_list):
    worksheet.write(row, col, i)
    worksheet.write(row, col + 1, ip)    # 带默认格式写入
    worksheet.write(row, col + 2, port,)  # 带自定义money格式写入
    row += 1
    i += 1

workbook.close()