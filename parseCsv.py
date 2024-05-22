# 15/5/2024
# created By atrox.he


import csv
import os
# from decimal import Decimal, getcontext
# getcontext().prec = 6
# 输入新文件夹和旧文件夹路径
new_folder = input("drop NEW OVL Log here:")
old_folder = input("drop POR OVL Log here:")

new_folder = new_folder.rstrip()
old_folder = old_folder.rstrip()

# 读取新文件夹和旧文件夹中的time.csv文件
new_time_csv = new_folder + '/system/time.csv'
old_time_csv = old_folder + '/system/time.csv'

# 读取新文件夹和旧文件夹中的records.csv文件

new_records_csv = new_folder + '/system/records.csv'
old_records_csv = old_folder + '/system/records.csv'


# 读取新文件夹中的ActionName和Duration数据
new_data = {}
with open(new_time_csv, 'r') as new_file:
    csv_reader = csv.DictReader(new_file)  
    for row in csv_reader:
        k = row["ActionName"]
        v = row["Duration"]
        new_data[k] = v
        # print(new_data)

# 读取旧文件夹中的ActionName和数据
old_data = {}
with open(old_time_csv, 'r') as old_file:
    csv_reader = csv.DictReader(old_file)
    for row in csv_reader:
        k = row["ActionName"]
        v = row["Duration"]
        old_data[k] = v
        # print(old_data)

# 读取新文件夹records.csv里面的test items
new_data_ = {}
with open(new_records_csv, 'r') as new_file:
    csv_reader = csv.DictReader(new_file)
    i = 1
    for row in csv_reader:
        if row["subSubTestName"] != '':
            v = row["subSubTestName"]
            new_data_[i] = v
            i = i + 1

old_data_ = {}
with open(old_records_csv, 'r') as new_file:
    csv_reader = csv.DictReader(new_file)
    i = 1 
    for row in csv_reader:
        if row["subSubTestName"] != '':
            v = row["subSubTestName"]
            old_data_[i] = v
            i = i + 1


#写入计算结果到新的csv文件
output_file = new_folder + '___output.csv'
with open(output_file, 'w', newline='') as file:

    csv_writer = csv.writer(file)
    csv_writer.writerow(['Test time compare', 'ActionName', 'delta(new OVL TT - old OVL TT)'])

    for k in new_data:
        if k in old_data:
            diff = float(new_data[k]) - float(old_data[k])
            print(diff)
            csv_writer.writerow(['', k, diff])
        else:
            csv_writer.writerow(['', k, "NEW add"])

    for k in old_data:
        if k not in new_data:
            csv_writer.writerow(['', k, "deleted"])

    csv_writer.writerow(['', '', ''])
    csv_writer.writerow(['test coverage compare',  'subSubTestName'])

    for K,v in new_data_.items():
        if v not in old_data_.values():
            csv_writer.writerow(['' , v , 'new add test coverage'])


    for k,v in old_data_.items():
        if v not in new_data_.values():
            csv_writer.writerow(['' , v , 'deleted test coverage'])

print("输出output.csv成功")
